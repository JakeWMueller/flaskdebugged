import os
from dotenv import load_dotenv
basedir = os.path.abspath(os.path.dirname(__file__))

# Windows = Documents\codingtemple-may2020\week5\in-class\
# Mac & Linux = Documents/codingtemple-may2020/week5/in-class/

class Config():
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you will never guess...'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite://' + os.path.join(basedir,'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    DEBUG = False
    SECRET_KEY = "9asdf8980as8df9809sf6a6ds4f3435fa64ˆGggd76HSD57hsˆSDnb"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    ENV = "development"
    DEVELOPMENT = True
    SECRET_KEY = "secret_for_test_environment"
    OAUTHLIB_INSECURE_TRANSPORT = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
