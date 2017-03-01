##Back up on it

Today I'm back to learning Pygame, I've gone on a lot of weird subpaths and been a bit distracted but I've got the motivation back and I'm doing it.
Are you proud? I'm proud. :cookie:

### Graphics
So at this point, having graphics for our games is important, more than just moving a square across a screen. Using [Open Game Art](http://opengameart.org/)

To load it into our program, we need to tell the program where it is. First importing os at the beginning of our program using the command ` import os`. Easy. Now we're going to set up our asset folder (assets in games are images and sounds) so we can later access it.

```python
game_folder = os.path.dirname(__file__)
```

Here we're making a variable called game_folder and using the os command (remember we imported the os library) and finding the path of the current file we're in. ` __file__ ` is a special variable python recognizes. Next we're going to define the image folder like this: `img_folder = os.path.join(game_folder, "img")` path.join joins two paths together. Here I'm joining the current file I'm editing with a folder called img which I already made in the directory my game file is in. This is to hold all the images i want in my game (sprites, backgrounds, etc.).

This is a little tricky, but now we know that our program will run on any computer we use.

Now lets implement a graphical sprite. We're going to change our previous code (the rectangle) to a sprite. So lets get rid of `self.image = pygame.Surface((50,50))` to `self.image = pygame.image.load(os.path.join(img_folder, "p1_jump.png")).convert()`.

Lets break down what this does:

`pygame.image.load` this part loads the image we want

`load(os.path.join(img_folder, "p1_jump.png"))` this part takes the previous folder we just defined (the folder we're putting all our images in) and joins it with that path.join command we just learned to include the image we actually want called p1_jump.png. So if you had a picture of a dog called dog.png you would just change the command to `(os.path.join(img_folder, "dog.png"))`. 

`convert()` this is a good easy way to speed up your game. Convert just turns the png format your importing into a file format python can readily use. :fire:

Next make sure to get rid of `self.image.fill(MAGENTA)` or else you'll just have a larger magenta square running across the screen

The computer loads every image as a rectangle which is awesome and works great except it0

```python

WIDTH = 800
HEIGHT = 600

