# eShopPrices
Nintendo eShop Game Prices

## Installation
```
pip install -r requirements.txt
```
## Configuration
Modify 'config.py' file:

change 'SQLALCHEMY_DATABASE_URI' value to server path

## Run Local
```
python manage.run runserver
```

## Run on Server
Gunicorn must be installed in the linux server
```
nohup gunicorn manage:app -b 0.0.0.0:80 &
```

## Reload App
Upload new app files and run:
```
kill -HUP [pid]
```
[pid] is the pid of the app process

