from flask import Flask, render_template, request, redirect
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

@app.route("/")
def inicio():
	posts = Post.query.order_by(Post.fecha.desc()).all() 
	return render_template("inicio.html", posts=posts)

@app.route("/add")
def add():
	return render_template("add.html")

@app.route("/crear", methods=["POST"])
def crear_post():
	titulo = request.form.get("titulo")
	texto = request.form.get("texto")
	post = Post(titulo=titulo, texto=texto)
	db.session.add(post)
	db.session.commit()
	return redirect("/")

@app.route("/delete", methods=["POST"])
def delete():
	post_id = request.form.get("post_id")
	post = db.session.query(Post).filter(Post.id==post_id).first()
	db.session.delete(post)
	db.session.commit()
	return redirect("/")

if __name__ == "__main__":
	app.run(debug=True)
