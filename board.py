import pygame as py
WIDTH=640
win=py.display.set_mode((WIDTH,WIDTH))
py.display.set_caption("DICE CHESS")
def display_board(win,board=[]):
    length=WIDTH/8
    win.fill((255,255,255))

    for i in range(8):
        for j in range(8):
            if (i+j) % 2 != 0:
                py.draw.rect(win,(0,200,0),(length*i, length*j, length,length))
    py.display.update()


run=True
while run:
    display_board(win)

    for event in py.event.get():

        if event.type == py.QUIT:
            run =False

