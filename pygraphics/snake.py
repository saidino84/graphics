import pygame
from pygame.locals import *
from random import randint 

pygame.init()
height=400
width=600
LEFT=4
RIGHT=6
UP=8
DOWN=2
SPEED_UP=5

screen=pygame.display.set_mode((width,height))
pygame.display.set_caption("snake")

snake_pos=[(200,200),(210,200),(220,200)]
snake_skin=pygame.Surface((10,10))
snake_skin.fill((255,255,255))

food_pos=(randint(0,width),randint(0,590))
food=pygame.Surface((10,10))
food.fill((255,15,15))

direction=LEFT


fps=pygame.time.Clock()
def start_rolling():
    while True:
        fps.tick(20)
        for event in pygame.event.get():
            if event.type ==pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_RIGHT or pygame.K_6:
                    print('RIGHT')
                    direction=RIGHT
                if event.key==pygame.K_LEFT or pygame.K_4:
                    print('LEFT')
                    direction=LEFT
                if event.key==pygame.K_UP or pygame.K_8:
                    print('UP')
                    direction=UP
                if event.key==pygame.K_DOWN or pygame.K_2:
                    print('DOWN')
                    direction=DOWN
        for pos in range(len(snake_pos)-1,0,-1):
            snake_pos[pos]=(snake_pos[pos-1][0],snake_pos[pos-1][1])
        screen.fill((0,0,0))
        screen.blit(food,food_pos)
        for pos in snake_pos:
            screen.blit(snake_skin,pos)
        pygame.display.update()

# if __name__=="__main__":
start_rolling()

