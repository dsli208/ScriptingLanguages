#!/bin/bash
count=$#
max=0
min=10000000000
total=0

for i do
	echo $i
	if (($i<min))
	then
		min=$i
	elif (($i>max))
	then
		max=$i
	((total+=$i))
	fi
done
mean=$((total/count))
echo "Mean is $mean, min is $min, and max is $max"
