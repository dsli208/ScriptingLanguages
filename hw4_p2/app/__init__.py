from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config.update(dict(
    SECRET_KEY="powerful secretkey",
    WTF_CSRF_SECRET_KEY="a csrf secret key"
))
app.secret_key = 'dont tell anyone'
from app import routes, models, forms
