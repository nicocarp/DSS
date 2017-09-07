## TP3 DSS Data Warehouse ##

### Empresa Venta Online de Vinos ###  
Esta empresa necesita que se diseñe un DW para registrar la cantidad y ventas de sus vinos a sus clientes. Parte de la
base de datos actual esta compuesta por las siguientes tablas:

  - CUSTOMER (Code, Name, Address, Phone, BDay, Gender)
  - WINE (Code, Name, Type, Vintage, BottlePrice, CasePrice, Class)
  - CLASS (Code, Name, Region)
  - TIME (TimeStamp, Date, Year)
  - ORDER (Customer, Wine, Time, nrBottles, nrCases)

Estas tablas representan las entidades principales de un ER, por lo que es nece-
sario derivar las relaciones entre ellas para poder diseñar correctamente el DW.

Luego de realizado el diseño del DW realice las siguientes consultas SQL:
  - Muestre porcentajes de tipos de vinos mas vendidos en X año.
  - Cual es la temporada con mayor cantidad de ventas de X vino?
  - Que clientes han realizado mas compras a lo largo de 4 años?


### Inmobiliaria ###
En este caso deseamos darle al Gerente Principal una vista general del
negocio, en terminos de cuales son las propiedades que la inmobiliaria maneja y
el seguimiento del trabajo de cada Agente dentro de la empresa. Nuestra Inmo-
biliaria cuenta con las siguientes tablas en su base de datos.

  - OWNER (IDOwner, Name, Surname, Address, City, Phone)
  - ESTATE (IDEstate, IDOwner, Category, Area, City, Province, Rooms, Bedrooms, Garage, Meters)
  - CUSTOMER (IDCust, Name, Surname, Budget, Address, City, Phone)
  - AGENT (IDAgent, Name, Surname, Office, Address, City, Phone)
  - AGENDA (IDAgent, Data, Hour, IDEstate, ClientName)
  - VISIT (IDEstate,IDAgent, IDCust, Date, Duration)
  - SALE (IDEstate,IDAgent, IDCust, Date, AgreedPrice, Status)
  - RENT (IDEstate,IDAgent, IDCust, Date, Price, Status, Time)

Luego de realizado el diseño del DW realice las siguientes consultas SQL:
  - ¿Que tipo de propiedad se vendio por el precio mas alto con respecto a cada
  - ciudad y meses?
  - ¿Quien ha comprado un piso con el precio mas alto con respecto a cada mes?
  - ¿Cual es la duracion media de visitas en las propiedades de cada categorıa?

### ETL (extract, transform, load) en Python ###

  - Tomar datos de un archivo csv, de json y una db SQL.
  - De los tres DataFrames realizar las siguientes operaciones y mostrar sus re- sultados, join, merge, concat, append, con una clave a eleccion.
  - Guardar en una db SQL, la interseccion de los datos obtenidos en el punto anterior.
