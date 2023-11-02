 
import pyxel
import hero
import map
class Game:
    def __init__(self):
        self.hero = hero.Hero(75, 50)
        self.map = map.Map()


        pyxel.init(160, 120, title="Portal da Escuridão")
        pyxel.load("my_resource.pyxres", image = True)
        pyxel.run(self.update, self.draw)



    def update(self):
        self.map.update()
        self.hero.update()

    def draw(self):
        pyxel.cls(0)
        
        self.map.draw()
        self.hero.draw()

Game()

