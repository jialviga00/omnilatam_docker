### HOW TO RUN THIS PROJECT

**Note:** The *"manage.py migrate"* and *"manage.py createsuperuser"*  are not required if db.sqlite3 file exists from git clone.

- **WITH DOCKER** *(into folder)*:
```
docker-compose build
docker-compose up -d
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
```

- **WITHOUT DOCKER** *(you should have python 3.8 installed)*
```
cd app
python -m pip install -r requirments.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver 0:1111
```

Now that the servers running, visit http://127.0.0.1:1111/admin with your Web browser

### HOW TO RUN TEST

- **WITH DOCKER**
```
docker-compose exec web python manage.py test
```

- **WITHOUT DOCKER** *(you should have python 3.8 installed)*
```
cd app
python manage.py test
```