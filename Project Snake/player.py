import pygame.time


class Player:

	def __init__(self, grid):
		self.grid = grid
		self.grid_rows = len(grid)
		self.grid_cols = len(grid[0])
		self.body = list()
		# place player in center of the screen
		center_row = self.grid_rows // 2
		center_col = self.grid_cols // 2
		self.body.append([center_row, center_col])
		# configure player attributes
		self.size = 5
		self.direction = 1		# 0 = up, 1 = right, 2 = down, 3 = left
		self.timer = pygame.time.get_ticks()
		self.move_delay = 200
		# direction queueing system
		self.queue_direction = None

	def set_direction(self, direction):
		# do not allow the snake to move backwards onto itself
		if abs(direction - self.direction) != 2:
			self.queue_direction = direction
		else:
			self.queue_direction = None

	def update(self):
		elapsed = pygame.time.get_ticks() - self.timer
		if elapsed >= self.move_delay:
			# reset timer
			self.timer = pygame.time.get_ticks()

			# if a direction change is queued, apply it now
			if self.queue_direction is not None:
				self.direction = self.queue_direction
				self.queue_direction = None

			# fetch the current head for convenience
			head = self.body[0]

			# calculate row and column offsets based on the direction
			if self.direction % 2 == 0:     # up and down
				r_offset = self.direction - 1
				c_offset = 0
			else:                           # left and right
				r_offset = 0
				c_offset = -1 * (self.direction - 2)        # go ahead and work this out by hand to prove it's correct

			# create the new head cell and insert it into the body list
			new_head = [(head[0] + r_offset) % self.grid_rows, (head[1] + c_offset) % self.grid_cols]
			self.body.insert(0, new_head)

			# detect if the player has run into itself
			if self.grid[new_head[0]][new_head[1]] == 1:
				return False

			# detect if the player is consuming an apple
			if self.grid[new_head[0]][new_head[1]] == 2:
				self.size += 1

			# remove all cells that are now farther back than the snake's size, and clear those grid cells
			while len(self.body) > self.size:
				cell = self.body[-1]
				self.grid[cell[0]][cell[1]] = 0
				index = len(self.body) - 1
				self.body = self.body[0:index]

			# update the grid at the new head spot
			self.grid[new_head[0]][new_head[1]] = 1

			return True

		else:
			return True

