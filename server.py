import socket
import pickle
import dice_chess
from _thread import *

# Server ip address in server add the ip address of the server
server = socket.gethostname()
PORT = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, PORT))

except socket.error as e:
    print(e)

s.listen(2)

print("Server Started \n Waiting for connection...")

# Sending initial positions of game pieces

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


def threadfun(conn, avai_piece):

    conn.send(pickle.dumps(avai_piece))

    while True:

        try:
            data = pickle.loads(conn.recv(2048))
            avai_piece = data

            if not data:
                print("Disconnected...")
                break

            else:
                print("Received: ", avai_piece)
                print("Sending: ", avai_piece)

            conn.sendall(pickle.dumps(avai_piece))
            print("Count: ", count)


        except:

            break
    print("Connection Lost ")
    conn.close()

count = 0

while True:

    conn, addr = s.accept()
    print(f"Connection Success ! \n Connected to : ", addr)

    start_new_thread(threadfun, (conn, avai_piece))
    count += 1
