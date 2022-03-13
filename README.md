# Django Shop

Simple shop with Django!


# Tools
- Django 4
- PostgreSQL


#
# How to Run Project

## Download Codes
```
git clone https://github.com/dori-dev/django-shop.git
```
```
cd django-shop
```

## Build Virtual Environment
```
python3 -m venv env
```
```
source env/bin/activate
```

## Install Project Requirements
```
pip install -r requirements.txt
```

## Setup PostgreSQL
Create `shop` Database in PostgreSQL and change `USER` `PASSWORD` `HOST` in the `shop/setting.py`


## Migrate Models
```
python manage.py makemigrations orderapp
```
```
python manage.py migrate
```

## Add Super User
```
python manage.py createsuperuser
```

## Run Codes
```
python manage.py runserver
```

## Open On Browser
Go to admin page and create `customer`, `product` and `order`!
<br>
[127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)

#
## Links


Download Source Code: [Click Here](https://github.com/dori-dev/django-shop/archive/refs/heads/master.zip)

My Github Account: [Click Here](https://github.com/dori-dev/)


