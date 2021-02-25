# Script en Qgis

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

##Listado de campos: Nombre y tipo

```
for field in vlayer.fields():
    print(field.name(), field.typeName())
```
