import socket
import threading
import random
from player import *
import json

class Server:
    def __init__(self):
        self.createServer()
        self.players = []
        self.playerConnect = 0
        self.FORMAT = 'utf-8'
        self.DISCONNECT_MESSAGE = '!DISCONNECT'

    def createServer(self):
        self.PORT = random.randrange(4040, 600)
        self.SERVER = socket.gethostbyname(socket.gethostname())
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.ADDR = (self.SERVER, self.PORT)
        self.server.bind(self.ADDR)

    def handleClient(self, conn, addr):
        while True:
            msg = conn.recv(1024)
            if msg == self.DISCONNECT_MESSAGE:
                self.playerConnect -= 1
                self.players.remove(player for player in self.players if player.conn == conn)

            playerDict = json.dumps(player.__dict__ for player in self.players if player.conn == conn)
            conn.send(playerDict.encode(self.FORMAT))

    def start(self):
        self.server.listen()
        while True:
            conn, addr = self.server.accept()
            self.players.append(Player(conn, addr))
            thread = threading.Thread(target=self.handleClient, args=(conn, addr))
            thread.start()
            self.playerConnect += 1

class ServerHandler:
    pass
