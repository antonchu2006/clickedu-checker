#!/bin/bash
  
i=1  
while read line; do  
    python3 checker.py $1 $line | grep HIT && echo -e "\e[42m[*] WE GOT A HIT: $1:$line\e[0m" && echo "$1:$line" >> hits.txt | grep "[*] WE GOT A HIT:"
    i=$((i+1))
done < $2
exit
