import pygame
from sys import exit
import os
from random import choice

pygame.init()
pygame.display.set_caption("Rock, paper, scissors")
clock = pygame.time.Clock()

width = 800
height = 400
screen = pygame.display.set_mode((width,height))

font = pygame.font.SysFont('verdana', 20)
text = font.render('Press 1, 2, 3 (left side) and 7, 8, 9 (right side)', True,("Black"))
textRect = text.get_rect()
textRect.center = (width//2,30)


scissors_surface = pygame.image.load(os.path.join("kaarid.png"))
paper_surface = pygame.image.load(os.path.join("paber.png"))
rock_surface = pygame.image.load(os.path.join("kivi.png"))

left = 5
right = 4

while True:
    screen.fill("White")
    screen.blit(text,textRect)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            #left
            if event.key == pygame.K_1:
                left = 0
            if event.key == pygame.K_2:
                left = 1
            if event.key == pygame.K_3:
                left = 2
            #right
            if event.key == pygame.K_7:
                right = 0
            if event.key == pygame.K_8:
                right = 1
            if event.key == pygame.K_9:
                right = 2
    #left
    if left == 0:
        screen.blit(rock_surface,(50,100))
    elif left == 1:
        screen.blit(paper_surface,(50,50))
    elif left == 2:
        screen.blit(scissors_surface,(50,100))
    #right
    if right == 0:
        screen.blit(rock_surface,(450,100))
    elif right == 1:
        screen.blit(paper_surface,(450,50))
    elif right == 2:
        screen.blit(scissors_surface,(450,100))

    pygame.display.update()
    clock.tick(60)