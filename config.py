import os.path

basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'storage.db')
# SQLALCHEMY_DATABASE_URI= 'postgres+psycopg2://postgres:teste123@localhost:5432/orcamentoDB'
SQLALCHEMY_TRACK_MODIFICATIONS = True
SECRET_KEY = "SIDOFAOSFOASADJ"