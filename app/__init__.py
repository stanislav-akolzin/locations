from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os


app = Flask(__name__, instance_relative_config=True)

user_name = os.environ.get('USER_NAME')
user_password = os.environ.get('USER_PASSWORD')
base_name = os.environ.get('BASE_NAME')
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{user_name}:{user_password}@localhost:5433/{base_name}'
db = SQLAlchemy(app)


from .import views
