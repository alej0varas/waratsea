from vela import Vela
from palos import tipos_palo

class Palo:
    def __init__(self, tipo):
        self.tipo = tipos_palo[tipo]
        self.velas = [ Vela(tipo) for tipo in self.tipo['velas'] ]
