#!/bin/bash
  
i=1  
while read line; do  
    python3 main.py $1 $line | grep True && echo -e "\e[42m[*] WE GOT A HIT: $1:$line\e[0m"
    i=$((i+1))
done < $2
exit
