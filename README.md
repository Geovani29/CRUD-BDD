# CRUD en Base de datos No Relacional MongoDB


## Descripción

Este proyecto tiene como objetivo principal desarrollar un sistema de gestión de datos basado en una base de datos No Relacional MongoDB. Se implementan las operaciones CRUD (Crear, Leer, Actualizar, Eliminar) para interactuar con los datos almacenados en la base de datos.

## Objetivos

- Implementar operaciones CRUD en una base de datos No Relacional MongoDB.
- Desarrollar un sistema de gestión de datos utilizando Python Flask.
- Practicar el diseño y desarrollo de aplicaciones web utilizando tecnologías modernas.

## Tecnologías Utilizadas

El proyecto hace uso de las siguientes tecnologías:

- ![Python](https://img.shields.io/badge/-Python-3776AB?logo=python&logoColor=white&style=flat-square)
- ![Flask](https://img.shields.io/badge/-Flask-000000?logo=flask&logoColor=white&style=flat-square)
- ![JavaScript](https://img.shields.io/badge/-JavaScript-F7DF1E?logo=javascript&logoColor=black&style=flat-square)
- ![HTML5](https://img.shields.io/badge/-HTML5-E34F26?logo=html5&logoColor=white&style=flat-square)
- ![CSS3](https://img.shields.io/badge/-CSS3-1572B6?logo=css3&logoColor=white&style=flat-square)

## Ejecución del Código

Para ejecutar este proyecto en tu máquina local, sigue estos pasos:

1. **Instalación de Python:**
    - Si aún no tienes Python instalado en tu sistema, puedes descargarlo e instalarlo desde el sitio web oficial de Python: [Descargar Python](https://www.python.org/downloads/).
    - Asegúrate de agregar Python a tu variable de entorno PATH durante la instalación.

2. **Instalación de Flask:**
    - Una vez que Python esté instalado, abre una terminal y ejecuta el siguiente comando para instalar Flask:
    ```
    pip install Flask
    ```

3. **Instalación de MongoDB:**
    - Si aún no tienes MongoDB instalado en tu sistema, puedes descargarlo e instalarlo desde el sitio web oficial de MongoDB: [Descargar MongoDB](https://www.mongodb.com/try/download/community).
    - Sigue las instrucciones de instalación específicas para tu sistema operativo.

4. **Importación de datos de la base de datos:**
    - Antes de ejecutar la aplicación, asegúrate de tener una instancia de MongoDB en ejecución en tu sistema.
    - Utiliza el archivo `Script biblioteca CRUD.txt` proporcionado para importar los datos de la base de datos. Puedes hacerlo ejecutando el siguiente comando en la terminal:
    ```
    mongo < Script biblioteca CRUD.txt
    ```
    Esto importará los datos en tu instancia de MongoDB y preparará la base de datos para su uso con la aplicación.

5. **Clonación del repositorio y ejecución de la aplicación:**
    - Clona el repositorio en tu máquina local utilizando el siguiente comando:
    ```
    git clone <URL_del_repositorio>
    ```
    Reemplaza `<URL_del_repositorio>` con la URL del repositorio de GitHub.
    - Navega hasta el directorio del proyecto y sigue los pasos mencionados en la sección anterior para instalar las dependencias y ejecutar la aplicación Flask.

6. **Acceso a la aplicación:**
    - Una vez que la aplicación esté en funcionamiento, abre tu navegador web y visita `http://localhost:5000` para acceder a la aplicación y probarla con los datos importados de la base de datos MongoDB.
