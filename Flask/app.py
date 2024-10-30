from flask import Flask, render_template
#'''El parametro de name, es para decirle a la app que esta siendo importada y que sepa exactamente donde buscar los archivos html y dem[as]'''
app = Flask(__name__)

#Esto del @ son decoradores
@app.route("/")
def index():
  name = "Nath"
  num = 2
  return render_template("index.html", name = name, num = num)

@app.route("/contacto")
def contacto():
  return render_template("contacto.html")

