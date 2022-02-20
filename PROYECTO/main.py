
import xml.etree.ElementTree as ET
from listapisos import ListaPisos

#from listapatrones import ListaPatrones
#from xml.dom import minidom

'''PRUEBA CON MINIDOM
class Lecturaxml():
    ruta = ("piso.xml")
    doc = minidom.parse(ruta)
    nombrepisoxml = doc.getElementsByTagName ("piso")
    print (nombrepisoxml)

    print ('\nLos nombre de los pisos son:')
    for elem in nombrepisoxml:
        print(elem.attributes['nombre'].value)
        
    print('\nLos datos son: ')
    for elem in nombrepisoxml:
        print(elem.firstChild.data)'''
 

Crearlistapisos = ListaPisos()

def elementTree(ruta):
    tree=ET.parse(ruta)
    raiz= tree.getroot()
    #print (raiz , ":)")
    for piso in raiz:   
        R= piso[0]  
        C= piso[1]
        F= piso[2]
        S= piso[3]

        #for datospiso in piso:
        #     print("-", datospiso.text)             #hasta aqui funcionaba
        #     for patron in datospiso:
        #         print('patrones disponibles para este piso artesanal',patron.text)    #hasta aqui funcionaba 
        # R= int(R)
       
        Crearlistapisos.inserta_al_final(piso.attrib['nombre'], R.text, C.text,F.text,S.text)
    Crearlistapisos.mostrar_pisos()
   
elementTree('./ARCHIVOS ENTRADA/piso.xml')