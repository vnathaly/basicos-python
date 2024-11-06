from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

#Este codigo es de practica mas que nada, para saber como funcionan las cosas del ORM a traves de la terminal

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////Users/Nath/Desktop/python/orm/blog.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

app.app_context().push()

class Equipo(db.Model):
	__tablename__ = "posts"
	id = db.Column(db.Integer, primary_key=True)
	nombre = db.Column(db.String, nullable=False)
	fecha = db.Column(db.DateTime, default=datetime.now)

def __repr__(self):
	return "<Equipo %r>" % self.nombre

if __name__ == "__main__":
	app.run(debug=True)
