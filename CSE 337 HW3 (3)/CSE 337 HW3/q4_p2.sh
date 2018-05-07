#!/bin/bash

for i in 1 2 3 4 5 6 7 8 9 10
do
	newdir=""
	rem=$(($i %2))
	
	if !(($rem))
	then
		newdir="even" 
		newdir="$newdir$i"
		mkdir "$newdir"
		chmod a+r "$newdir"
		chmod u+w "$newdir"
		chmod g+w "$newdir"
		chmod a-x "$newdir"
	else
		newdir="odd"
		newdir="$newdir$i"
		mkdir "$newdir"
		chmod a+r "$newdir"
		chmod a-w "$newdir"
		chmod a-x "$newdir"
	fi
done
