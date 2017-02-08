## Learning the Basics

All games run off something called a "*Game Loop*" which is comprised of three different components
* **Process Input / "events"**
  * i.e. mouse click or keyboard press
* **Update Game**
  * i.e. update character as it moves by input methods
* **Render**
  * basically - redrawing the game
  
### FPS
This is how many times per second does the game loop repeat.
* This has to be a happy medium, not too fast that it wont work on some computers and not too slow that it lags
* essentially how *fast* the game is

I also learned some really cool stuff about FPS. Basically, clock.tick keeps track of how long it took to run through the entire
game loop. If it was less time than whatever variable you decided on (let just say 30 fps or 1/30th of a second) then it will pause
until that time period is complete and then start again. This ensure the loop always happens at the same speed.

If it takes *more* than the variable you defined (more than 1/30th of a second) then you get the dreadded **LAG** :skull:

### Colour
Colour in Python/Pygame is defined by RGB values. It's good to this list these where you list the other variables so that you can constantly call upon them

On the topic of colour, constant redrawing for character movement really slows down your game.
To avoid this we use something called `*Double Buffering*`

### Double Buffering
Think of this like drawing on a two sided white board. You draw on the back where your audience can't see and when you're ready you *flip* the board when its finished
 Next time you're drawing, when youre finished you flip it again

This is used by the command 

```python
pygame.display.flip()
```

### Keeping Time
To keep time we use 
```python
clock.tick(fps)
```
its smart to define your variables beforehand so if you change how fast you want your FPS to be you dont have to look for all instances of it

### Initializing Game
To initialize the game use the following: ```python pygame.init()``` basically just makes a bunch of magic happen, will update my knowlegde about this in another day. For now: all I know is its *magic* :sparkles:

### What I coded today:




