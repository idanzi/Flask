class Config(object):
    SECRET_KEY = 'DSJFAKL23432UIJDSKLFJADLS'


class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:xixi20080608@localhost:3306/lishiwenhua"


class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:xixi20080608@localhost:3306/lishiwenhua"
    # SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True  # SQLALCHEMY_TRACK_MODIFICATIONS 添加后警告不显示
