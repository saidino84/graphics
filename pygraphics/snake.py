import pygame
from pygame.locals import *
from random import randint 

pygame.init()

from enum import Enum
class Direction(Enum):
    UP=8
    DOWN=2
    LEFT=4
    RIGHT=6

class Food:
    def __init__(self,width:int,height:int ,color=(255,0,0)):
        self.color=color
        self.size=(20,20)
        self.pos=(randint(20,width), randint(50,height))
        self.graphic=pygame.Surface(self.size)
        self.graphic.fill(self.color)
class Snake:
    def __init__(self,color=(255,255,255)):
        self.color=color
        self.pos=[(200,150),(210,150),(220,150)]
        self.size=(10,10)
        self.graphic=pygame.Surface(self.size)
class Game:
    def __init__(self,food:Food,snake:Snake,time=20, width:int=600,height:int=400):
        self.height=height
        self.width=height
        self.screen=pygame.display.set_mode((self.width,self.height))
        self.snake=snake
        self.food=food
        self.is_running=True
        self.time=time
        self.fps=pygame.time.Clock()
        self.direction=Direction.UP

        self.start()
    def start(self):
        while self.is_running:
            self.fps.tick(self.time)
            for event in pygame.event.get():
                if event.type == QUIT:
                    quit()
            
                if event.type ==KEYDOWN:
                    print("Going Down ...")
            self.screen.blit(self.food.graphic,(25,25))
                        
            self.screen.fill((36,33,33))
            # self.screen.fill((0,0,0))
            self.screen.blit(self.food.graphic,self.food.pos)
            # pygame.display.flip()
            self.food.pos=(self.food.pos[0],self.food.pos[1]+1)
            pygame.display.update()
        
def main():
    width=600
    height=400
    food=Food(width=width,height=height)
    snake=Snake()
    game = Game(food=food,snake=snake)
main()
