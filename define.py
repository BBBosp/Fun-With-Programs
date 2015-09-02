#!/usr/bin/env python
########################
#program name
#program function
#Cody Atkinson
#date
#
########################
import time
def countdown(upper,lower):
	for thing in range (upper, lower, -1):
		print(thing)
		time.sleep(1)
print("ignition")
countdown(10,0)
print("lift off")
