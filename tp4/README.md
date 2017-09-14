## TP4 DSS Data Mining ##

  - [Consigna](#consigna)
  - [Ejecuta](#Ejecutar)

## Consigna ##
### Mineria de Datos sobre Redes Sociales y sitios Web ###

1. Tomando datos de la red social Twitter, al menos 200 tweets, realice un script que
recolecte, procese y vizualice los datos con las siguientes restricciones:
  - Los tres trends m ́as RT del momento.
  - Listar nombres de usuarios que publicaron con los hashtag de los trends del punto anterior.
  - Cuales son las cinco palabras m ́as utilizadas en los tweets del primer item.
  - Listar los primeros 10 usuarios con mayor cantidad de seguidores.
  - Listar la ubicaci ́on (o en su defecto time-zone) del tweet.
  - Listar los cinco tweets m ́as populares.
  - Listar a los seguidores del autor del tweet m ́as popular.
 
2. Tomando datos de la red Social Google+, recolecte, procese y vizualice los datos con las siguientes restricciones:
  - Obtener las tres  ́ultimas actividades de X usuario.
  - Analizar el texto de una de estas actividades. (Palabras utilizadas, cantidad de veces, etc)

3. Sacando informacion de Microformatos en la Web.
  - Obtener y listar un subconjunto de noticias relevantes usando hNews.
  - Listar calendario de eventos.

### Visualizacion de Datos ###

#### Visualizacion Pasiva ####

1. Adquiera informacion de los seguidores de X usuario en Twitter y realize las siguientes actividades:
  - Clasifique la adquisicion de los datos. De todos los datos, tome el subconjunto de seguidores del usuario X que tengan al menos 10 seguidores
  - Dependiendo de la cantidad de seguidores que tenga Y seguidor, asignele un color.
  - Dependiendo de la cantidad de tweets que tenga Y seguidor, asignele un tama ̃no.
  - Grafique los items anteriores con el mejor tipo de gr ́afico, justique y visualice.

2. Teniendo en cuenta los pasos realizados en el punto anterior (Adquisicion, preparacion,estructuracion pre-visualizacion y visualizacion). Tome n con n mayor a 10 coordenadas geograficas y grafıquelas en un mapa.

#### Visualizacion Activa ####
Utilizando la informacion anterior, agregue la posibilidad de ocultar o mostrar ciertos datos, muestre valores totales y realize filtros (ver info por rango de fecha, cantidad de likes, retweets, si el tweet contiene cierta palabra, etc.)

Links
  - https://demo.bokehplots.com/apps/crossfilter
  - https://demo.bokehplots.com/apps/selection_histogram
  - https://demo.bokehplots.com/apps/movies

## Ejecutar ##

    $ jupter notebook

Para Visualizacion Activa ejecutar servidor bokeh
    $ cd bokeh_server
    $ bokeh serve main.py

  - [http://localhost:5006/main][http://localhost:5006/main]



