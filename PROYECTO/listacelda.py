
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
    

    def grafica_inicial(self):
        temp = self.primero
       
        graficadefault=" digraph G { \n"
        while temp is not None:
            graficadefault += '{}[label="{}",color = "black",fillcolor="black", fontcolor="green",style="filled",shape="box"];\n'.format(temp.colorcelda,temp.colorcelda)
            temp=temp.siguiente

        temp=self.primero
        while temp is not None:
            if temp.siguiente is None:
                None
            else: 
                graficadefault += '{}->{};\n'.format(temp.colorcelda,temp.siguiente.colorcelda)
            temp=temp.siguiente
        graficadefault +="}"
        documentotxt="Graficapisoinicial.txt"
        with open(documentotxt,'w') as grafica: 
            grafica.write(graficadefault)
        pdf="Graficapisoinicial.pdf"
        os.system('dot -Tpdf '+documentotxt+" -o "+pdf)
        webbrowser.open(pdf)

    
    def recorrer_lista(self):
        if self.iniciarnodocelda is None:
            print("La lista no tiene elementos")
            return
        else:
            n = self.iniciarnodocelda
            while n is not None:
                print("La lista de celdas es:",n.colorcelda , "funciona el método de recorrer lista")    
                n = n.siguiente


    def mostrar_celda(self):
        tmp=self.primero
        for i in range(self.size):
            print(i,'*El color de la celda es:',tmp.getcolorcelda())
            tmp = tmp.getsiguiente()


    def retornar_nodo(self, id):
        aux=self.primero
        while aux.getidcelda()< id:
            aux=aux.getsiguiente()
        return aux












