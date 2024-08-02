import os
from os import environ

class Config(object):

    DEBUG = False
    TESTING = False

    basedir = os.path.abspath(os.path.dirname(__file__))

    SECRET_KEY = 'pianalytix'

    UPLOADS = "/home/username/app/app/static/uploads"

    SESSION_COOKIË_SECURE = True

    DEFAULT_THEME = None


class DevelopmentConfig(Config):
    DEBUG = True
    SESSION_COOKIË_SECURE = False


class DebugConfig(Config):
    DEBUG = False