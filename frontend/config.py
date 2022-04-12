import os

ENDPOINT = os.environ['ENDPOINT']
APP_HOST = os.environ['APP_HOST']
APP_PORT = int(os.getenv('APP_PORT', '5000'))

SECRET_KEY = os.environ['SECRET_KEY']
