import sys
import pygame
import random
from settings import *

pygame.init()

game_font = pygame.font.Font("assets/fonts/Black_Crayon.ttf", 69)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("chomp!!!")
screen.fill(WATER_COLOR)
pygame.draw.rect(screen, SAND_COLOR, (0,
                                      SCREEN_HEIGHT - SAND_HEIGHT,
                                      SCREEN_WIDTH,
                                      SAND_HEIGHT))
sand = pygame.image.load("assets/images/sand.png").convert()
for i in range(SCREEN_WIDTH // TILE_SIZE):
    print(i)
    screen.blit(sand, (i * TILE_SIZE,
                       SCREEN_HEIGHT - TILE_SIZE))
# bit sand tiles across the bottom of the screen

sand_top = pygame.image.load("assets/images/sand_top.png").convert()
sand_top.set_colorkey((0, 0, 0))
for i in range(SCREEN_WIDTH // TILE_SIZE):
    print(i)
    screen.blit(sand_top, (i * TILE_SIZE,
                           SCREEN_HEIGHT - 2 * TILE_SIZE))

# randomly place 4 pieces of grass along the bottom of the screen
SEAGRASS = pygame.image.load("Assets/images/seagrass.png").convert()
SEAGRASS.set_colorkey((0, 0, 0))
for i in range(4):
    x = random.randint(0, SCREEN_WIDTH)
    # offset the seaweed so it looks better
    y = random.randint(SCREEN_HEIGHT - 2 * TILE_SIZE, SCREEN_HEIGHT) - int(.5 * TILE_SIZE)
    screen.blit(SEAGRASS, (x, y))
# draw the CHOMP! title
text = game_font.render("Chomp!",True, (255,69,0))

screen.blit(text, (SCREEN_WIDTH//2 - text.get_width()//2,SCREEN_HEIGHT//2 - text.get_height()//2))

pygame.display.flip()
while True:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            print("Thanks for Playing ")
            pygame.quit()
            sys.exit()

        pygame.display.flip()
