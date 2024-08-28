#!/bin/bash

# Define the file, the line number, the word to replace, and the new word
file="example.txt"
line_number=5
oldword="oldword"
newword="newword"

# Replace the word in the specified line using sed
sed -i "${line_number}s/$oldword/$newword/" "$file"
