#!/bin/bash

read -p "Enter a string: " input
normalized=$(echo "$input" | tr -d '[:space:]' | tr '[:upper:]' '[:lower:]')
reversed=$(echo "$normalized" | rev)

if [ "$normalized" = "$reversed" ]; then
    echo "'$input' is a palindrome."
else
    echo "'$input' is not a palindrome."
fi

