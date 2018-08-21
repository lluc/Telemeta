#!/bin/bash

# paths
app='/srv/app'
manage=$app'/manage.py'
wsgi=$app'/wsgi.py'

# stating apps
pip install -U django==1.8.18
pip uninstall -y south
# pip install django-environ redis
pip install -e git+https://github.com/Parisson/django-jqchat.git@dj1.8#egg=django-jqchat
pip install django-debug-toolbar==1.6
pip install -e git+https://github.com/Parisson/saved_searches.git@dj1.8#egg=saved_searches-2.0.0-beta
pip install django_select2==5.11.1 lxml django-leaflet django-geojson django-markdownx 

# waiting for other services
bash $app/scripts/wait.sh

# Starting celery worker with the --autoreload option will enable the worker to watch for file system changes
# This is an experimental feature intended for use in development only
# see http://celery.readthedocs.org/en/latest/userguide/workers.html#autoreloading
python $manage celery worker --autoreload -A worker
