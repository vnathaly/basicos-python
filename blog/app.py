from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////Users/Nath/Desktop/python/blog/blog.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

app.app_context().push()

class Post(db.Model):
  __tablename__ = "posts"
  id = db.Column(db.Integer, primary_key=True)
  titulo = db.Column(db.String, nullable=False)
  fecha = db.Column(db.DateTime, default=datetime.now)
  texto = db.Column(db.String, nullable=False)


