#!/bin/bash

factorial() {
    local n=$1
    local result=1
    for (( i=2; i<=n; i++ )); do
        result=$((result * i))
    done
    echo $result
}

read -p "Enter a number: " number
if [[ $number -lt 0 ]]; then
    echo "Factorial is not defined for negative numbers."
else
    echo "Factorial of $number is $(factorial $number)"
fi
