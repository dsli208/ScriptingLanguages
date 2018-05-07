#!/bin/bash

echo -n "Enter a sentence: "
read -e -a sentence
totalChars=0
for c in ${sentence[@]}
do
	((totalChars+=${#c}))
	((totalChars++))
done
((totalChars--))
numWords=${#sentence[@]}
echo "$totalChars total characters and $numWords total words"
