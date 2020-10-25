# Proyecto Walmart API

Para este proyecto, se tomaron las siguientes consideraciones.

* La fuente de datos sera un MongoDB externo al proyecto.
* La DB de Mongo entregara para realizar las pruebas fue integrada el proyecto para ser levantada con el docker de la API al momento de la ejecución del proyecto.
* Por desconocimiento, y no querer pedir mas tiempos, no pude levantar la DB de Mongo en Heroku, pero para suplir esta falencia, levante un DB en MongoCloud con Atlas. Esta DB esta abierta para ser usada con el proyecto en Heroku.
* Se levanto el proyecto de docker en Heroku mediante Gunicorn, y los test corren en github actions.
* Se utilizo la regla de Palindromos que fueran 2 o más caracteres.
* La busqueda minima en texto es de 4 caracteres(en el enunciado decir mayor a 3)
* La API esta expuesta en `https://tranquil-reaches-35249.herokuapp.com/search`


# Correr el proyecto en local

Para la primera vez que se levanta el proyecto se debe realizar con `docker-compose up migration`. Esto levantara el docker de MongoDB y le agregara los datos entregados en el enunciado.

Para levantar la api se debe correr el comando `docker-compose up api`. Esto dejara la API corriendo en la dirección `http://127.0.0.1:8000/search`

Los parametros de entrada de la API son `text` y `page` donde `text` es un string y page es el numero de la pagina a consultar. Si no es un numero valido, siempre sera 1.

# Test

Para realizar test se debe levantar el contenedor con `docker-compose up test`. Este contenedor no necesita de una DB ya que utiliza `mongomock` para realizar las pruebas correspondientes y se agrego una muestra de los datos enviados en el enunciado.

# Variables de entorno

Existen 2 variables de entorno en el proyecto.

Variable | Descripción
------------ | -------------
SECRET_KEY | Es un valor random generado como una semilla para el proyecto de Django.
MONGO_URI | Es el URI de conexión a MongoDB
