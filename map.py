import pyxel

class Map:
    def __init__(self):
        self.width = 10
        self.height = 7
        self.x = 0
        self.y = 0
        self.maps = [
            [INTRODUCTION, SANDPLACE ],
            [FLOREST_1, FLOREST_2 ]
        ]
        INTRODUCTION = [
            [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
            [2, 0, 0, 0, 0, 0, 0, 0, 0, 2],
            [2, 0, 0, 1, 1, 0, 0, 0, 0, 2],
            [2, 0, 1, 1, 1, 0, 0, 0, 0, 0],
            [2, 0, 0, 1, 1, 0, 0, 0, 0, 2],
            [2, 0, 0, 0, 0, 0, 0, 0, 0, 2],
            [2, 0, 0, 0, 0, 0, 0, 0, 0, 2],
            [2, 2, 2, 2, 2, 0, 2, 2, 2, 2], 
        ]

        SANDPLACE= [
            [2, 2, 2, 2, 2, 2, 2, 2, 2, 2], 
            [2, 1, 1, 1, 1, 1, 1, 1, 1, 2],
            [2, 1, 1, 1, 1, 1, 1, 1, 1, 2],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
            [2, 1, 1, 1, 1, 1, 1, 1, 1, 2],
            [2, 1, 1, 1, 1, 1, 1, 1, 1, 2],
            [2, 1, 1, 1, 1, 1, 1, 1, 1, 2],
            [2, 2, 2, 2, 2, 0, 2, 2, 2, 2], 
        ]

        FLOREST_1 = [
            [2, 2, 2, 2, 2, 0, 2, 2, 2, 2],
            [2, 0, 0, 0, 0, 0, 0, 0, 0, 2],
            [2, 0, 0, 0, 0, 0, 0, 0, 0, 2],
            [2, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [2, 0, 0, 0, 0, 0, 0, 0, 0, 2],
            [2, 0, 0, 0, 0, 0, 0, 0, 0, 2],
            [2, 0, 0, 0, 0, 0, 0, 0, 0, 2],
            [2, 2, 2, 2, 2, 2, 2, 2, 2, 2], 
        ]

        FLOREST_2 = [
            [2, 2, 2, 2, 2, 0, 2, 2, 2, 2],
            [2, 0, 0, 0, 0, 0, 0, 0, 0, 2],
            [2, 0, 0, 0, 0, 0, 0, 0, 0, 2],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
            [2, 0, 0, 0, 0, 0, 0, 0, 0, 2],
            [2, 0, 0, 0, 0, 0, 0, 0, 0, 2],
            [2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
        ]

       

    def draw(self):
        y = 0

        for row in self.maps[self.y][self.x]:
            x = 0
            for tile in row:
                 pyxel.blt(x, y, 0, 16*tile, 64, 16, 16)
                 x += 16
            y += 16

    def update(self):
        pass



