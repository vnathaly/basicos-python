#La posibilidad de que una sub clase cuente con metodos con el mismo nombre y la clase superior defina comportamientos diferentes
class Auto:
  rueda = 4
  def desplazamiento(self):
    print('The car is runing with four ruedas')

class Moto:
  rueda = 2
  def desplazamiento(self):
    print('The motocycle is runing sobre two ruedas')

#-------Polimorfismo---------
#Mismo nombre pero diferentes funciones
class Animal:
  def __init__(self, nombre):
    self.nombre = nombre
  def tipo_animal(self):
    pass

class Leon(Animal):
  def tipo_animal(self):
    print('Animal salvaje')

class Perro(Animal):
  def tipo_animal(self):
    print('Animal domestico')

nuevo_animal = Leon('Simba')
nuevo_animal.tipo_animal()