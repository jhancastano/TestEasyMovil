# TestEasyMovil
## Crear base de datos en postgresl y configurar archivo local_setting.py
```python
DATABASES = {
    'default':{
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'dbtestEasyMovil',#nombre base de datos creada
        'USER': 'postgres',
        'PASSWORD': '123456', #password base de datos
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

```
### Crear virtualenv 
```
virtualenv envEasyMovil --python=python3
```
### Inicializar entorno virtual
```
source envEasyMovil/bin/activate  
```
### Copiar repositorio
```
git clone https://github.com/jhancastano/TestEasyMovil.git
``` 
### Instalar dependecias
```
pip install -r requirements.txt
```

#### Crear migraciones y un superusuario
``` 
python manage.py migrate
python manage.py createsuperuser 
python manage.py runserver
```


luego de crear super usuario para gestionar usuarios abrir localhost:8000/admin 


obtener el token http://localhost:8000/api/token/