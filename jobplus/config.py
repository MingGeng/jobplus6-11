class BaseConfig(object):
    SECRET_KEY = 'secret key'
    INDEX_PER_PAGE = 9

class DevelopmentConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqldb://root@localhost:3306/jobplus?charset=utf8'

class ProductionConfig(BaseConfig):
    pass

class TestingConfig(BaseConfig):
    pass

configs = {
        'development': DevelopmentConfig,
        'production': ProductionConfig,
        'testing': TestingConfig
        }
