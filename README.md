# ProyectoSoftware

Antes que nada, entre en el directorio correspondiente:
`cd ProyectoSoftware/`

Para ejecutar el proyecto de manera correcta, necesita las librerías correspondientes. Para instalarlas use el siguiente comando:
`pip3 install -r requirements`

Antes de ejecutar el servidor, asegúrece de haber creado la base de datos con los elementos predefinidos. Para ello, ejecute:
`./migrates.sh`

Finalmente, para ejecutar el servidor:
`python3 manage.py runserver`
