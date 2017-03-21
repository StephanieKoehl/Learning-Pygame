# Python Pygame skeleton for a new project

import pygame
import random
import os


WIDTH = 800
HEIGHT = 600
FPS = 30

#define a few useful colours
WHITE = (255,255,255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
MAGENTA = (255, 0, 255)

#where folders are
#set up assets (art and sound that goes into our game)

game_folder = os.path.dirname(__file__) #knows the name of the file itself
img_folder = os.path.join(game_folder,"img")


class Player(pygame.sprite.Sprite):
	#sprite for the player
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load(os.path.join(img_folder, "p1_jump.png")).convert()
		self.rect = self.image.get_rect()
		self.image.set_colorkey(BLACK)
		self.rect.center = (WIDTH / 2, HEIGHT / 2)
		self.y_speed = 5

	def update(self):
		self.rect.x += 5
		self.rect.y += self.y_speed
		if self.rect.bottom > HEIGHT - 150:
			self.y_speed = -5
		if self.rect.top < 150:
			self.y_speed = 5
		if self.rect.left > WIDTH:
			self.rect.right = 0

# initialize pygame and create window

pygame.init() # initializes game, gets it good2go
pygame.mixer.init() # handles sound effects and music in your game

screen = pygame.display.set_mode((WIDTH, HEIGHT)) #window
pygame.display.set_caption("My Swagilicious Game")
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

# Game loop
running = True #set to false when we want to stop our game

while running:
	#keep loop running at the right speed
	clock.tick(FPS)
	#process input (events)
	for event in pygame.event.get():
		#check for closing window
		if event.type == pygame.QUIT:
			running = False
	#update
	all_sprites.update()

	#draw/render
	screen.fill(BLACK) #fill screen with solid colour instead of having moving parts/sprites
	all_sprites.draw(screen)
	# *after* drawing everything, this happens last
	pygame.display.flip()

pygame.quit()
