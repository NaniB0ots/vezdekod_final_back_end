#!/bin/bash

sleep 3
python manage.py migrate

gunicorn --bind 0.0.0.0:8080 project.wsgi