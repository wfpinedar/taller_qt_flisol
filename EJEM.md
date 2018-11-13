Buenas tardes compañeros,

Como parte de los compromisos en la reunión de desarrolladores este es un
ejemplo de como realizar el "hello world" usando gitpich para hacer
presentaciones.

1. No es necesario el login para hacer presentaciones, lo único que se requiere
es crear la plantilla, esta se debe llamar PITCHME.md, similar al ya conocido
README.md de los repositorios

2. Crear los Slides teniendo en cuenta lo siguiente:

Separador slides horizontal:
```
---
```
Separador slides vertical:
```
+++
```
* El resto de elementos (links, imágenes, código, etc.) son similares al
README.md dado que es MarkDown.

3. Luego de tener creado el elemento PITCHME.md apuntamos gitpitch a la
ubicación de este siguiendo el patrón como se ve a continuación:
```
https://gitpitch.com/$user/$repo/$branch
```
4. Para finalizar se muestra un ejemplo con un repo existente:

![Repo ejemplo](https://github.com/wfpinedar/taller_qt_flisol)

Para el cual la presentación resultante fue la siguiente:

![](https://gitpitch.com/wfpinedar/taller_qt_flisol)
