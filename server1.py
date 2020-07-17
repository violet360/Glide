import socket
from _thread import *
# from player import Player
from participant import *
import pickle
import math
# from peg import Peg


def if_hit(player,peg):

    try:
        distance = math.sqrt((player.get_position()[0]-peg.get_position()[0])**2+(player.get_position()[1]-peg.get_position()[1])**2)
        
        if distance - 5 <= striker_radius+peg_radius:
            return calculate_velocity(player,peg)
        else: return False
        
    except Exception as e:
        print(e)
        return False
        pass

def calculate_velocity(player,peg):
    a = peg.position[0]-player.position[0]
    b = peg.position[1]- player.position[1]
    d = peg.position[0]-player.position[0]+peg.position[1]- player.position[1]
    return int (a)//3, int (b)//3


server = socket.gethostname()
port = 5555
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.bind((server, port))
except socket.error as e:
    str(e)
s.listen(2)
print("Waiting for a connections.............")


size           = width, height = 1100,650
striker_radius = height//15
peg_radius     = int(striker_radius//1.5)


player1 = Striker((255, 0, 0),(0, 255, 0),striker_radius,90,30)
player2 = Striker((255, 0, 0),(0, 255, 0),striker_radius,90,30)
peg = pegs((255, 255, 255),(0, 0, 255),peg_radius,500,325)


# peg = Pegs(25,50, 20, (0,255,0)) #peg object
players = [player1, player2] #[player1, player2]

def threaded_client(conn, player):
    global peg
    print(conn)
    try:
        conn.send(pickle.dumps([players[player], peg])) # sends [respectve_player, peg] to the respctive player 
    except conn.error as e:
        print(e)
    reply = ""
    while True:
        try:
            data = pickle.loads(conn.recv(2048)) #receives [respective_player, peg]
            players[player] = data

            hit = if_hit(players[player] , peg)
            # print("88888888888888")
            if hit is not False:
                # print()
                print(hit)
                peg.vx, peg.vy = hit

            peg.move()
            # players[player].move()

            if not data:
                print("Disconnected")
                break
            else:
                if player == 1:
                    reply = [players[0], peg]
                else:
                    reply = [players[1], peg]

                print("Received: ", data)
                print("Sending : ", reply) #if the "data" variable is received from player1 then "reply" will be [player2, peg],.............. else it will be [player1, peg]

            conn.sendall(pickle.dumps(reply)) 
        except:
            break

    print("Lost connection")
    conn.close()

currentPlayer = 0
while True:
    conn, addr = s.accept()
    print("Connected to:", addr)
    start_new_thread(threaded_client, (conn, currentPlayer)) #start a new_thread
    currentPlayer += 1
