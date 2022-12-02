<h1 align="center"> FINANZAS A LA MANO </h1>

<p align="center">
<img src="https://img.shields.io/badge/STATUS-EN%20DESAROLLO-green">
</p>

## 🛠️ Abre y ejecuta el proyecto

Posterior a descargar el proyecto cree la base de datos en postgresql posterior a esto en un archivo con nombre ".env" en la misma ubicación del main y agregue las siguientes lineas de codigo:

- `DB_NAME = "Nombre de la base de datos"`
- `DB_USER = "Usuario de postgresql"`
- `DB_PASS = "Clave de postgresql"`
- `DB_HOST = "Host de postgresql"`
- `DB_PORT = "Puerto de postgresql"`

Por su seguridad agregue a `.env` a su `.gitignore` esto con el fin de no compartir sus datos personales 

Posterior a esto ejecute los siguientes comandos que crearan las tablas dentro de la base se datos:

- `from app.v1.scripts.create_tables import create_tables`
- `create_tables()`

## :hammer:Funcionalidades del proyecto

- `Funcionalidad 1`: descripción de la funcionalidad 1- 
- `Funcionalidad 2`: descripción de la funcionalidad 2- 
- `Funcionalidad 2a`: descripción de la funcionalidade 2a relacionada con la funcionalidad 2- 
- `Funcionalidad 3`: descripción de la funcionalidad 3

Planteamiento del problema.

La vida cotidiana ha tenido una transformación increíble durante el siglo XXI, siendo los avances tecnológicos uno de los grandes protagonistas de esta transformación, pues no es para nadie un secreto que en la vida cotidiana actual nos vemos (una gran cantidad de personas) obligados a utilizar dispositivos tecnológicos que sirven de herramientas para permitirnos una interacción mucho más rápida con un mundo globalizado y para acceder a las múltiples herramientas que este brinda. Así con la facilidad de poder llegar de manera más rápida y fácil a un publico en constante crecimiento, las estrategias de marketing y de publicidad de grandes, medianas y pequeñas marcas se ven interesadas en ofrecer la mayor cantidad de productos e impactar de manera considerable en su público objetivo y nosotros como potenciales consumidores muchas veces sucumbimos a estás estrategias y podemos en muchas ocasiones hacer un mal uso de nuestras finanzas personales y llegar a fin de mes con bastantes preocupaciones. 

Es así como surge Finanzas a la mano ,una API que está interesada en ayudar y facilitar a las personas las cuentas mes a mes, teniendo dentro de sus herramientas gastos fijos (que están establecidos por las personas y que pueden ser como: arriendo, servicios públicos, servicios con entidades de telefonía, servicios de cable, metro u otros medios de transporte, créditos, deudas e hipotecas entre otros gastos) y unos “gastos hormiga” que se espera la persona a medida que hace uso del dinero sobrante de los gastos fijos los vaya incluyendo en la API y así poder saber con exactitud en que se van sus gastos mes a mes.

El objetivo de Finanzas a la mano es que la gente tenga una buena perspectiva financiera de sus gastos y que puedan ser conscientes de los gastos innecesarios que pueda tener mes a mes para que, de esta manera se pueda ir corrigiendo paulatinamente estos gastos y ver reflejado en sus estados bancarios una mejoría. 

Finanzas a la mano desea generar un impacto significativo en las personas que la usan, y a mediano plazo desea posicionarse como la aplicación más descargada de Colombia, contando además con múltiples reconocimientos por la practicidad de su plataforma y la interacción con los usuarios de todas las edades, como por tener una fuerte política de privacidad con los datos ingresados por los usuarios.

Para resolver estás problemáticas la aplicación cuenta con múltiples entradas, abarcando desde el registro de usuarios (creación de nuevos usuarios), como el log in de usuarios ya registrados. Posteriormente a esto la aplicación cuenta con las opciones de crear, consultar, actualizar y eliminar:

- Actualizar y consultar información de usuarios ya registrados en las bases de datos.
- Ingresos en el mes.
- Gastos que van contemplados: gastos fijos, gastos variables.
- Retiros que se han hecho en mes.

Cada gasto(fijo o variable),ingreso, retiro o usuario cuenta con una tabla independiente creada en SQL, y mediante la programación de la API Finanzas a la mano mediante la librería Fastapi, Peewee, Typing entre otras librerías de Python se hizo la conexión entre archivos .py para poner en marchar la API, y además se hizo la conexión a las bases de datos SQL para almacenar la información(a continuación, se visualiza el esquema). 
  
Finalmente, y para un mejor entendimiento del estado de sus finanzas, el usuario obtendrá una gráfica informativa que puede ser de gran utilidad para interpretar visualmente los números y tomar decisiones asertivas respecto a sus finanzas futuras. 

Nota: Es importante mencionar que para el proyecto se ha creado un entorno virtual para controlar las versiones y las librerías que se han tratado para la construcción de la app y se han llevado a cabo las buenas prácticas de código, además en pro de la comunicación y aporte en el trabajo en equipo se ha implementado un repositorio en git en el cual todos los integrantes del equipo han contribuido a que el proyecto salga a flote. 
