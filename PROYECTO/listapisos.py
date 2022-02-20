from nodopiso import NodoPiso

class ListaPisos():
    def __init__(self):
        self.primero: NodoPiso= None
        self.ultimo=None
        self.size = 0

    def inserta_al_final(self, nombrepiso, R, C, F, S):
        nuevopiso=NodoPiso(nombrepiso, R, C, F, S)
        self.size += 1 
        if self.primero is None:
            self.primero=nuevopiso
            self.ultimo=nuevopiso
        else:
           self.ultimo.setsiguiente(nuevopiso)
           self.ultimo=nuevopiso
        return nuevopiso

    def mostrar_pisos(self):
        tmp=self.primero
        for i in range(self.size):
            print(i,'El nombre del piso es:', tmp.getnombrepiso(),'\n','-cantidad de filas:',tmp.getfila(),'\n','-cantidad de columnas:',tmp.getcolumna(),'\n','-precio por voltear:',tmp.getprecioflip(), '\n','-precio por deslizar:',tmp.getprecioslide())
            tmp = tmp.getsiguiente()


# pruebadelistapisos = ListaPisos()
# pruebadelistapisos.inserta_al_final("mm2",3,54,4,112)
# pruebadelistapisos.inserta_al_final("mm05",3,54,4,112)
# print (pruebadelistapisos, "pruebaaaa")

# pruebadelistapisos.mostrar_pisos()