#!/bin/bash

while :
do

	find /seccam -mtime +2 -exec rm {} \;
	sleep 1d
done
