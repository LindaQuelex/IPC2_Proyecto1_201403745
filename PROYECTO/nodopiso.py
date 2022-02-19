from listacelda import ListaCelda
from listapatrones import ListaPatrones
from lecturaxml import Lecturaxml

class NodoPiso():
    def __init__(self, nombrepiso, R, C,color, F, S, siguiente, anterior) :
        self.nombrepiso= nombrepiso
        self.fila= R
        self.columna= C
        self.precioflip= F
        self.precioslide= S
        self.anterior=None
        self.siguiente=None
        self.patrones= ListaPatrones()
        self.celda= ListaCelda()
    
    
    def inicializarceldas(self):
        self.nombrespiso1.crearpatrones(Lecturaxml)
        self.patrones.crearpatrones()
        self.celda.crearnodo()
        self.fila.crearfila()
        self.columna.crearcolumna()
        
        
    #crear lista vacia con base a variables declaradas
    #for anidado para fila y columna

