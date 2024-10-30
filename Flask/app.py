from flask import Flask, render_template, request
#'''El parametro de name, es para decirle a la app que esta siendo importada y que sepa exactamente donde buscar los archivos html y dem[as]'''
app = Flask(__name__)

@app.route("/")
def home():
  return render_template("index.html")

@app.route("/contacto",  methods=["POST"])
def contacto():
  name = request.form.get("name")
  return render_template("contacto.html", name = name)
