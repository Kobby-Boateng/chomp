import sys
import pygame

# dimensions
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
SAND_HEIGHT = 20
TILE_SIZE = 64  # tile are square height == width

# colors
WATER_COLOR = (100, 53, 255)
SAND_COLOR = (100, 25, 0)
pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("chomp!!!")
screen.fill(WATER_COLOR)
pygame.draw.rect(screen, SAND_COLOR, (0,
                                      SCREEN_HEIGHT - SAND_HEIGHT,
                                      SCREEN_WIDTH,
                                      SAND_HEIGHT))
sand = pygame.image.load("assets/images/sand.png").convert()
screen.blit(sand, (SCREEN_WIDTH/2 - TILE_SIZE/2,
                   SCREEN_HEIGHT/2 - TILE_SIZE/2))
pygame.display.flip()
while True:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            print("Thanks for Playing ")
            pygame.quit()
            sys.exit()

        pygame.display.flip()
