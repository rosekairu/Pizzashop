import os


class Config:
    """Main configurations class"""

    # SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get("SECRET_KEY")
    UPLOADED_PHOTOS_DEST = 'app/static/photos'
    
    AIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    
    SUBJECT_PREFIX = 'Pizza'
    SENDER_EMAIL = 'janedoe@gmail.com'

    # simple mde  configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True
    @staticmethod
    def init_app(app):
        pass

class ProdConfig(Config):
    """Production configuration class that inherits from the main configurations class"""
    # SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://jane:doejane@localhost/pizzashop'


class DevConfig(Config):
    """Configuration class for development stage of the app"""
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://jane:doejane@localhost/pizzashop'
    DEBUG = True


config_options = {
    'development': DevConfig,
    'production': ProdConfig
}