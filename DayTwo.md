### Sprites

Game development term that means an object on the screen that can move around. If you have a bunch of sprites on the screen the update section of the game loop gets really messy, and it will cause your game to lag
To update all your sprites at once we can make it into a group by using ``` all_sprites = pygame.sprite.Group ```. Then when we need to update the movement of these sprites we can do it all at once with ``` all_sprites.update() ``` in the draw section
we can also do something similar with ```all_sprites.draw(screen)``` which just makes all sprites in the group draw at once instead of asking each one to draw individually. Super speedy :runner:

As long as we remember to put sprites into the group, we dont have to worry about changing our draw and update code!

### Updated Template

```python

```

### Making a sprite

```python

class Player(pygame.sprite.Sprite): #using pygame library built in basic sprite setup
  def __init__(self): #code that will run whenever a new object is made. First thing that happens
    pygame.sprite.Sprite.__init__(self) #messy line that just makes the sprite initialize // happen
    
    # every sprite must have self.image and self.rect
    #self.image = what the sprite looks like
    #self.rect = rectangle that encloses the sprite **super important for it to be self aware (know when it bumps into things or how movement works)
    
    self.image = pygame.Surface((50,50)) #something you can draw on in pygame
    self.image.fill(WHITE) #remember we already defined colours, so now it will just be a 50x50 white square on our screen
    self.rect = self.image.get_rect() #looks at the image and determines the rectangle around it
    self.rect.center = (WIDTH / 2, HEIGHT /2) #have the sprite start in the center of the screen
    
```

Then all we have to do is add the sprite to the sprite group

```python

player = Player()
all_sprites.add(player)

```
