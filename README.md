# App de registro de pagos

## ¿Que hace?

1. Registrar los pagos de condominio de una residencia
2. Mostrar cada uno de los fondos con sus registros que esta residencia posee  

Este es un programa que se realizo como proyecto para el servicio comunitario en la universidad 


## Como usarla o configurla

1. Clona el repositorio o descargalo como zip.

```git clone https://github.com/daniel-canino/app-edificio.git```

2. Instala las dependencias/librerias en requirements.txt

```pip install -r requirements.txt```

3. Ejecuta las migraciones.

```python manage.py makemigrations```
```python manage.py migrate```

4. Crea un superusuario.

```python manage.py createsuperuser```

5. Corre el servidor.
```python manage.py runserver```