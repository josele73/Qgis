import os 
from qgis.core import *

# path del shape Ej: /home/project/data/ports.shp
path_capa= "c:/a/alturas/CONSTRU.SHP"

# vlayer = QgsVectorLayer(fichero_shape, nombre_al_cargar, provideedor)
vlayer = QgsVectorLayer(path_capa, "construcciones", "ogr")

#Comprobacion
if not vlayer.isValid():
    print("Error de carga!")
else:
    QgsProject.instance().addMapLayer(vlayer)
    print("Fichero cargado")