## Baby come back :baby:
March 21, 2017

I've been really busy with other projects, I cant believe its almost been a month :scream_cat:

Today I plan to finish up sprite movement for the pygame, and then read more of the book on pygame. I've decided, if possible, at the end of this to make a comprehensive guide overviewing everything I've learned and how to easily make a game.

### Movement :running:
Instead of our dude just moving straight across the x-axis, let's add some y movement so he kind of jumps across the screen.

In the `__init__ (self):` definition (function), add `self.y_speed = 5`. This sets the speed the sprite will move to be 5 (same as the x axis). Whenever the sprite moves now it will move diagonally, so when we update lets add that too: `self.rect.y += self.y_speed` this lets the sprite move in both directions at the same time

Finally, lets make sure it doesn't go off the screen:

```python

if self.rect.bottom > HEIGHT - 150: #ensuring it doesnt run off the bottom of screen
  self.y_speed = -5 #go in the opposite direction 
if self.rect.top < 150: #checking if its too close to the top
  self.y_speed = 5 #changing speed in opposite direction
```
The more you make the margin number (150 in this case) the shallower it will jump, the smaller you make it the higher it will jump!

AND WE'RE DONE! That's the end of jumping-alien.py :rocket:
*find my source code in the Project 1 folder*

