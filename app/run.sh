#!/bin/bash

sleep 6
python manage.py migrate

gunicorn --bind 0.0.0.0:8080 project.wsgi