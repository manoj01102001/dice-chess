import pygame as py
import dice_chess
import random
from network import Network

"""

Placed this part of code in server file

qw = dice_chess.queen(7, 3, 0)
qb = dice_chess.queen(0, 3, 1)
kw = dice_chess.king(7, 4, 0)
kb = dice_chess.king(0, 4, 1)
rw1 = dice_chess.rook(7, 0, 0)
rw2 = dice_chess.rook(7, 7, 0)
rb1 = dice_chess.rook(0, 0, 1)
rb2 = dice_chess.rook(0, 7, 1)
bw1 = dice_chess.bishop(7, 2, 0)
bb1 = dice_chess.bishop(0, 2, 1)
bw2 = dice_chess.bishop(7, 5, 0)
bb2 = dice_chess.bishop(0, 5, 1)
nb1 = dice_chess.knight(0, 1, 1)
nw1 = dice_chess.knight(7, 1, 0)
nb2 = dice_chess.knight(0, 6, 1)
nw2 = dice_chess.knight(7, 6, 0)

avai_piece = [qw, qb, kw, kb, rw1, rw2, rb1, rb2, bw1, bw2, bb1, bb2, nb1, nb2, nw1, nw2] 

def create_pawn_structure():
    for rows in range(8):
        black_pawn = dice_chess.pawn(1, rows, 1)
        white_pawn = dice_chess.pawn(6, rows, 0)
        avai_piece.append(black_pawn)
        avai_piece.append(white_pawn)


create_pawn_structure()

"""

def createboard(avai_piece):
    chess_board = []
    for rows in range(8):
        row = []
        for colomns in range(8):
            row.append(None)
        chess_board.append(row)
    for piece in avai_piece:
        if piece.x == -1:
            continue
        chess_board[piece.x][piece.y] = piece

    return chess_board


py.init()
WIDTH = 480
win = py.display.set_mode((WIDTH, WIDTH))
py.display.set_caption("DICE CHESS")

length = WIDTH / 8


def display_board(win, board=[], moves_shower=[], moves_counter=0, dice=[]):
    length = WIDTH / 8
    win.fill((0, 255, 255))

    for i in range(8):
        for j in range(8):
            if (i + j) % 2 != 0:
                py.draw.rect(win, (0, 200, 0), (length * i, length * j, length, length))
    for piece in avai_piece:
        if piece.x == -1:
            continue
        text = piece.draw_piece(win)
        tuple = (piece.y * length, piece.x * length)
        win.blit(text, tuple)
    if len(moves_shower) > 0:
        for move in moves_shower:
            pos = (int((move[1] * length) + length / 2), int((move[0] * length) + length / 2))
            py.draw.circle(win, (0, 0, 255), pos, 5)

    if len(dice) > 0:
        for piece in avai_piece:
            if piece.x == -1:
                continue
            if (piece.color == moves_counter % 2) and (piece.type in dice):
                pos = ((int(piece.y * length) + length / 2), int((piece.x * length) + length / 2))
                py.draw.circle(win, (255, 255, 0), pos, 5)


    py.display.update()


###dice generator
def dice(no_of_dice):
    pieces_name = ["K", "Q", "B", "N", "R", "P"]
    output = []
    while len(output) < no_of_dice:
        face_of_dice = random.choice(pieces_name)
        output.append(face_of_dice)
    return output


#####
def skip_to_next_player(board, dcp, move_counter):
    for row in board:
        for sq in row:
            if sq == None:
                continue
            else:
                if sq.color == move_counter % 2:
                    if sq.type in dcp:
                        if len(sq.possible_moves(board)) > 0:
                            return False
    return True


def promotion():
    promotion_sq = [0, 7]

    for piece in avai_piece:
        if piece.type != "P" or piece.x == -1 or piece.x not in promotion_sq:
            continue
        else:
            promotion_x = piece.x
            promotion_y = piece.y
            promoted_piece = random.choice(["Q", "R", "N", "B"])
            promoted_color = random.choice([0, 1, piece.color])

            if promoted_piece == "Q":
                avai_piece.append(dice_chess.queen(promotion_x, promotion_y, promoted_color))
            if promoted_piece == "R":
                avai_piece.append(dice_chess.rook(promotion_x, promotion_y, promoted_color))
            if promoted_piece == "B":
                avai_piece.append(dice_chess.bishop(promotion_x, promotion_y, promoted_color))
            if promoted_piece == "N":
                avai_piece.append(dice_chess.knight(promotion_x, promotion_y, promoted_color))
            piece.x = -1


####
run = True
move_shower = []
move_counter = 0
dice_choosen_pieces = []
no_to_colour = {0: "white", 1: "black"}
n = Network()
avai_piece = n.getpos()

n.send(avai_piece)

while run:


    chess_board = createboard(avai_piece)
    display_board(win, avai_piece, move_shower, move_counter, dice_choosen_pieces)
    promotion()
    if avai_piece[2].x == -1 or avai_piece[3].x == -1:
        font = py.font.Font("freesansbold.ttf", 30)
        text = font.render("GAME OVER", True, (255, 0, 0))
        win.blit(text, (300, 300))
        py.display.update()
        for event in py.event.get():
            if event.type == py.QUIT:
                run = False
        continue

    for event in py.event.get():
        ###rolling of dice
        if event.type == py.KEYDOWN:
            if event.key == py.K_SPACE:
                if len(dice_choosen_pieces) > 0:
                    continue
                dice_choosen_pieces = dice(3)

                if skip_to_next_player(chess_board, dice_choosen_pieces, move_counter):
                    print("no possible moves")
                    move_counter += 1
                    dice_choosen_pieces = []

        if event.type == py.QUIT:
            run = False

        if py.mouse.get_pressed()[0]:
            if len(dice_choosen_pieces) == 0:
                continue
            pos = py.mouse.get_pos(0)
            square = (int(pos[1] // length), int(pos[0] // length))

            if square in move_shower:
                if chess_board[square[0]][square[1]] != None:
                    chess_board[square[0]][square[1]].x = -1
                if selected_piece.type == "R":
                    selected_piece.castling = False

                if selected_piece.type == "K":
                    if square not in selected_piece.possible_moves_without_casting(chess_board):
                        print("casting")
                        castle_rooks = selected_piece.castle(chess_board)
                        for castle_rook in castle_rooks:
                            if square[1] == 6:
                                if castle_rook.y == 7:
                                    castle_rook.y = 5
                                    selected_piece.castling = False
                            else:
                                if castle_rook.y == 0:
                                    castle_rook.y = 3
                                    selected_piece.castling = False

                    selected_piece.castling = False

                selected_piece.x = square[0]
                selected_piece.y = square[1]

                move_shower = []
                move_counter += 1
                dice_choosen_pieces = []

            if chess_board[square[0]][square[1]] != None:
                if chess_board[square[0]][square[1]].color != move_counter % 2:
                    continue
                if chess_board[square[0]][square[1]].type in dice_choosen_pieces:
                    selected_piece = chess_board[square[0]][square[1]]
                    move_shower = selected_piece.possible_moves(chess_board)

    n.send(avai_piece)
