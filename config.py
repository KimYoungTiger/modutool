import os

file_path = os.path.abspath(os.getcwd())+"\contents.db"

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'default-secret-key')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + file_path
    SQLALCHEMY_TRACK_MODIFICATIONS = False
