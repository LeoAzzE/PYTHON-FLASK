class DevelopmentConfig():
    DEBUG=True
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = '1234567'
    MYSQL_DB = 'flask-projeto'

config = {
    'development' : DevelopmentConfig
}