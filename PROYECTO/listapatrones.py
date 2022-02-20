from nodopatrones import NodoPatrones

class ListaPatrones():
    def __init__(self, codigopatrones):
        self.codigopatrones = codigopatrones
        self.primero: NodoPatrones= None
        self.ultimo=None
        self.size = 0


    def inserta_al_final_patrones(self, codigopatrones):
        nuevopatron=NodoPatrones(codigopatrones)
        self.size += 1 
        if self.primero is None:
            self.primero=nuevopatron
            self.ultimo=nuevopatron
        else:
           self.ultimo.setsiguiente(nuevopatron)
           self.ultimo=nuevopatron

    def mostrar_patrones(self):
        tmp=self.primero
        for i in range(self.size):
            print(i,'El codigo del patron es:', tmp.getcodigopatrones())
            tmp = tmp.getsiguiente()