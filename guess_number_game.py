#! /bin/python3

# Author Github,Facebook,Twitter,Instagram,GitHub: @syedalizain033 (syedalizain03@gmail.com)
#Remember this is totally beginner level code with no classes and proper structure. You are welcome in changing code to classes or proper shape :)

import random
import os
initial_level=1
less="Less than your number."
large="larger than your number."
score=0

def generate_guess(level):
	gen=5*level
	guess=random.randint(0,gen)
	return guess
	
def gameStart(level,death):
	
	death=death+1
	level1(level,death)

def level1(level,death):
	print("Level {0} ".format(level))
	os.system('sleep 1')
	print("\nNumbers will be ranging from 0 to {0}".format(level*5))
	guess=generate_guess(level)
	nextLevel=level
	death_copy=death
	#print(guess) This is the number one have to guess. You can remove #. This is for testing purpose
	print("\nOkay! I have a number in my mind. You have to guess it. You have {0} chances.".format(death))
	print("Life: {0}".format(death))
	os.system('sleep 2')
	while  death>=0:
		
		if (death==0):
			print("Your life is over. Better try next time.")
			print("Your total score is {0}".format(level-1))
			break
		try:
			ans=int(input("What is the number? Tell me: "))
			
			if ans > guess:
				print("My number is "+less)
				death=death-1
				print("Life: {0}".format(death))
			elif ans < guess:
				print("My number is "+large)
				death=death-1
				print("Life: {0}".format(death))
			elif ans==guess:
				print("Congratulations! You cleared the level.\n")
				print("++++++++++++++++++++++++++++++++++++++++++++")
				os.system('sleep 2')
				nextLevel+=1
				gameStart(nextLevel,death_copy)
		except ValueError:
			print("Invalid input. Enter correct value i.e. number")
			
			
def level0(level):
	print("Welcome to Guessing game. You will be asked for the number I will be having in mind. Let's start\n\n")
	gameStart(level,2)
	
level0(initial_level) #It's calling function from main() 
