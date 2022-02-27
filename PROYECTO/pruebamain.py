import xml.etree.ElementTree as ET
from listacelda import ListaCelda
from listapatrones import ListaPatrones
from listapisos import ListaPisos

Crearlistapisos = ListaPisos()
Crearlistacodpatron =ListaPatrones()
Crearlistaceldas =ListaCelda()


def elementTree(ruta):
    tree=ET.parse(ruta)
    raiz= tree.getroot()
    print (raiz , "posición en memoria de la etiqueta raíz")
    for piso in raiz:
        nombrepiso=(piso.attrib['nombre'])
        #print(nombrepiso)
        for datospiso in piso:
            dptag=datospiso.tag
            dp=datospiso.text
            if datospiso.tag=="R":
                row= datospiso.text
                #print(row)
            if datospiso.tag=="C":
                colum=datospiso.text
                #print(colum)
            if datospiso.tag=="F":
                cost_flip=datospiso.text
                #print(cost_flip)
            if datospiso.tag =="S":
                cost_slide=datospiso.text
                #print (cost_slide)  
                listapisos=Crearlistapisos.inserta_al_final(nombrepiso,row, colum, cost_flip, cost_slide)
                print ("Se inserto el piso", listapisos.getnombrepiso(),'\n', "Cantidad de filas:", listapisos.getfila(),'\n', "Cantidad de columnas:", listapisos.getcolumna(),'\n', "Costo de voltear:", listapisos.getprecioflip(),'\n', "Costo de deslizar:", listapisos.getprecioslide())
            if datospiso.tag=="patrones":
                for patron in datospiso:
                    patrontag=patron.tag
                    codigopatron=patron.attrib
                    cadenapatron=patron.text
                    #print (patrontag, codigopatron, cadenapatron)
                    codpatronesinlist= listapisos.patrones.inserta_al_final_patrones(codigopatron)
                    print("Se inserto el codigo patron:", codpatronesinlist.getcodigopatrones())
                    colorcelda=cadenapatron
                    for caracter in colorcelda:
                        #print(caracter)
                        cadenacolores= codpatronesinlist.listaceldas.inserta_al_final_celda(caracter)
                        print("Se inserto el color:", cadenacolores.getcolorcelda())
                        #listapisos.celda.inserta_al_final_celda()
    
                #listapisos.celda.mostrar_celda()
                # listapisos=Crearlistapisos.inserta_al_final(nombrepiso,row, colum, cost_flip, cost_slide)     
    #Crearlistapisos.mostrar_pisos()
    
   
#Crearlistaceldas.recorrer_lista()
Crearlistaceldas.inserta_al_final_celda("w")
Crearlistaceldas.inserta_al_final_celda("b")
Crearlistaceldas.mostrar_celda()
Crearlistaceldas.grafica_inicial()





elementTree('./ARCHIVOS ENTRADA/piso.xml')