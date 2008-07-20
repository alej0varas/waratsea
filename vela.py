from velas import tipos_vela

class Vela:
    def __init__(self, tipo):
        self.tipo = tipos_vela[tipo]
        self.alto = self.tipo["alto"]
        self.ancho = self.tipo["ancho"]
##        self.formula =tipo.formula
