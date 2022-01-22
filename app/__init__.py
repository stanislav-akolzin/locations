from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import config


app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config')
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{config.USER_NAME}:{config.USER_PASSWORD}@localhost/{config.BASE_NAME}'
db = SQLAlchemy(app)


from .import views
