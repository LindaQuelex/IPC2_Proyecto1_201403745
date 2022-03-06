from listacelda import ListaCelda

class NodoPatrones():
    def __init__(self, codigopatrones):
        self.id=0
        self.codigopatrones= codigopatrones
        self.anterior=None
        self.siguiente=None
        self.listaceldas=ListaCelda()

    def getid(self):
        return self.id

    def setid(self, id):
        self.id =id

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
   
    def getlistacelda(self):
        return self.listaceldas

    def setlistaceldas(self, nuevacelda):
        self.listaceldas = nuevacelda