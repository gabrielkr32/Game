import pyxel
class Hero:
    def __init__(self, position_x, position_y):
        self.position_x = position_x
        self.position_y = position_y
        self.direction = 0
        self.running = False
        self.attacking = True
        self.frame = 0
        self.estamine = 1
          

    def draw(self):
            if self.running:
                if self.direction == 0:
                   pyxel.blt(self.position_x, self.position_y, 0, 16*int(self.frame), 48, 16, 15, pyxel.COLOR_BLACK)
                else:
                    pyxel.blt(self.position_x, self.position_y, 0, 16*int(self.frame), 32, 16, 15, pyxel.COLOR_BLACK)
            else:
                if self.attacking:
                    if self.direction == 0:
                       pyxel.blt(self.position_x, self.position_y, 0, 0, 16, 16, 15, pyxel.COLOR_BLACK)
                    else:
                         pyxel.blt(self.position_x, self.position_y, 0, 16, 16, 16, 15, pyxel.COLOR_BLACK)    
        

                else:
                    if self.direction == 0:
                       pyxel.blt(self.position_x, self.position_y, 0, 0, 0, 16, 16, pyxel.COLOR_BLACK)

                    
                       pyxel.blt(self.position_x, self.position_y, 0, 16, 0, 16, 16, pyxel.COLOR_BLACK)

            
                    


    def update(self):
        self.running = False
        self.attacking = False
       

        if pyxel.btn(pyxel.KEY_D):
            self.position_x += 1
            self.direction = 1
            self.running = True
        if pyxel.btn(pyxel.KEY_A):
            self.position_x -= 1
            self.direction = 0
            self.running = True
        if pyxel.btn(pyxel.KEY_W):
            self.position_y -= 1
            self.running = True
            
        if pyxel.btn(pyxel.KEY_S):
            self.position_y += 1
            self.running = True

        if pyxel.btn(pyxel.KEY_SPACE) and self.estamine >= 1:
            self.attacking = True
            self.estamine = 0

        if self.estamine < 1:
            self.estamine += 0.05

        if self.running:
            self.frame += 0.5
            self.frame = self.frame % 4

   
   