import os

class Config:

    FLASK_ENV = 'development'

    ASSETS_ROOT = os.getenv('ASSETS_ROOT', '/static/assets')