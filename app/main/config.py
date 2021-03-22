import os
from dotenv import load_dotenv


basedir = os.path.abspath(os.path.dirname(__file__))

DATABASE_URI_DEV = os.getenv('DATABASE_URI_DEV')
DATABASE_URL = os.getenv('DATABASE_URL')


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'my_precious_secret_key')
    DEBUG = False


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = DATABASE_URI_DEV
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    # select inet_server_addr( ), inet_server_port( ); <- to show the ip address of the server and its port
    SQLALCHEMY_DATABASE_URI = DATABASE_URI_DEV
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = DATABASE_URL
    SQLALCHEMY_TRACK_MODIFICATIONS = False


config_by_name = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)

key = Config.SECRET_KEY
