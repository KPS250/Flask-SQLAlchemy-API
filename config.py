class Config(object):
    DEBUG = False
    TESTING = False
    SECRET_KEY = '122332'


class ProductionConfig(Config):
    DATABASE_HOST = '127.0.0.1'
    USER = 'admin'
    PASSWORD = 'admin123'
    DATABASE = 'flask_db'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:admin123@localhost:3306/flask_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    DATABASE_HOST = '127.0.0.1'
    USER = 'admin'
    PASSWORD = 'admin123'
    DATABASE = 'flask_db'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:admin123@localhost:3306/flask_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig(Config):
    DATABASE_HOST = '127.0.0.1'
    USER = 'admin'
    PASSWORD = 'admin123'
    DATABASE = 'flask_db'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:admin123@localhost:3306/flask_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
