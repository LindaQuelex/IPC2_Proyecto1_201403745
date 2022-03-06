from listapatrones import ListaPatrones
from listacelda import ListaCelda

class NodoPiso():
    def __init__(self, nombrepiso, R, C, F, S) :
        self.id=0
        self.nombrepiso= nombrepiso
        self.fila= R
        self.columna= C
        self.precioflip= F
        self.precioslide= S
        self.siguiente=None
        self.anterior=None
        self.patrones= ListaPatrones()
       
    
    def setId(self,id):
        self.id=id

    def getId(self):
        return self.id

    def getnombrepiso(self):
        return self.nombrepiso
    
    def setnombrepiso(self, nombrepiso):
        self.nombrepiso = nombrepiso

    def getfila(self):
        return self.fila

    def setfila(self, fila):
        self.fila =fila

    def getcolumna(self):
        return self.columna

    def setcolunma(self, columna):
        self.columna =columna

    def getprecioflip(self):
        return self.precioflip

    def setprecioflip(self, precioflip):
        self.precioflip = precioflip

    def getprecioslide(self):
        return self.precioslide

    def setprecioslide(self, precioslide):
        self.precioslide =precioslide

 
    def getsiguiente(self):
        return self.siguiente

    def setsiguiente(self, nuevopiso):
        self.siguiente = nuevopiso

    def getanterior(self):
        return self.anterior

    def setanterior(self,anterior):
        self.anterior = anterior
   
   
 
    def getListapatrones(self):
        return self.getListapatrones()

    def setlistapatrones(self, nuevalistapatrones):
        self.patrones = nuevalistapatrones


    def getListaceldas(self):
        return self.getListaceldas()

    def setlistaceldas(self, nuevalistaceldas):
        self.celdas= nuevalistaceldas
    
    # def inicializarceldas(self):
    #     #self.nombrespiso1.crearpatrones(Lecturaxml)
    #     self.patrones.crearpatrones()
    #     self.celda.crearnodo()
    #     self.fila.crearfila()
    #     self.columna.crearcolumna()
        
    #crear lista vacia con base a variables declaradas
    #for anidado para fila y columna

