import pygame as py
import dice_chess

qw=dice_chess.queen(7,3,0)
qb=dice_chess.queen(0,3,1)
kw=dice_chess.king(7,4,0)
kb=dice_chess.king(0,4,1)
rw1=dice_chess.rook(7,0,0)
rw2=dice_chess.rook(7,7,0)
rb1=dice_chess.rook(0,0,1)
rb2=dice_chess.rook(0,7,1)
bw1=dice_chess.bishop(7,2,0)
nb1=dice_chess.knight(0,1,1)


avai_piece=[qw,qb,kw,kb,rw1,rw2,rb1,rb2,bw1,nb1]


def createboard(avai_piece):
    chess_board = []
    for rows in range(8):
        row = []
        for colomns in range(8):
            row.append(None)
        chess_board.append(row)
    for piece in avai_piece:
        chess_board[piece.x][piece.y] = piece
    return chess_board



py.init()
WIDTH=640
win=py.display.set_mode((WIDTH,WIDTH))
py.display.set_caption("DICE CHESS")

length=WIDTH/8






def display_board(win,board=[],moves_shower=[]):
    length=WIDTH/8
    win.fill((0,255,255))

    for i in range(8):
        for j in range(8):
            if (i+j) % 2 != 0:
                py.draw.rect(win,(0,200,0),(length*i, length*j, length,length))
    for piece in avai_piece:
        text=piece.draw_piece(win)
        tuple=(piece.y * 80 + 40 , piece.x * 80 +40 )
        win.blit(text,tuple)
    if len(moves_shower) > 0:
        for move in moves_shower:
            pos=(int((move[1]*length)+length/2),int((move[0]*length)+length/2))
            py.draw.circle(win,(0,0,255),pos,5)
    py.display.update()


run=True
move_shower=[]
while run:
    chess_board=createboard(avai_piece)
    display_board(win,avai_piece,move_shower)

    for event in py.event.get():

        if event.type == py.QUIT:
            run =False
        if  py.mouse.get_pressed()[0]:
            pos=py.mouse.get_pos(0)
            square=(int(pos[1]//length),int(pos[0]//length))



            if chess_board[square[0]][square[1]] != None:
                selected_piece=chess_board[square[0]][square[1]]
                move_shower=selected_piece.possible_moves(chess_board)

            if square in move_shower:
                selected_piece.x=square[0]
                selected_piece.y=square[1]
                move_shower=[]



