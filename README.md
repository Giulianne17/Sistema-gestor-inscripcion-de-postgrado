# Proyecto: Ingenieria de Software I
## Desarrollo de gestor de materias de cursos de Postgrado

El presente trabajo consiste en el desarrollo de un sistema gestor de inscripción de cursos de postgrado, utilizando solamente el framework Django. Las especificaciones de los diferentes sprints del proyecto, entre su implementación, casos de uso, distrubición de tareas, y otros detalles, pueden encontrarse en [la carpeta de documentación](https://github.com/Giulianne17/Coordinacion-de-computacion-API/tree/master/Documentacion).

No fueron usadas librerias para las vistas ni autenticación. En su mayoría el proyecto fue desarrollado por el equipo de trabajo.

### Autores:

* Manuel Rodriguez (13-11223@usb.ve)
* Giulianne Tavano (13-11389@usb.ve)
* Angelica Acosta (14-10005@usb.ve)
* Aurivan Castro (14-10205@usb.ve)
* Ian Goldberg (14-10406@usb.ve)
* Elvin Quero (14-10869@usb.ve)
* Sandra Vera (14-11130@usb.ve)

## Ejecución del proyecto

### Preparación previa

Antes que nada, entre en el directorio correspondiente:

```Bash
cd ProyectoSoftware/
```

Para ejecutar el proyecto de manera correcta, necesita las librerías correspondientes. Para instalarlas use el siguiente comando:

```Bash
pip3 install -r requirements
```

Antes de ejecutar el servidor, asegúrece de haber creado la base de datos con los elementos predefinidos. Para ello, ejecute:

```Bash
./migrates.sh
```

## Ejecutar

Finalmente, para ejecutar el servidor:

```Bash
python3 manage.py runserver
```
