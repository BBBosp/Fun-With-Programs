#!usr/bin/bash/env python
#################################
#Cody Atkinson
#python fizzbuzz
#february 26, 2015
#################################
x=0 #declare x as chosen variable
y=0
z=0
a=0
import time
while x<=1000: #initiate a count to 100
	if (x%3==0 and x%5==0): 	#combine conditions for fizz and buzz 
		print("FizzBuzz")	#print only for defined fizzbuzz
		y=y+1
	elif (x%3==0):			#define condition for fizz
		print ("Fizz")		#print fizz
		z=z+1
	elif(x%5==0):			#define condition for buzz
		print("Buzz")		#print buzz
		a=a+1
	else: print (x)			#if no fizz buzz conditions are met print number
#	time.sleep(.007)
	x=x+1 				#increase x by one to reiterate
print ('Out of ',x)
print ('FizzBuzz=',y)
print ('Fizz=',z)
print ('Buzz=',a)
