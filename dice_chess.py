import pygame as py

board=[]
for i in range(8):
    b=[]
    for j in range(8):
        b.append(None)
    board.append(b)



class queen():
    def __init__(self,x,y,color):
        self.type="Q"
        self.x=x
        self.y=y
        self.color=color
    def possible_moves(self,board):
        temp_x=self.x+1
        temp_y=self.y+1

        moves=[]


        while temp_x  < 8:

            if board[temp_x][self.y] != None:

                if board[temp_x][self.y].color == self.color:
                    break
                else:
                    moves.append((temp_x, self.y))
                    break
            moves.append((temp_x,self.y))
            temp_x+=1

        while temp_y  < 8:
            if board[self.x][temp_y] != None:

                if board[self.x][temp_y].color == self.color:
                    break
                else:
                    moves.append((self.x, temp_y))
                    break
            moves.append((self.x, temp_y))
            temp_y += 1
        temp_x = self.x-1
        temp_y = self.y-1

        while temp_x  >= 0:
            if board[temp_x][self.y] != None:

                if board[temp_x][self.y] != None:

                    if board[temp_x][self.y].color == self.color:
                        break
                    else:
                        moves.append((temp_x, self.y))
                        break
            moves.append((temp_x,self.y))
            temp_x-=1

        while temp_y  >=0:
            if board[self.x][temp_y] != None:
                if board[self.x][temp_y].color == self.color:
                    break
                else:
                    moves.append((self.x, temp_y))
                    break

            moves.append((self.x, temp_y))
            temp_y -= 1



        ###################




        x_change = [-1,1]
        y_change = [-1,1]

        for xc in x_change:
            for yc in y_change:
                temp_x=self.x+ xc
                temp_y=self.y +yc
                while (0<=temp_x<8) and (0<=temp_y<8):
                    if board[temp_x][temp_y] != None:

                        if board[temp_x][temp_y].color == self.color:
                            break
                        else:
                            moves.append((temp_x, temp_y))
                            break


                    moves.append((temp_x,temp_y))
                    temp_x += xc
                    temp_y += yc

        return moves


    ##

    def draw_piece(self,win):
        if self.color == 1:
            piece_color=(0,0,0)
        else:
            piece_color=(255,255,255)
        font=py.font.Font("freesansbold.ttf",30)
        text=font.render(self.type,True,piece_color)
        return text

    ##

class rook():
    def __init__(self,x,y,color):
        self.type="R"
        self.x=x
        self.y=y
        self.color=color


    def possible_moves(self,board):
        temp_x = self.x + 1
        temp_y = self.y + 1

        moves = []

        while temp_x < 8:

            if board[temp_x][self.y] != None:

                if board[temp_x][self.y].color == self.color:
                    break
                else:
                    moves.append((temp_x, self.y))
                    break
            moves.append((temp_x, self.y))
            temp_x += 1

        while temp_y < 8:
            if board[self.x][temp_y] != None:

                if board[self.x][temp_y].color == self.color:
                    break
                else:
                    moves.append((self.x, temp_y))
                    break
            moves.append((self.x, temp_y))
            temp_y += 1
        temp_x = self.x - 1
        temp_y = self.y - 1

        while temp_x >= 0:
            if board[temp_x][self.y] != None:

                if board[temp_x][self.y] != None:

                    if board[temp_x][self.y].color == self.color:
                        break
                    else:
                        moves.append((temp_x, self.y))
                        break
            moves.append((temp_x, self.y))
            temp_x -= 1

        while temp_y >= 0:
            if board[self.x][temp_y] != None:
                if board[self.x][temp_y].color == self.color:
                    break
                else:
                    moves.append((self.x, temp_y))
                    break

            moves.append((self.x, temp_y))
            temp_y -= 1
        return moves
    def draw_piece(self,win):
        if self.color == 1:
            piece_color=(0,0,0)
        else:
            piece_color=(255,255,255)
        font=py.font.Font("freesansbold.ttf",30)
        text=font.render(self.type,True,piece_color)
        return text



class bishop():
    def __init__(self,x,y,color):
        self.type="B"
        self.x=x
        self.y=y
        self.color=color

    def possible_moves(self,board):
        x_change = [-1, 1]
        y_change = [-1, 1]
        moves=[]

        for xc in x_change:
            for yc in y_change:
                temp_x = self.x + xc
                temp_y = self.y + yc
                while (0 <= temp_x < 8) and (0 <= temp_y < 8):
                    if board[temp_x][temp_y] != None:
                        print((temp_x, temp_y))
                        if board[temp_x][temp_y].color == self.color:
                            break
                        else:
                            moves.append((temp_x, temp_y))
                            break

                    moves.append((temp_x, temp_y))
                    temp_x += xc
                    temp_y += yc

        return moves
    def draw_piece(self,win):
        if self.color == 1:
            piece_color=(0,0,0)
        else:
            piece_color=(255,255,255)
        font=py.font.Font("freesansbold.ttf",30)
        text=font.render(self.type,True,piece_color)
        return text



class king():
    def __init__(self,x,y,color):
        self.x=x
        self.y=y
        self.color=color
        self.type="K"
    def possible_moves(self,board):
        moves=[]

        diagonal=[-1,0,1]
        for dia_x in diagonal:
            for dia_y in diagonal:
                if (0<= self.x + dia_x < 8 ) and (0<= self.y + dia_y < 8):
                    if board[self.x + dia_x][self.y + dia_y] != None:

                        if (board[self.x + dia_x][self.y + dia_y].color == self.color):
                            continue
                    moves.append((self.x + dia_x ,self.y + dia_y))
        return moves
    def draw_piece(self,win):
        if self.color == 1:
            piece_color=(0,0,0)
        else:
            piece_color=(255,255,255)
        font=py.font.Font("freesansbold.ttf",30)
        text=font.render(self.type,True,piece_color)
        return text




class pawn():
    def __init__(self,x,y,color):
        self.x =x
        self.y =y
        self.color=color
        self.type = "P"
    def possible_moves(self,board):
        moves=[]
        if self.color == 1:
            if board[self.x + 1][self.y] == None:
                moves.append((self.x+1,self.y))
            if self.x == 1 and board[self.x + 2][self.y] == None:
                moves.append((self.x+2,self.y))
            for dia_y in [-1,1]:
                if 0<= self.y + dia_y < 8 and board[self.x + 1][self.y + dia_y] != None:
                    if board[self.x + 1][self.y + dia_y].color != self.color:
                        moves.append((self.x+1,self.y + dia_y))
        if self.color == 0:
            if board[self.x - 1][self.y] == None:
                moves.append((self.x-1,self.y))
            if self.x == 6 and board[self.x - 2][self.y] == None:
                moves.append((self.x-2,self.y))
            for dia_y in [-1,1]:
                if 0<= self.y + dia_y < 8 and board[self.x - 1][self.y + dia_y] != None:
                    if board[self.x - 1][self.y + dia_y].color != self.color:
                        moves.append((self.x-1,self.y + dia_y))
        return moves
    def draw_piece(self,win):
        if self.color == 1:
            piece_color=(0,0,0)
        else:
            piece_color=(255,255,255)
        font=py.font.Font("freesansbold.ttf",30)
        text=font.render(self.type,True,piece_color)
        return text




class knight():
    def __init__(self,x,y,color):
        self.x = x
        self.y = y
        self.color= color
        self.type ="N"
    def possible_moves(self,board):
        moves=[]
        kn=[-2,-1,1,2]
        for k in kn:
            for n in kn :
                if abs(k) == abs(n):
                    continue
                kn_x=self.x+k
                kn_y=self.y+n


                if 0 <= kn_x < 8 and 0 <= kn_y < 8:
                    if board[kn_x][kn_y] != None and board[kn_x][kn_y].color == self.color:
                        continue
                    moves.append((kn_x,kn_y))
        return moves
    def draw_piece(self,win):
        if self.color == 1:
            piece_color=(0,0,0)
        else:
            piece_color=(255,255,255)
        font=py.font.Font("freesansbold.ttf",30)
        text=font.render(self.type,True,piece_color)
        return text












