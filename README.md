Sistema de Control de Inventario – TECHMEDIUM
Este proyecto consiste en un sistema básico de control de inventario y ventas desarrollado en Python, utilizando la librería Tkinter para la creación de la interfaz gráfica y SQLite como base de datos local. El programa está diseñado para funcionar de manera completamente offline y permite gestionar productos de forma sencilla, rápida y organizada. A través de una interfaz intuitiva, el usuario puede registrar artículos, modificar su información, consultar el inventario en una tabla clara y realizar ventas controlando automáticamente el stock disponible.
El sistema guarda toda la información en una base de datos local, evitando la pérdida de datos y reduciendo errores comunes en el manejo manual del inventario.
•	Interfaz gráfica simple y fácil de usar
•	Base de datos local automática
•	Operación sin conexión a internet
 <img width="533" height="422" alt="image" src="https://github.com/user-attachments/assets/60a1c88b-ec3b-4a42-9903-98d7b10c99b0" />

________________________________________
Proyecto dirigido para
Este programa está dirigido a personas y pequeños negocios que necesitan un control básico y práctico de sus productos sin recurrir a sistemas complejos. Es ideal para tiendas pequeñas, técnicos independientes, talleres, ferreterías o cualquier emprendimiento que maneje inventario y ventas simples. También es adecuado para estudiantes, ya que permite comprender de forma clara el funcionamiento de una base de datos, un sistema de ventas y una interfaz gráfica.
El usuario final no necesita conocimientos técnicos ni de programación, ya que todas las acciones se realizan mediante botones y ventanas emergentes, haciendo que el uso del sistema sea accesible para cualquier persona.
•	Pequeños negocios y emprendimientos
•	Técnicos y talleres independientes
•	Uso educativo y académico
________________________________________
Problema a solucionar
El problema principal que se busca resolver es la falta de un control simple, claro y confiable del inventario en pequeños negocios o proyectos básicos. Muchas personas llevan el control de stock en cuadernos, hojas sueltas o de memoria, lo que genera errores frecuentes como vender productos que ya no existen, no saber cuántas unidades quedan disponibles o perder información importante de los artículos.
Además, sin un sistema organizado resulta difícil consultar rápidamente los productos, actualizar el stock después de una venta o mantener los datos almacenados de forma segura. Este programa soluciona estas dificultades proporcionando una forma estructurada y sencilla de gestionar el inventario sin complicaciones técnicas.
•	Evita ventas con stock insuficiente
•	Reduce errores por control manual
•	Centraliza la información en un solo sistema
________________________________________
Interfaz gráfica
La interfaz gráfica fue desarrollada con Tkinter y está pensada para ser clara y amigable. El programa cuenta con una ventana principal que funciona como menú, desde donde se accede a todas las funciones. Las acciones se realizan mediante ventanas emergentes que solicitan únicamente la información necesaria al usuario.
La tabla de consulta presenta los productos con un formato ordenado, utilizando filas alternadas para mejorar la visualización de los datos.
•	Menú principal con botones
•	Ventanas emergentes para ingreso de datos
•	Tabla con diseño claro y ordenado

<img width="461" height="366" alt="image" src="https://github.com/user-attachments/assets/5af73b42-bf14-4f87-878a-7e57da9efef5" />

<img width="549" height="118" alt="image" src="https://github.com/user-attachments/assets/43dad1f1-1091-4032-8097-987acf2e4394" />

<img width="465" height="186" alt="image" src="https://github.com/user-attachments/assets/4666a089-d554-4e72-aa77-ae63988cf78c" />

________________________________________
Base de datos
El sistema utiliza SQLite como motor de base de datos, lo que permite almacenar la información de forma local sin necesidad de configuraciones adicionales. La base de datos se crea automáticamente al ejecutar el programa por primera vez y se guarda en un archivo llamado productos.db.
La tabla principal almacena el código del producto, su nombre y la cantidad disponible en stock, asegurando que cada producto tenga un identificador único.
•	Base de datos local SQLite
•	Creación automática de la tabla
•	Almacenamiento persistente de datos
 
________________________________________
Ejecución del programa
Para ejecutar el programa es necesario contar con Python 3 instalado en el sistema. No se requieren librerías externas, ya que se utilizan únicamente módulos estándar de Python. Al ejecutar el archivo principal, la base de datos se inicializa automáticamente y el sistema queda listo para su uso.
•	Python 3.x
•	Librerías estándar (Tkinter y SQLite)
•	Ejecución directa del archivo principal
