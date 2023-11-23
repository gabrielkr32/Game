import pyxel
import body
DIRECAO_ESQUERDA = 0
DIRECAO_DIREITA = 1
DIRECAO_ACIMA = 2

class Hero:
    def __init__(self, game, position_x, position_y):
        self.game = game
        self.body = body.Body(position_x, position_y, 16, 16)
        self.position_x = position_x
        self.position_y = position_y
        self.direction = DIRECAO_ESQUERDA
        self.running = False
        self.attacking = True
        self.frame = 0
        self.estamine = 1
          

    def draw(self):
            if self.running:
                if self.direction == DIRECAO_ESQUERDA:
                   pyxel.blt(self.position_x, self.position_y, 0, 16*int(self.frame), 48, 16, 15, pyxel.COLOR_BLACK)
                if self.direction == DIRECAO_DIREITA:
                    pyxel.blt(self.position_x, self.position_y, 0, 16*int(self.frame), 32, 16, 15, pyxel.COLOR_BLACK)
                if self.direction == DIRECAO_ACIMA:
                    pyxel.blt(self.position_x, self.position_y, 0, 16*int(self.frame), 80, 16, 15, pyxel.COLOR_BLACK)
                 
                           
            else:
                    
            
                if self.attacking:
                    if self.direction == DIRECAO_ESQUERDA:
                       pyxel.blt(self.position_x, self.position_y, 0, 0, 16, 16, 15, pyxel.COLOR_BLACK)
                    if self.direction == DIRECAO_DIREITA:
                         pyxel.blt(self.position_x, self.position_y, 0, 16, 16, 16, 15, pyxel.COLOR_BLACK)    
                    if self.direction == DIRECAO_ACIMA:  
                        pyxel.blt(self.position_x, self.position_y, 0, 0, 80, 16, 15, pyxel.COLOR_BLACK)
                    

                else:
                    if self.direction == DIRECAO_ESQUERDA: 
                       pyxel.blt(self.position_x, self.position_y,  0, 0, 16, 16, 15, pyxel.COLOR_BLACK)

                    if self.direction == DIRECAO_DIREITA:
                       pyxel.blt(self.position_x, self.position_y,  0, 16, 0, 16, 15, pyxel.COLOR_BLACK)

                    if self.direction == DIRECAO_ACIMA:  
                        pyxel.blt(self.position_x, self.position_y, 0, 0, 80, 16, 15, pyxel.COLOR_BLACK)   
                    
                   
   
    def collided(self):
        for body in self.game.bodies:
            if self.body.verificar_colisao(body):
                return True
        return False 
             
                    


    def update(self):
        self.running = False
        self.attacking = False
       

        if pyxel.btn(pyxel.KEY_D):
            self.position_x += 1
            self.body.x += 1
            self.direction = DIRECAO_DIREITA
            self.running = True
        if pyxel.btn(pyxel.KEY_A):
            self.position_x -= 1
            self.body.x += 1
            self.direction = DIRECAO_ESQUERDA
            self.running = True
        if pyxel.btn(pyxel.KEY_W):
            self.position_y -= 1
            self.body.x += 1
            self.direction = DIRECAO_ACIMA
            self.running = True
            
        if pyxel.btn(pyxel.KEY_S):
            self.position_y += 1
            self.body.x += 1
            self.running = True
            
            
            
        if self.collided():
            self.body.x = self.position_x
            self.body.y = self.position_y
        else:
            self.position_x = self.body.x
            self.position_y = self.body.y
            

        if pyxel.btn(pyxel.KEY_SPACE) and self.estamine >= 1:
            self.attacking = True
            self.estamine = 0

        if self.estamine < 1:
            self.estamine += 0.05

        if self.running:
            self.frame += 0.5
            self.frame = self.frame % 4

   
   