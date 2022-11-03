import os

class Config(object):
	ASSETS_ROOT = os.getenv('ASSETS_ROOT', '/static/assets')