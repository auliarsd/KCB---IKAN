import os

SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///fishcarelab.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False
