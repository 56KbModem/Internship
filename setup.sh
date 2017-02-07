#!/bin/sh

zero=0;

killall listen.sh
killall nc
./demo.py

if [ $zero -eq $? ]; then
	echo "LAUNCHING LISTENER!"
	socat -,raw,echo=0 tcp-listen:5151
else
	echo "SOMETHING WENT WRONG!"
fi
