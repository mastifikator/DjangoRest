#!/bin/bash
service nginx start
gunicorn  -b 0.0.0.0:8003 front.wsgi:application
exec "$@"