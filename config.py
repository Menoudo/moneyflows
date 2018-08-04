import os

basedir = os.path.abspath(os.path.dirname(__file__))


class AppConfig(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'this-really-needs-to-be-changed1'


class ProductionConfig(AppConfig):
    DEBUG = False


class StagingConfig(AppConfig):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(AppConfig):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(AppConfig):
    TESTING = True


class BotConfig(object):
    TELEGRAM_TOKEN = ''
    ACESS_KEY = ''
