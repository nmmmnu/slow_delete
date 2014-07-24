#!/bin/sh

find $1 -depth | while read file
do
	echo -f $file
	sleep 0.1
done

