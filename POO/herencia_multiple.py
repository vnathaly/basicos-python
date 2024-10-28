#Herencia de multplices clases
class Telefono:
  def __init__(self):
    pass
  def llamar(self):
    print('Llamando...')
  def ocupado(self):
    print('Ocupado...')

class Camara:
  def __init__(self):
    pass
  def Fotografia(self):
    print('Tomando fotos...')

class Reproduccion:
  def __init__(self):
    pass
  def fotografia(self):
    print('Reproduciendo fotos...')


class Smartphone(Telefono, Camara, Reproduccion):
  def _del_(self): #Con este metodo podemos utilizar las subsclases directamente eliminando la clas en este casoi 'smarthphone'
    #Entonces dentro de smartphone no haremos metodos para el como tal sino que nos ayudara a unir las otras clases
    print('Telefono apagado')

#Ahora simplemente estaremos llamando a la clase padre y de ahi podemos usar cualquier metodos de sus clases hijos, optimizando el codigo y su ejecucion
movil = Smartphone()
print(movil.llamar())
