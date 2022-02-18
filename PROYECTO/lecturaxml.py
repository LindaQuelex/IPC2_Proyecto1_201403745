from ast import Attribute
from xml.dom import minidom
 
ruta = ("piso.xml")
doc = minidom.parse(ruta)
piso = doc.getElementsByTagName ("piso")

#print("Los códigos de los pisos son:")
#print( piso[1].attributes["nombre"].value)

print ('\nLos nombres de los pisos son:')
for elem in piso:
    print(elem.attributes['nombre'].value)
    

print('\nLos datos son: ')
for elem in piso:
    print(elem.firstChild.data)



