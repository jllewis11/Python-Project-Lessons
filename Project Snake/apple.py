import pygame
import random


class Apple:

	def __init__(self, grid):
		self.grid = grid
		self.grid_rows = len(grid)
		self.grid_cols = len(grid[0])
		# location where the apple is stored
		self.apple = None
		self.generate_apple()
		# timer for spawning apples
		self.timer = -1

	def generate_apple(self):
		while True:
			row = random.randint(0, self.grid_rows-1)
			col = random.randint(0, self.grid_cols-1)
			if self.grid[row][col] == 0:
				self.apple = (row, col)
				self.grid[row][col] = 2
				break

	def apple_removed(self):
		return self.grid[self.apple[0]][self.apple[1]] != 2

	def update(self):
		if self.apple_removed():
			if self.timer == -1:
				# apple has been removed since last frame
				self.timer = pygame.time.get_ticks()
			else:
				# apple was removed previously, count down
				elapsed = pygame.time.get_ticks() - self.timer
				if elapsed >= 3000:
					self.generate_apple()
					self.timer = -1

