#Resolución#
1 - Para ejecutar la aplicación correr:
python backend/main.py
2 - Para compilar angular
--> /frontend npm install
-->/frontend/ ng server
--> /frontend ng build
Copiar dist en /backend/static/*


## Consigna ##
Dado el conjunto de datos detallado anteriormente, desarrolle y responda los siguientes puntos:
1. Qu ́e tipo de pre-procesamiento realizar ́ıa sobre los datos? C ́omo manejar ́ıa, por ejemplo, los valores de los pixels? Hay otros casos que deben ser  re-procesados? El pre-procesamiento de los datos var ́ıa dependiendo el m ́etodo a utilizar?
2. Se encuentra el conjunto de datos balanceados por clases?
3. Desarrolle un predictor que indique el label con X entrada. Se trata de una regresi ́on o clasificaci ́on?
4. Compare tres m ́etodos distintos de predictores (entre ellos una red neuronal obligatoria, esta puede o no ser convolucionada, los otros dos a elecci ́on de los alumnos). Qu ́e m ́etricas utiliz ́o para esta comparaci ́on? Cu ́al m ́etodo fue seleccionado?, justifique su elecci ́on (tiempo de modelado, performance, tiempo de entrenamiento, precisi ́on, capacidad de generalizaci ́on, exactitud, etc.)
5. Que visualizaciones utilizar ́ıa para verificar sus modelos?
6. Cu ́ales son los pixels m ́as importantes a la hora de decidir la etiqueta correspondiente? Vea de forma gr ́afica al menos tres de las clases de ropa.
7. Que uso le dar ́ıa al predictor desarrollado?
8. Desarrolle interfaz web que utilizar ́ıa el cliente para cargar nuevos elementos, que resultados se le mostrar ́ıa al cliente?