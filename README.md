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



``` 
python manage.py migrate
python manage.py createsuperuser 
```