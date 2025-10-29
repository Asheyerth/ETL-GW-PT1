# ETL 
## Generación de los datos 
Se generan datos fake de forma semicontrolada en volúmenes pequeños para efectos de testing y claridad durante el desarrollo. 
Ver el archivo *<Generate_data.py>* para mayor claridad del proceso. Los datos generados sin procesar se pueden encontrar en formato **csv** en la carpeta ***/raw***.
Se escogió el formato **csv** para términos de facilidad. Este formato permite ser escrito de forma más rápida, es mejor legible por variados métodos y para el caso actual se están usando pequeños volúmenes de datos. En dado caso se busque algo más especializado y de mayor volumen (alcanzando el millón de filas en adelante), el formato más indicado es **parquet**. 