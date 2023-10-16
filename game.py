import sys

import pygame
import time

print(f"the quit event is type {pygame.QUIT}")
pygame.init()

screen = pygame.display.set_mode((400,400))
pygame.display.set_caption("chomp!!!")


screen.fill((100,53,255))
pygame.draw.rect(screen, (100, 25, 0), (0, 380, 400, 400))
sand = pygame.image.load("assets/images/sand.png").convert()
screen.blit(sand,(200,200,64,64))
pygame.display.flip()
while True:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            print ("Thanks for Playing ")
            pygame.quit()
            sys.exit()

