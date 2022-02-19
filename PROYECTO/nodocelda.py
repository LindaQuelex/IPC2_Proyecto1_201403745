class NodoCelda():
    def __init__(self, r,c, color ):
        self.fila = r
        self.columna = c
        self.color =color
        self.siguiente = None
        self.anterior = None

    class DoublyLinkedList:
        def __init__(self):
            self.start_node = None


    def insertar_en_lista_vacia(self, data):
        if self.start_node is None:
            new_node = NodoCelda(data)
            self.start_node = new_node
        else:
            print("list is not empty")


    def insetar_al_inicio(self, data):
        if self.start_node is None:
            new_node = NodoCelda(data)
            self.start_node = new_node
            print("node inserted")
            return
        new_node = NodoCelda(data)
        new_node.nref = self.start_node
        self.start_node.pref = new_node
        self.start_node = new_node

    def inserta_al_final(self, data):
        if self.start_node is None:
            new_node = NodoCelda(data)
            self.start_node = new_node
            return
        n = self.start_node
        while n.nref is not None:
            n = n.nref
        new_node = NodoCelda(data)
        n.nref = new_node
        new_node.pref = n

    def insertar_despues_de_otro(self, x, data):
        if self.start_node is None:
            print("List is empty")
            return
        else:
            n = self.start_node
            while n is not None:
                if n.item == x:
                    break
                n = n.nref
            if n is None:
                print("item not in the list")
            else:
                new_node = NodoCelda(data)
                new_node.pref = n
                new_node.nref = n.nref
                if n.nref is not None:
                    n.nref.prev = new_node
                n.nref = new_node


    def insertar_delante_de_otro(self, x, data):
        if self.start_node is None:
            print("List is empty")
            return
        else:
            n = self.start_node
            while n is not None:
                if n.item == x:
                    break
                n = n.nref
            if n is None:
                print("item not in the list")
            else:
                new_node = NodoCelda(data)
                new_node.nref = n
                new_node.pref = n.pref
                if n.pref is not None:
                    n.pref.nref = new_node
                n.pref = new_node


    def recorrer_lista(self):
        if self.start_node is None:
            print("La lista no tiene elementos")
            return
        else:
            n = self.start_node
            while n is not None:
                print(n.item , " ")
                n = n.nref

    def eliminar_al_inicio(self):
        if self.start_node is None:
            print("La lista no contiene elementos para eliminar")
            return 
        if self.start_node.nref is None:
            self.start_node = None
            return
        self.start_node = self.start_node.nref
        self.start_prev = None;


    def eliminar_al_final(self):
        if self.start_node is None:
            print("The list has no element to delete")
            return 
        if self.start_node.nref is None:
            self.start_node = None
            return
        n = self.start_node
        while n.nref is not None:
            n = n.nref
        n.pref.nref = None

        


    