#!/bin/bash

logfiles = "filepath/"

if [ ! -e "$logfiles" ]; then 
    echo "this files is exists"
    exit 1
fi

awk '{print $1}' "$logfiles" | sort | uniqu -c | sort -c | awk '$1 > 1' > repeaded_ip.txt

if [ -s repeaded_ip.txt ]; then 
    echo "Ip are replaede"
else
    echo "no ip"
fi

count=1
while [ $count -le 5 ]; do
    echo "Count $count"
    ((count++))
done


for i in {1..5}; do
    echo "Iteration $i"
done


if [ condition ]; then
    # commands if condition is true
elif [ another_condition ]; then
    # commands if another_condition is true
else
    # commands if none of the conditions are true
fi
