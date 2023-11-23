 
import pyxel
import hero
import map
import body
class Game:
    def __init__(self):
        self.hero = hero.Hero(self, 75, 50)
        self.map = map.Map()
        self.bodies = [
            body.Body(30, 30, 160, 1),
        ]


        pyxel.init(160, 120, title="Portal da Escuridão")
        pyxel.load("my_resource.pyxres", image = True)
        pyxel.run(self.update, self.draw)



    def update(self):
        self.map.update()
        self.hero.update()
        if self.hero.position_x < 0:
            self.hero.position_x = 160
            self.map.x -= 1

        if self.hero.position_x > 160:
            self.hero.position_x = 0
            self.map.x += 1

        if self.hero.position_y < 0:
            self.hero.position_y = 120
            self.map.y -= 1


        if self.hero.position_y > 120:
            self.hero.position_y = 0
            self.map.y += 1

    def draw(self):
        pyxel.cls(0)
        
        self.map.draw()
        self.hero.draw()

Game()

