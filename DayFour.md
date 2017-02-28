### Rock paper scissors :scissors:

I pulled a heckin rookie move and forgot to save my last day four which was like 2 weeks ago. It was also reading week and I fell off earth. To my loyal 0 followers my apologies.

TODAY I was feeling like trying to figure out a simple game I could easily make better with pygame, I decided on Rock Paper Scissors and in 10 minutes made this attrocious version. 


Cash me in a week with the gameified version of this **HOW BOW DAH?** :girl:

```python
import random

player = 0

CPU = 0

print("Rock (r), paper (p) or scissor (s)?")
foo = input()

if foo == 'p':
	cpu = random.randrange(0,3)
	if cpu == 0:
		print("you win!")
	elif cpu == 1:
		print("you tie")
	else:
		print("you lose")

elif foo == 'r':
	cpu = random.randrange(0,3)
	if cpu == 0:
		print("you tie")
	elif cpu == 1:
		print("you lose")
	else:
		print("you win")

elif foo == 's':
	cpu = random.randrange(0,3)
	if cpu == 0:
		print("you lose")
	elif cpu == 1:
		print("you win")
	else:
		print("you tie")

else:
	print("lol")

print("cpu was " + str(cpu) )

```

Don't Stop Believin,

Stooph :sparkles:
