from listacelda import ListaCelda

class NodoPatrones():
    def __init__(self, codigopatrones, cadenapatrones):
        self.codigopatrones= codigopatrones
        self.anterior=None
        self.siguiente=None
        self.celdas=ListaCelda()


    def getcodigopatrones(self):
        return self.codigopatrones

    def setcodigopatrones(self, codigopatrones):
        self.codigopatrones = codigopatrones

    def getsiguiente(self):
        return self.siguiente

    def setsiguiente(self, nuevopiso):
        self.siguiente = nuevopiso

    def getanterior(self):
        return self.anterior

    def setanterior(self, nuevopatron):
        self.anterior = nuevopatron
   
        

