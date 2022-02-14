class NodoPiso():
    def __init__(self, codigopiso, color, posicion_x,posicion_y, siguiente, anterior) :
        self.codigopiso= codigopiso
        self.color=color
        self.posicion_x= posicion_x
        self.posicion_y=posicion_y
        self.anterior=None
        self.siguiente=None