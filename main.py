import ludo
import pygame as pg

width,height=400,400
window = pg.display.set_mode((width,height))

def update():
    pg.display.update()
    window.fill("black")
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            return False
        if event.type == pg.KEYDOWN:
            if pg.event.key==pg.k_ESCAPE:
                pg.quit()
                return False
    return True
def idToCol(v):
    if v==0:return "red"
    elif v==1:return "blue"
    elif v==2:return "green"
    return "yellow"
def draw_board():
    pg.draw.rect(window,"red",[0,0,150,150])
    pg.draw.rect(window,"blue",[400-150,0,150,150])
    pg.draw.rect(window,"green",[0,400-150,150,150])
    pg.draw.rect(window,"yellow",[400-150,400-150,150,150])
    pg.draw.rect(window, "white",[150,150,100,100])

    pg.draw.rect(window, "blue",[150+33,0,33,150])
    pg.draw.rect(window, "green",[150+33,150+100,33,150])
    pg.draw.rect(window, "red",[0,150+33,150,33])
    pg.draw.rect(window, "yellow",[150+100,150+33,150,33])

    [pg.draw.line(window, "white", (150,25*i),(150+100,25*i)) for i in range(1,6)]
    [pg.draw.line(window, "white", (150,150+100+(25*i)),(150+100,150+100+(25*i))) for i in range(1,6)]
    [pg.draw.line(window, "white", (25*i,150+100), (25*i,150)) for i in range(1,6)]  
    [pg.draw.line(window, "white", (150+100+(25*i),150+100), (150+100+(25*i),150)) for i in range(1,6)]

    for dx in [0,150+100]:
        for dy in [0,150+100]:
            pg.draw.circle(window, "white", (dx+(150/3),dy+(150/3)),20)  
            pg.draw.circle(window, "white", (dx+(2*(150/3)),dy+(150/3)),20)  
            pg.draw.circle(window, "white", (dx+(150/3),dy+(2*(150/3))),20)  
            pg.draw.circle(window, "white", (dx+(2*(150/3)),dy+(2*(150/3))),20)
    
            pg.draw.circle(window, "grey", (dx+(150/3),dy+(150/3)),15)  
            pg.draw.circle(window, "grey", (dx+(2*(150/3)),dy+(150/3)),15)  
            pg.draw.circle(window, "grey", (dx+(150/3),dy+(2*(150/3))),15)  
            pg.draw.circle(window, "grey", (dx+(2*(150/3)),dy+(2*(150/3))),15)

    pg.draw.polygon(window,"blue",[(width/2,height/2),(150,150),(150+100,150)])
    pg.draw.polygon(window,"red",[(width/2,height/2),(150,150),(150,150+100)])
    pg.draw.polygon(window,"green",[(width/2,height/2),(150+100,150+100),(150,150+100)])
    pg.draw.polygon(window,"yellow",[(width/2,height/2),(150+100,150+100),(150+100,150)])
def draw_player(player):
    for pice in player.pices:
        if pice.is_at_home:draw_home_pice(pice)
def draw_home_pice(pice):
    dx,dy=idToOffSet(pice.col)
    if pice.identity==0:pg.draw.circle(window, idToCol(pice.col), (dx+(150/3),dy+(150/3)), 10)
    if pice.identity==1:pg.draw.circle(window, idToCol(pice.col), (dx+(2*(150/3)),dy+((150/3))), 10)
    if pice.identity==2:pg.draw.circle(window, idToCol(pice.col), (dx+(2*(150/3)),dy+(2*(150/3))), 10)
    if pice.identity==3:pg.draw.circle(window, idToCol(pice.col), (dx+((150/3)),dy+(2*(150/3))), 10)
def idToOffSet(n):
    if n==0:return 0,0
    elif n==1:return 150+100,0
    elif n==2:return 0,150+100
    elif n==3:return 150+100,150+100
def draw_running_cell(cells):
    for i,cell in enumerate(cells):
        if 0<i<6:draw_pice(cell,25+12+(25*i),150+16)
def draw_pice(cell,x,y):
    if len(cell)==1:
        pg.draw.circle(window,idToCol(cell[0].col),(x,y),10)
def draw_home_cell(cell):pass
def draw_home_mat_cell(cell):pass


board = ludo.Board()

while update():
    draw_board()
    # for player in board.players:
    #     draw_player(player)
    # draw_running_cell(board.grid[:53])
    # draw_home_cell(board.grid[53:70])
    # draw_home_mat_cell(board.grid[70:91])

