from nodopatrones import NodoPatrones
from nodopiso import NodoPiso
from listapatrones import ListaPatrones

class ListaPisos():
    def __init__(self):
        self.primero: NodoPiso= None
        self.ultimo=None
        self.size = 0

     
    def insertar(self, nuevo:NodoPiso):
        self.size +=1
        if self.primero == None:
            self.primero = nuevo
            self.ultimo =nuevo
        else:
            if nuevo.id < self.primero.id:
               nuevo.siguiente=self.primero
               self.primero.anterior=nuevo
               self.primero =nuevo
            elif nuevo.id > self.ultimo.id:
                self.ultimo.siguiente =nuevo
                nuevo.anterior =self.ultimo
                self.ultimo =nuevo
            else:
                tmp : NodoPiso =self.primero
                while tmp != None:
                    if nuevo.id < tmp.id:
                        nuevo.siguiente =tmp
                        nuevo.anterior =tmp.anterior
                        tmp.anterior.siguiente= nuevo
                        tmp.anterior=nuevo
                        break
                    elif nuevo.id >tmp.id:
                        tmp = tmp.siguiente
                    else:
                        break 




    def inserta_al_final(self, nombrepiso, R, C, F, S):
        nuevopiso=NodoPiso(nombrepiso, R, C, F, S)
        nuevopiso.setId(self.size)
        self.size += 1 
        if self.primero is None: 
            self.primero=nuevopiso
            self.ultimo=nuevopiso
        else:
           self.ultimo.setsiguiente(nuevopiso)
           self.ultimo=nuevopiso
        nuevopiso.patrones.inserta_al_final_patrones
        return nuevopiso
    
    def retornarNodoPiso(self,id):
        aux = self.primero
        while aux.getId()<id:
            aux=aux.getsiguiente()
        return aux

    def mostrar_pisos(self):
        tmp=self.primero
        for i in range(self.size):
            print('El número de piso es:','(',i,')','\n','El nombre del piso es:', tmp.getnombrepiso(),'\n','-cantidad de filas:',tmp.getfila(),'\n','-cantidad de columnas:',tmp.getcolumna(),'\n','-precio por voltear:',tmp.getprecioflip(), '\n','-precio por deslizar:',tmp.getprecioslide())
            tmp.patrones.mostrar_patrones()
            tmp = tmp.getsiguiente()


    def mostrar(self):
        tmp=self.primero
        while tmp != None:
            print("temporal",tmp.id, tmp.nombrepiso,tmp.fila, tmp.columna, tmp.precioflip, tmp.precioslide)
            tmp=tmp.siguiente


    def ordenar_pisos_BubbleSortStd(self):
        comprobar = self.primero
        aux = self.primero
        if comprobar.siguiente != None and aux != None:
            i = self.primero
            while i != None:
                j = i.siguiente
                while j != None:
                    if i.nombrepiso > j.nombrepiso:
                        temporal = i.nombrepiso
                        i.nombrepiso = j.nombrepiso
                        j.nombrepiso = temporal
                    j = j.siguiente
                i = i.siguiente
                



# pruebadelistapisos = ListaPisos('nodo')
# pruebadelistapisos.inserta_al_final("mm2",3,54,4,112)
# pruebadelistapisos.inserta_al_final("mm05",3,54,4,112)
# print (pruebadelistapisos, "pruebaaaa")
# pruebadelistapisos.mostrar_pisos()

nodos=ListaPisos()
nodo2= NodoPiso('ejemplo02', None,2,3,4)
nodo1= NodoPiso('ejemplo99', 1,2,3,4)
nodo3= NodoPiso('ejemplo12', 1,2,3,4)
nodo4= NodoPiso('ejemplo04', 1,2,3,4)

nodos.insertar(nodo3)
nodos.insertar(nodo4)
nodos.insertar(nodo2)
nodos.insertar(nodo1)

nodos.mostrar()
