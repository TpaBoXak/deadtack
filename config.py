class Config:
    DB_CONNECTOR = "mariadb+mariadbconnector"
    DB_USER = "root"
    DB_PASSWORD = "12345"
    DB_HOST = "127.0.0.1:3306"
    DB_NAME = "deadtrack"
    SQLALCHEMY_DATABASE_URI = f"{DB_CONNECTOR}://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}?charset=utf8"
    LANGUAGES = ['ru']

    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_ECHO = False
    
    # UPLOAD_FOLDER = os.environ.get('UPLOAD_FOLDER')
    # MAX_CONTENT_LENGTH = int(os.environ.get('MAX_CONTENT_LENGTH'))

