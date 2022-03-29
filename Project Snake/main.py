import pygame
from player import Player
from apple import Apple

pygame.init()

# create the screen
screen = pygame.display.set_mode((700, 700))
pygame.display.set_caption('Snake')

# calculate grid dimensions
cell_size = 25
grid_cols = screen.get_width() // cell_size
grid_rows = screen.get_height() // cell_size


# set up the grid
grid = list()
for i in range(grid_rows):
    grid.append([0] * grid_cols)

# set up colors to use
grid_colors = ((0, 165, 0), (20, 150, 0))
player_color = (0, 255, 0)
apple_color = (255, 0, 0)

# use a clock to control frame rate
clock = pygame.time.Clock()

# create a player snake
player = Player(grid)

# create an apple generator
apple = Apple(grid)

# use a flag to control the game loop
running = True
while running:
    # process all events each frame
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            break
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                player.set_direction(0)
            elif event.key == pygame.K_d:
                player.set_direction(1)
            elif event.key == pygame.K_s:
                player.set_direction(2)
            elif event.key == pygame.K_a:
                player.set_direction(3)

    # break the game loop early if a quit event has occurred
    if not running:
        break

    # run the game code
    if not player.update():
        running = False
        break

    apple.update()

    # draw the grid
    for r in range(grid_rows):
        color_offset = r % 2
        for c in range(grid_cols):

            color_index = (c % 2 + color_offset) % 2

            color = grid_colors[color_index]

            cell = grid[r][c]
            if cell == 1:
                color = player_color
            elif cell == 2:
                color = apple_color

            cell_rect = pygame.Rect(c * cell_size, r * cell_size, cell_size, cell_size)
            pygame.draw.rect(screen, color, cell_rect)

    # control the framerate and update the window
    clock.tick(60)
    pygame.display.flip()


pygame.quit()
