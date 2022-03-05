
import xml.etree.ElementTree as ET
from listacelda import ListaCelda
from listapatrones import ListaPatrones
from listapisos import ListaPisos

Crearlistapisos = ListaPisos()

def elementTree(ruta):
    contador=0
    tree=ET.parse(ruta)
    raiz= tree.getroot()
    print (raiz , "posición en memoria de la etiqueta raíz")
    for piso in raiz:
        nombrepiso=(piso.attrib['nombre'])
        for datospiso in piso:
            dptag=datospiso.tag
            dp=datospiso.text
            if datospiso.tag=="R":
                row= datospiso.text
            if datospiso.tag=="C":
                colum=datospiso.text
            if datospiso.tag=="F":
                cost_flip=datospiso.text
            if datospiso.tag =="S":
                cost_slide=datospiso.text
                Crearlistapisos.inserta_al_final(nombrepiso,row, colum, cost_flip, cost_slide)
            if datospiso.tag=="patrones":
                contadordos=0
                for patron in datospiso:
                    patrontag=patron.tag
                    codigopatron=patron.attrib['codigo']
                    cadenapatron=patron.text
                    Crearlistapisos.retornarNodoPiso(contador).patrones.inserta_al_final_patrones(codigopatron)
                    colorcelda=cadenapatron
                    for caracter in colorcelda:
                        Crearlistapisos.retornarNodoPiso(contador).patrones.retornar_nodo(contadordos).listaceldas.inserta_al_final_celda(caracter)
                    contadordos=contadordos+1
                contador=contador+1

elementTree('./ARCHIVOS ENTRADA/piso.xml')
print("******************************")
print("PISOS ARTESANALES DISPONIBLES")
print("******************************")
Crearlistapisos.mostrar_pisos()


print("*************************************************************")
obtenerpiso=input("INGRESE EL NÚMERO DE PISO A DISEÑAR:")
obtenerpatron=input("INGRESE EL NÚMERO CORRELATIVO DEL PATRON A DISEÑAR:")
print("*************************************************************")

if int(obtenerpiso)< Crearlistapisos.size:
    if int(obtenerpatron)< Crearlistapisos.retornarNodoPiso(int(obtenerpiso)).patrones.size:
        Crearlistapisos.retornarNodoPiso(int(obtenerpiso)).patrones.retornar_nodo(0).listaceldas.grafica_inicial()
        Crearlistapisos.retornarNodoPiso(int(obtenerpiso)).patrones.retornar_nodo(int(obtenerpatron)).listaceldas.grafica_seleccionada()
        print("*************************************************************")
        print("EL PATRON INICIAL ES: VER ARCHIVO PDF ------>Grafica piso inicial.pdf")
        print("EL PATRON A DISEÑAR ES: VER ARCHIVO PDF------>Grafica piso seleccionado.pdf")
        print("*************************************************************")
    else:
        print("No exite le número de patron xd")
    
else:
    print("No existe el número de piso :)")

