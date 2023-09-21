from flet import *


class Pixel(UserControl):
    def __init__(self,index,**kw):
        self.index=index
        super().__init__(**kw)
    def get_pixel(self ):
        return Container(
            padding=1,bgcolor= colors.BLUE_ACCENT if self.index in [4,14,24,34,35] else colors.WHITE24,
            border_radius=4,
            alignment=alignment.center,
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
class Board(UserControl):
    col_lenth=10
    row_lenth=15
    board_width=310
    def pixel(self,index):
        return Container(
            padding=1,bgcolor= colors.BLUE_ACCENT if index in [4,14,24,34,35] else colors.WHITE24,
            border_radius=4,
            alignment=alignment.center,
            content=Text(f'{index}',size=10,style=TextStyle()),
        )
    def build(self):
        return Column(
                controls=[
                Container(
                width=self.board_width,
                content=GridView(
                # col=10,
                runs_count=self.col_lenth,#Numero de colunas
                max_extent=30,#largura maxima de item da grade
                child_aspect_ratio=1.0,
                spacing=1,#spaçamento vertical
                run_spacing=1,#espaçamento horizontal
                controls=list(map(lambda index:Pixel(index).get_pixel(),range(0,self.col_lenth*self.row_lenth))),
                    )
                    ),
                    
            Container(
                width= self.board_width,
                
                height=40, alignment=alignment.center,
                content=Row(
                alignment=MainAxisAlignment.SPACE_BETWEEN,
                controls=[
                    IconButton(icon=icons.SWIPE_LEFT),
                    IconButton(icon=icons.SWIPE_DOWN),
                    IconButton(icon=icons.ROTATE_90_DEGREES_CCW_OUTLINED),
                    IconButton(icon=icons.SWIPE_RIGHT_ROUNDED),
            ]
                )
            ),        
            ]
        )

def main(page:Page):
    page.window_width=360
    page.window_height=600
    page.theme_mode=ThemeMode.DARK
    board=Board()


    page.add(board)

if __name__=="__main__":
    app(target=main)