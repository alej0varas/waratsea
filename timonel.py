# Clase Timonel

class Timonel:
    def __init__(self, nave):
        self.habilidad = 0.5
        self.nave = nave

    def jugar(self):
		self.timonear()

    def timonear(self):
        dr = self.nave.rumbo_verdadero.valor - self.nave.rumbo.valor
        if dr:
            cant = 1
            if self.nave.rumbo_verdadero.valor < 180:
                if self.nave.rumbo.valor < 180:
                    if dr > 0:
                        self.nave.timon.iz(cant)
                    else:
                        self.nave.timon.de(cant)
                else:
                    if abs(dr) < 180:
                        self.nave.timon.de(cant)
                    else:
                        self.nave.timon.iz(cant)
            else:
                if self.nave.rumbo.valor > 180:
                    if dr > 0:
                        self.nave.timon.iz(cant)
                    else:
                        self.nave.timon.de(cant)
                else:
                    if dr > 180:
                        self.nave.timon.de(cant)
                    else:
                        self.nave.timon.iz(cant)
