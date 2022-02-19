
from xml.dom import minidom


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
        print(elem.firstChild.data)


