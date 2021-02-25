# Etiquetados condicionales en QGIS

## Para que con base en una variable puedan asignar tamaños a las letras de su etiqueta.

```
CASE WHEN "VPH_INTER" IN ( '*','N/D') THEN '5'Else'10'END
```

## Traducción: Cuando la columna "x" tenga ( 'valor 1' , ' valor 2') que el tamaño sea '5' , el resto '10'

```
CASE WHEN "VPH_INTER" IN ( '*','N/D') THEN '5' Else'10' END 
```

![Alt text](EvAjaewVIAAU1ed.png?raw=true "Title")

## ---
