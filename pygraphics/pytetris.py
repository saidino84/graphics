import enum
from functools import reduce
from flet import *

class TetrominoType(enum.Enum):
    L='L',#=[4,14,24,34,35],
    S='S',#=[5,4,3,13,23,33,34,35],
    Z='Z',#=[3,4,5,14,23,24,25],
    O='O',#=[3,4,14,13],
    I='I',#=[3,4,5,14,24,34,33,35],
    J='J',#=[3,4,5,14,24,34,33],
    T='T',#=[3,4,5,14,25,34],


class Piece:
    def __init__(self,type:TetrominoType):
        self.type=type
        self.positions=[]
    def initialize(self):
        match(self.type):
            case TetrominoType.L:
                self.positions=[4,14,24,34,35]
            case TetrominoType.S:
                self.positions=[5,4,3,13,23,24,25,35,45,44,43]
            case TetrominoType.Z:
                self.positions=[3,4,5,14,23,24,25]
    
class MoveDirection(enum.Enum):
    Left=0,
    Right=1,
    Down=2,
    Rotate=3,
    Drop=4,
class MoveType(enum.Enum):
    Move=0,
    HardDrop=1,
    SoftDrop=2,
class GameState(enum.Enum):
    Playing=0,
    Paused=1,
    GameOver=2,
class GameMode(enum.Enum):
    Classic=0,
    Hard=1,
    Harder=2,


class Board(UserControl):
    col_lenth=10
    row_lenth=15
    board_width=310
    currentPiece:Piece=Piece(type=TetrominoType.S)
    def pixel(self,index):
        return Container(
            padding=1,bgcolor= colors.BLUE_ACCENT if index in self.currentPiece.positions else colors.WHITE24,
            border_radius=4,
            alignment=alignment.center,
            content=Text(f'{index}',size=10,style=TextStyle()),
            
        )
    def build(self):
        self.currentPiece.initialize()
        self.list=list(map(lambda index:Pixel(index,color=colors.BLUE_ACCENT if index in self.currentPiece.positions else colors.WHITE24,).get_pixel(),range(0,self.col_lenth*self.row_lenth)))
        # self.currentPiece.positions=list(map(lambda index:index+self.col_lenth,self.currentPiece.positions))
        self.grid=GridView(
                # col=10,
                runs_count=self.col_lenth,#Numero de colunas
                max_extent=30,#largura maxima de item da grade
                child_aspect_ratio=1.0,
                spacing=1,#spaçamento vertical
                run_spacing=1,#espaçamento horizontal
                controls=self.list,
                    )
        return Column(
                controls=[
                Container(
                width=self.board_width,
                content=self.grid,
                    ),
                    
            Container(
                width= self.board_width,
                
                height=40, alignment=alignment.center,
                content=Row(
                alignment=MainAxisAlignment.SPACE_BETWEEN,
                controls=[
                    IconButton(icon=icons.SWIPE_LEFT),
                    IconButton(icon=icons.SWIPE_DOWN,on_click=self.moveDow),
                    IconButton(icon=icons.ROTATE_90_DEGREES_CCW_OUTLINED),
                    IconButton(icon=icons.SWIPE_RIGHT_ROUNDED),
            ]
                )
            ),     
            Container(height=40, alignment=alignment.center,bgcolor=colors.TEAL,
                      
                      on_long_press=self.on_long_press_handler,
                      )   
            ]
        )
    def moveDow(self,t):
        print(f" OLD LIST:{self.currentPiece.positions}")
        self.currentPiece.positions=list(map(lambda index:index+self.col_lenth,self.currentPiece.positions))
        print(f'NEW {self.currentPiece.positions}')
        print('Moving...')
        _lista=list(map(lambda index:Pixel(index,color=colors.BLUE_ACCENT if index in self.currentPiece.positions else colors.WHITE24,).get_pixel(),range(0,self.col_lenth*self.row_lenth)))
        self.grid.controls=_lista
        self.grid.update()
        self.page.update()
    def on_long_press_handler(self,x):
        # print(f'Moving.. {self.page.window.x},')
        # self.window.move_to(x.control.x,x.control.y)
        # print(f'{x.control}')
        print(f"{MouseCursor.CELL.value},")



class Pixel(UserControl):
    def __init__(self,index,color,**kw):
        self.index=index
        self.color=color
        super().__init__(**kw)
    def get_pixel(self ):
        return Container(
            padding=1,
            bgcolor=self.color,
            border_radius=4,
            alignment=alignment.center,
            border=border.all(color=colors.WHITE10 ,width=2) if self.color==colors.BLUE_ACCENT else None,
            content=Text(f'{self.index}',size=10,style=TextStyle()),
        )
    def build(self):
        if(self.index in [4,14,24,34,35]):
            return Container(
            padding=1,bgcolor=colors.AMBER,
            border_radius=4,
            # alignment=Alignment.center,
            content=Text(f'{self.index}'),
                            )
        return Container(
            padding=1,bgcolor=colors.AMBER,
            border_radius=4,
            # alignment=Alignment.center,
            content=Text(f'{self.index}'),
        )
    



 






def main(page:Page):
    page.window_width=360
    page.window_height=640
    page.theme_mode=ThemeMode.DARK
    page.window_always_on_top=True
    page.bgcolor=colors.TRANSPARENT
    page.window_resizable=False
    # page.window_title_bar_hidden=True
    # page.window_bgcolor=colors.TRANSPARENT
    page.window_center=True
    page.window_movable=False
    page.window_left=750
    # page.window_top=150

    # page.show_semantics_debugger=True
    board=Board()
    page.add(board)
    page.update()
if __name__=="__main__":
    app(target=main)

 