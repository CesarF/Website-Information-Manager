# Manejador de información de sitios web

Inicia el proyecto para manejar la información de los sitios web. Vamos!!!!

## Instalación

* Instalar python 3 (el más reciente), las últimas versiones ya vienen con pip para el manejo de paquetes.
* Verifique la versión de python por medio del comando
```
python -m django --version
```
* En el caso que no reconozca el comando python, debe agregar la ruta donde se instaló el python al PATH
* Instalar django y las librerías necesarias. Para ello ubíquese en la carpeta del proyecto y ejecute
```
pip install -r requeriments.txt
```
* Crear la base de datos. Solo en caso que no esté usando la misma base de datos sqlite presente en el proyecto
* Ejecutar el migrate para que se creen las tablas o se actualice la base de datos con los nuevos cambios
```
python manage.py migrate
```

## Ejecución

* Ejecute la aplicación (desde la carpeta del proyecto)
```
python manage.py runserver
```
