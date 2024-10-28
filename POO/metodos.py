class Matematica:
  def suma (sielf):
    sielf.n1 = 2
    sielf.n2 = 3

s = Matematica()

s.suma()
print(s.n1 + s.n2)

#Mejor forma de realizarlo
#El init ayuda a inicializar cualquier propiedad
class Ropa :
  def __init__(self):
    self.marca = "Onda Civic"
    self.talla = "2A"
    self.color = "Blue"

camisa = Ropa()
print(camisa.marca)
print(camisa.color)
print(camisa.talla)

#Vamos a hacer una calculadora y declarar variables en clases
class Calculadora :
  def __init__(self, n1, n2):
    self.suma = n1 + n2
    self.resta = n1 - n2
    self.producto = n1 * n2
    self.division = n1/n2

operacion = Calculadora(3, 5)
print(operacion.suma)
print(operacion.resta)
print(operacion.producto)
print(operacion.division)

