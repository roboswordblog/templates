class Player:
    def __init__(self, conn, addr):
        self.conn = conn
        self.addr = addr
        self.x = 0
        self.y = 0
        self.health = 100
        self.username = ""
        self.deltaY = 0
        self.deltaX = 0

    def update(self):
        pass
