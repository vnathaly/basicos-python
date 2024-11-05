from flask import Flask, render_template, request, redirect

app = Flask(__name__)
tareas = []

@app.route("/")
def home():
  return render_template("index.html", tareas = tareas)

@app.route('/add', methods=['GET', 'POST'])
def add():
  if request.method == 'GET':
   return(render_template("add.html"))
  else:
    tarea = request.form.get('tarea')
    tareas.append(tarea)
    return redirect('/')
