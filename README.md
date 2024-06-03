# Aplicación de demostración de introducción a microservicios en Python

Esta es una aplicación diseñada para el curso de iniciación a Microservicios.

Vamos a hacer una calculadora y vamos a ir construyendo las diferentes piezas de lo que, incialmente era un monolito, en formato microservicios.

Luego de la toma de requisitos vemos que es necesario lo siguiente:

* Microservicio para sumar
* Microservicio para restar
* Microservicio para multiplicar
* Microservicio para dividir
* Microservicio para la interfaz gráfica
* Que utilice un bus de mensajería para comunicarse entre los microservicios

* Que todo se despliegue en Azure con:
    * Queues de una Storage Account
    * Functions Apps
    * Static App

## Las pruebas no son opcionales
* Cada microservicio debe tener su batería de pruebas, al menos una de que funciona correctamente, y se deben poder lanzar todas desde el directorio raiz con el comando ***pytest***

## Prerequisitos
* Cuenta de Azure
* Tener instalado Flask
* Tener instalado PyTest

### Disclamer
Este no es un proyecto para enseñar Programación orientada a objetos o Python. El objetivo es iniciarse en las arquitecturas de Microservicios, y por ello no se ha buscado la excelencia en la codificación. Si ves errores garrafales o mejoras que no confundan al que se está iniciando, no dudes en hacer un Pull Request o abrir una Issue.
