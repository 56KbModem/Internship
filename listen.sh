#!/bin/bash

FILE=/tmp/pipe

function looping
{
     while true;
      do
          cat /tmp/pipe;
      done | nc -lnvp 4000 > out.txt &
}

if [ -e $FILE ]; then
   looping
else
   mkfifo /tmp/pipe;
   looping
fi

# (c) Nick Snel
