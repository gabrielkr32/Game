class Body:
    def __init__(self, x, y, largura, altura):
        self.x = x
        self.y = y
        self.largura = largura
        self.altura = altura

    def verificar_colisao(self, outro_objeto):
        if self.x < outro_objeto.x + outro_objeto.largura and \
           self.x + self.largura > outro_objeto.x and \
           self.y < outro_objeto.y + outro_objeto.altura and \
           self.y + self.altura > outro_objeto.y:
            return True
        return False