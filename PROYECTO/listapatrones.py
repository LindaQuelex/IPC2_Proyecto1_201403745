from nodocelda import NodoCelda
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
    
    def ordenar_patrones_BubbleSortStd(self):
        comprobar = self.primero
        aux = self.primero
        if comprobar.siguiente != None and aux != None:
            i = self.primero
            while i != None:
                j = i.siguiente
                while j != None:
                    if i.codigopatrones > j.codigopatrones:
                        temporal = i.codigopatrones
                        i.codigopatrones = j.codigopatrones
                        j.codigopatrones = temporal
                    j = j.siguiente
                i = i.siguiente
    
    def mov_precio_volter_es_menor(self,listaceldas):
        self.size +=1
        pass

# ListaPatrones.inserta_al_final_patrones(12)
# ListaPatrones.inserta_al_final_patrones(22)
# ListaPatrones.inserta_al_final_patrones(2)
# #ListaPatrones.ordenar_patrones_BubbleSortStd()
# ListaPatrones.mostrar_patrones()