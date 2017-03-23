Proyect Upload / Download file
==============================

Proyecto para carga y descarga de arhivos.

Las configuracion se realiza para un entorno linux .


## instalar modulo node

Ubicarse en el la carptea __socketioupload__ e instalar modulos

	$ cd socketioupload
	$ npm install
	$ cd app
	$ npm install

Cambiar la configuracion del __docker-compose.yml__  la ruta del volumen  carga de archivos **/Users/Edumar/OSCE/2017/UPLOAD/fuentes/uploadnode/uploads** por una ruta local absoluta

compilar y levantar la aplicacion con docker-compose

	$ docker-compose up --build 
	 

Cargar la aplicacion

```
http://localhost:800
```

Para parar la apliacion 

	$ docker-compose stop

Para levantar la aplicacion en modo servicio
	
	$ docker-compose up -d
	
Para esclar la aplicacion con cuatro contenedores balanceados

	$ docker-compose scale web=4
	
verificamos los contenedores levantados

	$ docker-compose ps 