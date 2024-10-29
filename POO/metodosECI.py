#Un objeto se crea usando el constructor de una clase, una vez creadp se le conoce como instancia.
class Pastel:
  def __init__(self, ingredientes):
    self.ingredientes = ingredientes
  
  def __repr__(self):
    return f'Pastel({self.ingredientes !r})'
  
#Poner elementos dentro de una clase pero que quiero que sean independientes
  @classmethod 
  def Pastel_chocolate(cls):
    return cls(['Harina','leche','huevos','chocolate'])
  @classmethod
  def Pastel_vainilla(cls):
    return cls(['Harina','leche','huevos','vainilla'])

print(Pastel.Pastel_chocolate())

#---------------Metodo estatico---------------
#Pueden ser llamados sin tener una instancia de la clase y no tienen acceso al exterior
import math
class Pastel:
  def __init__(self, ingredientes, rango):
    self.ingredientes = ingredientes
    self.rango = rango
  def __repr__(self):
    return (f'Pastel({self.ingredientes},'f' {self.rango})')
  
  def area(self):
    return self.rango_area(self.rango)
  
  @staticmethod
  def rango_area(A):
    return A ** 2 * math.pi

nuevo_pastel = Pastel(['Harina','leche','huevos','vainilla'],4)
print(nuevo_pastel.rango_area(2))

