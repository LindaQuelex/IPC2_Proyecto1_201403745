from listacelda import ListaCelda
from listapatrones import ListaPatrones

class NodoPiso():
    def __init__(self, codigopiso, R, C,color, F, S, siguiente, anterior) :
        self.codigopiso= codigopiso
        self.fila= R
        self.columna= C
        self.precioflip= F
        self.precioslide= S
        self.anterior=None
        self.siguiente=None
        self.patrones= ListaPatrones()
        self.celda= ListaCelda()
    
    
    def inicializarceldas(self):
        self.patrones.crearpatrones()
        self.celda.crearnodo()
        self.fila.crearfila()
        self.columna.crearcolumna()
        
    #crear lista vacia con base a variables declaradas
    #for anidado para fila y columna

