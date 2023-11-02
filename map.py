import pyxel

class Map:
    def __init__(self):
        self.width = 10
        self.height = 7
        self.tiles = [
           [0, 0, 0, 0, 0, 0, 0, 0, 2, 2],
         [0, 0, 0, 0, 0, 0, 0, 0, 2, 2],
         [0, 0, 0, 1, 1, 0, 0, 0, 2, 2],
         [0, 0, 1, 1, 1, 0, 0, 0, 2, 2],
         [0, 0, 0, 1, 1, 0, 0, 0, 2, 2],
         [0, 0, 0, 0, 0, 0, 0, 0, 2, 2],
         [0, 0, 0, 0, 0, 0, 0, 0, 2, 2],
         ]

    def draw(self):
        y = 0

        for row in self.tiles:
            x = 0
            for tile in row:
                 pyxel.blt(x, y, 0, 16*tile, 64, 16, 16)
                 x += 16
            y += 16

    def update(self):
        pass