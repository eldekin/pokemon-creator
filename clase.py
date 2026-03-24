class Pokemon:
    def __init__(self, nombre, numero, tipo, pc, nivel):
        self.nombre = nombre
        self.numero = numero
        self.tipo = tipo
        self.pc = pc
        self.nivel = nivel

    def to_dict(self):
        return {
            "nombre": self.nombre,
            "numero": self.numero,
            "tipo": self.tipo,
            "pc": self.pc,
            "nivel": self.nivel
        }