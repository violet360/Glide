import socket
from _thread import *
from player import Player
import pickle
from peg import Peg

# class peg():


server = socket.gethostname()
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(2)
print("Waiting for a connections.............")

peg = Peg(25,50, 20, (0,255,0))
players = [Player(0,0, 40, (255,0,0)), Player(0,0, 40,(0,0,255))]

def threaded_client(conn, player):
    global peg
    conn.send(pickle.dumps([players[player], peg]))
    reply = ""
    while True:
        try:
            data = pickle.loads(conn.recv(2048))
            players[player] = data[0]
            peg = data[1]

            if not data:
                print("Disconnected")
                break
            else:
                if player == 1:
                    reply = [players[0], peg]
                else:
                    reply = [players[1], peg]

                # for i in enumerate(players)
                

                print("Received: ", data)
                print("Sending : ", reply)

            conn.sendall(pickle.dumps(reply))
        except:
            break

    print("Lost connection")
    conn.close()

currentPlayer = 0
while True:
    conn, addr = s.accept()
    print("Connected to:", addr)

    # if(currentPlayer == 1):
    #     peg = Peg(50,50, 20, (0,255,0))



    start_new_thread(threaded_client, (conn, currentPlayer))
    currentPlayer += 1
