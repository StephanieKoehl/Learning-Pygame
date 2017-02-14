### Back 2 Basics

I started to get frustrated with Python, I haven't used it in almost 3 years and I've gotten a little rusty. I decided to go back to basics and read up on some basic python programming from Al Sweigart and his book 
(Invent Your Own Computer Games with Python)[https://inventwithpython.com/] which I would highly recommend.

I got re-excited with making super simple text based games, while slightly modifying his guessing game below:

```python

#Learning Pygame
#Stephanie

import random

guessesTaken = 0
flag = True

print('Hello What is your name?')
name = input()
print('cool, nice to meet you ' + name + ' try to guess my number btw 1 and 20')
number = random.randint(1,20)

while guessesTaken < 6:
	print('take a guess')
	guess = input()
	guess = int(guess)

	guessesTaken = guessesTaken + 1

	if guess < number:
		print('too low')

	if guess > number:
		print('too high')

	if guess == number:
		flag = False
		break #jump immediately out of the loop

if flag == False:
	guessesTaken = str(guessesTaken)
	guessesTaken = print('Good job it took u ' + guessesTaken + ' guesses')

if flag == True:
	number = str(number)
	print('no u dum shit it was ' + number)
  
  ```
  
  this was actually my first time using ```break``` . I had a Computer Science teacher who hates breaks and called it lazy programming (*which is fair*) 
  but it made things super simple and fast. I'm excited to use breaks in further programming.
  
  ###final notes
  
  I've been in a bit of a slump these past couple days so haven't been overly motivated to do much. Today's progress: 3 cookie-making grandmas at a bake sale :older_woman:
  
  Until next time my d00ds
