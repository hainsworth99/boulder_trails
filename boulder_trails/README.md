## Dependencies
- python 3.8.5
- django 3.1.4 - a python-based web framework 
- PostgreSQL 13.1 - a open-source relational database management system
- PostGIS 3.0 - a postgres extension enabling geographic objects and queries


## Database Setup
After successful installation of PostgreSQL and PostGIS, run the following to setup the database and create a user:
- Login to PostgreSQL as root user by running `> psql -U root_username`
- Create new database for the project with `root_username=# CREATE DATABASE boulder_trails;`
- Switch to new database and add PostGIS extension with `root_username=# \c boulder_trails` and `boulder_trails=# CREATE EXTENSION postgis;`
- Create new user to connect to database via django with `boulder_trails=# CREATE USER trail_manager PASSWORD XXXXXXXX;`
- Configure database settings in `boulder_trails/boulder_trails/settings.py` so django can connect to database:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'boulder_trails',
        'USER': 'trail_manager',
        'PASSWORD': 'XXXXXXXXXXX',
        'HOST': '127.0.0.1',  # host database is running on
        'PORT': '5432',  # port num database is accepting connections on 
    },
}
```
- Make migrations to the database by running the following commands
    - `python manage.py makemigrations`
    - `python manage.py migrate` 
- In a text editor, open `boulder_trails/data_load.py` and update `jsonPATH` to the absolute URI of `OSMP_Trails.geojson`
- Run the following command to load trail data into database 
    - `python manage.py shell < OSMP_Trails.py`