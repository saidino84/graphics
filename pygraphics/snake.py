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
        self.direction=Direction.LEFT
    
class Snake:
    def __init__(self,color=(255,255,255)):
        self.color=color
        self.pos=[(200,150),(225,150),(235,150),(265,150),(285,150),(310,150)]
        self.size=(20,20)
        self.graphic=pygame.Surface(self.size)
        self.graphic.fill(self.color)
    def change_direction(self,direction:Direction=Direction.RIGHT):
        match direction:
            case Direction.LEFT:
                self.pos[0]=(self.pos[0][0]-self.size[0],self.pos[0][1])
                print('MOVE LEFT')
            case Direction.RIGHT:
                self.pos[0]=(self.pos[0][0]+self.size[0] ,self.pos[0][1])
                print('MOVE RIGHT')

            case Direction.UP:
                self.pos[0]=(self.pos[0][0] ,self.pos[0][1]-self.size[1])
                print('MOVE UP')

            case Direction.DOWN:
                self.pos[0]=(self.pos[0][0],self.pos[0][1]+self.size[1])
                print('MOVE DOWN')
                 
            case _:
                print('Not wolking')
class Game:
    def __init__(self,food:Food,snake:Snake,time=5, width:int=600,height:int=400):
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
                    self.direction=None
                    match(event.key):
                        case  pygame.K_DOWN:
                            self.direction=Direction.DOWN
                            print('DOWN')
                        case pygame.K_UP:
                            self.direction=Direction.UP
                            print('UP')

                        case pygame.K_LEFT:
                            self.direction=Direction.LEFT
                            print('LEFT')

                        case pygame.K_RIGHT:
                            self.direction=Direction.RIGHT
                            print('RIGHT')

                        case _:
                            print('UREGNOZIBLE KEY')
            self.snake.change_direction(direction=self.direction)
                    
            self.screen.blit(self.food.graphic,(25,25))
                        
            self.screen.fill((36,33,33))
           
            # drawing food
            # self.food.pos=(self.food.pos[0],self.food.pos[1]+1)
            ''' A LOGICA DE Desenhar as posicoes da cobra, vai ser:
            quando for apertado/acionado ex: Direction.UP
            so a primeiro valor da cobra é que vai ter que mudar de posicao,
            nesse caso se estava indo pra baixo e clicaste pra ir direita 
            para de decrementar o o eixo Y e passamos a mexer no eixo X, NESSE CASO:
            snake=[(200,100),(210,100)]
            snake[0][0]=eixo X da cabeca da cobra e snake[0][1] Y Da cabexa
            s
            A LOGICA PARA FAZER OUTRAS TUPLAS SEGUIREM COM O QUE A CABEÇA SEGUE, É DESENHARMOS 
            '''
            for index in range(len(self.snake.pos)-1,0,-1):
                self.snake.pos[index]=(self.snake.pos[index-1][0],self.snake.pos[index-1][1])
            
            # drawing snake CORDENATES
            for pos in self.snake.pos:
                self.screen.blit(self.snake.graphic,pos)
            
            self.screen.blit(self.food.graphic,(65,200)
                            #  self.food.pos
                             )
            
            pygame.display.update()
        
def main():
    width=600
    height=400
    food=Food(width=width,height=height)
    snake=Snake()
    game = Game(food=food,snake=snake)
main()
