#!/bin/bash

if [ $# -eq 0 ]
then
  exit 1
fi

name="$1"
echo "Greeting, $name"
date "+%d-%m-%Y"
date "+%H:%M:%S"
ps aux | grep -v "ps aux" | grep -v "grep" | wc -l
cat /etc/os-release