# Script en QGis

## Carga ficheros vectoriales

carga_vectorial.py
```
import os 
from qgis.core import *

# path del shape Ej: /home/project/data/ports.shp
path_capa= "c:/a/alturas/CONSTRU.SHP"

# vlayer = QgsVectorLayer(fichero_shape, nombre_al_cargar, proveedor)
vlayer = QgsVectorLayer(path_capa, "construcciones", "ogr")

#Comprobacion
if not vlayer.isValid():
    print("Error de carga!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    print("Fichero cargado")
````

## Carga todos los ficheros vectoriales de un directorio

carga_directorio.py
```
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
      
        #Nombre que le asignamos al fichero
        baseName=os.path.splitext(fich)[0]
       
        #cargamos en el visor
        iface.addVectorLayer(fileName, baseName, "ogr")
        print ("Cargada capa "+baseName)
```

## Listado de campos: Nombre y tipo

```
for field in vlayer.fields():
    print(field.name(), field.typeName())
```
