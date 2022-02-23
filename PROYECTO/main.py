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
        print(piso.attrib['nombre'])
        for variable in piso:
            var2=variable.text
            etiqueta2=variable.tag
            print (etiqueta2, var2)
            if variable.tag=="patrones":
                for patron in variable:
                    etiqueta3=patron.tag
                    var3=patron.text
                    print (patron.attrib, var3) 
                                    
elementTree('./ARCHIVOS ENTRADA/piso.xml')

'''def main():
    user_response = input('Write a word: ')
    # Si deseas recorrer la palabra puedes hacer esto
    for char in user_response: # los strings son iterables
        print(char)
    """Output
    Write a word: hello world
    h
    e
    l
    l
    o

    w
    o
    r
    l
    d"""
    # Si lo que deseas es simplemente obtener el arreglo para procesarlo o lo que sea puedes hacer lo siguiente:
    word_chars = list(user_response)
    print(word_chars)
    """Output
    Write a word: hi
    ['h', 'i']

if __name__ == '__main__':
    main()'''

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



'''crearpisos=Crearlistapisos.inserta_al_final(piso.attrib['nombre'], R.text , C.text, F.text, S.text)         
        patrones = piso[4]
        for patron in patrones:
            y=patron.tag
            z=patron.text
            print("prueba1")
            #crearpisos.patrones.inserta_al_final_patrones(p.text)
            print("prueba2")
        #crearpisos.patrones.mostrar_patrones()
             color=patron.text[0]
             for c in p: 
                  #print("se inserto",p.tag)
                 crearpisos.celda.inserta_al_final_celda(p.text)
             crearpisos.celda.mostrar_celda()     
     Crearlistapisos.mostrar_pisos()'''
