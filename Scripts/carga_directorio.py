import os
from qgis.core import *


path="c:/a/alturas/"

ficheros = os.listdir( path )

#Si la extension en SHP lo cargamos en el visor

for fich in ficheros:
    extension = os.path.splitext(fich)[1]
    if extension ==  ".shp":
        #Ruta + Nombre fichero
        fileName=path+fich
        #print fileName
        #Nombre que le asignamos al fichero
        baseName=os.path.splitext(fich)[0]
        #print  baseName
        #cargamos en el visor
        iface.addVectorLayer(fileName, baseName, "ogr")
        print ("Cargada capa "+baseName)