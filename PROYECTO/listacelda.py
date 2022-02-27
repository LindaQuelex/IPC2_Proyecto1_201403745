
from nodocelda import NodoCelda
import os
import webbrowser
import graphviz

class ListaCelda():
    def __init__(self):
        self.iniciarnodocelda = None
        self.primero : NodoCelda=None
        self.ultimo= None
        self.size=0

    def inserta_al_final_celda(self, color):
        nuevacelda=NodoCelda(color)
        self.size += 1 
        if self.primero is None:
            self.primero=nuevacelda
            self.ultimo=nuevacelda
        else:
           self.ultimo.setsiguiente(nuevacelda)
           self.ultimo=nuevacelda
        return nuevacelda
    

    def grafica(self):
        auxNodo = self.primero
        strGrafica=" digraph G { \n"
        ##----------while para crear nodos
        while auxNodo is not None:
            strGrafica += '{}[label="{}",color = "green",arrowhead = "diamond",fillcolor="red",style="filled",shape="box"];\n'.format(auxNodo.colorcelda,auxNodo.colorcelda)
            auxNodo=auxNodo.siguiente
        ##----------while para Unir nodos
        auxNodo=self.primero
        while auxNodo is not None:
            if auxNodo.siguiente is None:
                None
            else: 
                strGrafica += '{}->{};\n'.format(auxNodo.colorcelda,auxNodo.siguiente.colorcelda)
            auxNodo=auxNodo.siguiente
        ##-------------Creacion de texto plato y conversion
        strGrafica +="}"
        documentotxt="Graficapiso1.txt"
        with open(documentotxt,'w') as grafica: 
            grafica.write(strGrafica)
        pdf="Graficapiso1.pdf"
        os.system("neato -Tpdf "+documentotxt+" -o "+pdf)
        webbrowser.open(pdf)

    def recorrer_lista(self):
        if self.iniciarnodocelda is None:
            print("La lista no tiene elementos")
            return
        else:
            n = self.iniciarnodocelda
            while n is not None:
                print("La lista de celdas es:",n.color , "funciona el método de recorrer lista")    
                n = n.siguiente


    def mostrar_celda(self):
        tmp=self.primero
        for i in range(self.size):
            print('*El color de la celda es:',tmp.getcolorcelda())
            tmp = tmp.getsiguiente()


  















    '''def insertar_en_lista_vacia(self, r,c,color):
        if self.iniciarnodocelda is None:
            nuevonodo = NodoCelda(r,c,color)
            self.iniciarnodocelda = nuevonodo
        else:
            print("La lista no esta vacía") #La lista ya contiene el patron de pisos artesanales

    def insetar_al_inicio(self, r,c,color):
        if self.iniciarnodocelda is None:
            nuevonodo = NodoCelda(r,c,color)
            self.iniciarnodocelda = nuevonodo
            print("Celda de piso insertada")
            return
        nuevonodo = NodoCelda(r,c,color)
        nuevonodo.siguiente = self.iniciarnodocelda
        self.iniciarnodocelda.anterior = nuevonodo
        self.iniciarnodocelda = nuevonodo

    def inserta_al_final(self, r,c,color):
        if self.iniciarnodocelda is None:
            nuevonodo = NodoCelda(r,c,color)
            self.iniciarnodocelda = nuevonodo
            return
        n = self.iniciarnodocelda
        while n.siguiente is not None:
            n = n.siguiente
        nuevonodo = NodoCelda(r,c,color)
        n.siguiente = nuevonodo
        nuevonodo.anterior = n

    def insertar_despues_de_otro(self, x, r,c,color):
        if self.iniciarnodocelda is None:
            print("La lista esta vacía")
            return
        else:
            n = self.iniciarnodocelda
            while n is not None:
                if n.color == x:   #como hago para jalar todos los valores del nodo y no solo un dato?
                    break
                n = n.siguiente
            if n is None:
                print("El color no esta en lista")
            else:
                nuevonodo = NodoCelda(r,c,color)
                nuevonodo.anterior = n
                nuevonodo.siguiente = n.siguiente
                if n.siguiente is not None:
                    n.siguiente.anterior = nuevonodo
                n.siguiente = nuevonodo

    def insertar_delante_de_otro(self, x, r,c,color):
        if self.iniciarnodocelda is None:
            print("La lista esta vacía")
            return
        else:
            n = self.iniciarnodocelda
            while n is not None:
                if n.color == x: #como hago para jalar todos los valores del nodo y no solo un dato?
                    break
                n = n.siguiente
            if n is None:
                print("El color no esta en la lista")
            else:
                nuevonodo = NodoCelda(r,c, color)
                nuevonodo.siguiente= n
                nuevonodo.anterior = n.siguiente
                if n.anterior is not None:
                    n.anterior.siguiente = nuevonodo
                n.anterior = nuevonodo



    def eliminar_al_inicio(self):
        if self.iniciarnodocelda is None:
            print("La lista no contiene elementos para eliminar")
            return 
        if self.iniciarnodocelda.siguiente is None:
            self.iniciarnodocelda = None
            return
        self.iniciarnodocelda = self.iniciarnodocelda.siguiente
        self.iniciaranterior = None;


    def eliminar_al_final(self):
        if self.iniciarnodocelda is None:
            print("La lista no tienen elementos para eliminar")
            return 
        if self.iniciarnodocelda.siguiente is None:
            self.iniciarnododcelda = None
            return
        n = self.iniciarnodocelda
        while n.siguiente is not None:
            n = n.siguiente
        n.anterior.siguiente = None


    def elimimar_por_valor(self, x):
        if self.iniciarnodocelda is None:
            print("La lista no tiene elementos para eliminar")
            return 
        if self.iniciarnodocelda.siguiente is None:
            if self.iniciarnodocelda.color == x: #como hago para jalar todos los valores del nodo y no solo un dato?
                self.iniciarnodocelda= None
            else:
                print("Color no encontrado")
            return 

        if self.iniciarnodocelda.color == x:  #como hago para jalar todos los valores del nodo y no solo un dato?
            self.iniciarnodocelda = self.iniciarnodocelda.siguiente
            self.iniciarnodocelda.anterior = None
            return

        n = self.iniciarnodocelda
        while n.siguiente is not None:
            if n.color == x:
                break;
            n = n.siguiente
        if n.siguiente is not None:
            n.anterior.siguiente = n.siguiente
            n.siguiente.anterior = n.anterior
        else:
            if n.color  == x:             #como hago para jalar todos los valores del nodo y no solo un dato?
                n.anterior.siguiente = None
            else:
                print("Elemento no encontrado")

    def invertir_lista(self):
        if self.iniciarnodocelda is None:
            print("La lista no tiene elementos para eliminar")
            return 
        p = self.iniciarnodocelda
        q = p.siguiente
        p.siguiente = None
        p.anterior = q
        while q is not None:
            q.anterior = q.siguiente
            q.siguiente = p
            p = q
            q = q.anterior
        self.iniciarnodocelda = p'''


#PRUEBA DE FUNCIONES DE LA LISTA DOBLEMENTE ENLAZADA

# nuevalistacelda = ListaCelda()
# nuevalistacelda.insertar_en_lista_vacia(2,3,"W")
# nuevalistacelda.recorrer_lista()