from nodopatrones import NodoPatrones

class ListaPatrones():
    def __init__(self):
    
        self.primero: NodoPatrones= None
        self.ultimo=None
        self.size = 0


    def inserta_al_final_patrones(self, codigopatrones):
        nuevopatron=NodoPatrones(codigopatrones)
        nuevopatron.setid(self.size)
        self.size += 1 
        if self.primero is None:
            self.primero=nuevopatron
            self.ultimo=nuevopatron
        else:
           self.ultimo.setsiguiente(nuevopatron)
           self.ultimo=nuevopatron
           #nuevopatron.nuevacelda
        nuevopatron.listaceldas.inserta_al_final_celda
        return nuevopatron

    def retornar_nodo(self, id):
        aux=self.primero
        while aux.getid()< id:
            aux=aux.getsiguiente()
        return aux

        

    def mostrar_patrones(self):
        tmp=self.primero
        for i in range(self.size):
            print('     El correlativo del patron es: ', i,'\n','     Patron: ',tmp.getcodigopatrones(),' Las celdas del patron son:')
            tmp.listaceldas.mostrar_celda()
            tmp = tmp.getsiguiente()
        