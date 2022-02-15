from xml.dom import minidom
#ruta= input("Ingrese dirección del archivo xml:")

xml= minidom.parse('c:\Users\Linda Quelex\Desktop\UNIVERSIDAD 2022\LAB IPC2\PROYECTO 1 VERSIONES GIT\IPC2_Proyecto1_201403745\CÓDIGO PROYECTO\ARCHIVOENTRADA.XML')
#print(xml)    

piso= xml.getElementsByTagName ('R')
#print (piso[1].attributes['nombre'].value)
print()
