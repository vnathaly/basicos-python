#Herencia de clases
class Pokemon:
  pass
  def __init__(self, nombre, tipo):
    self.nombre = nombre
    self.tipo = tipo
  def descripcion(self):
    return '{} es un pokemon de tipo {}'.format(self.nombre, self.tipo)
  
class Pikachu(Pokemon):
  def ataque(self, tipo_ataque):
    return 'El pokemon {} tiene el atque de {}'.format(self.nombre, tipo_ataque)

class Charmander(Pokemon):
  def ataque(self, tipo_ataque):
    return 'El pokemon {} tiene el atque de {}'.format(self.nombre, tipo_ataque)

nuevo_pokemon = Pikachu('boby','electrico')
print(nuevo_pokemon.descripcion())
print(nuevo_pokemon.ataque('impacto trueno'))

#Parte practica, ejercicios
class Calculadora:
  '''Parte practic hjhgjhga, ejercicios'''
  def __init__(self, numero):
    self.num = numero
    self.datos = [0 for i in range(numero)] #Estoy limitando el numero de veces que se puede realizar
  def ingresar_dato (self):
    self.datos = [int(input('Ingresar datos')) for i in range(self.num)] #Los datos seran ingresados y guardados, el bucle me pone a correr los datos hasta que sea n
class Op_basicas (Calculadora):
  def __init__(self):
    Calculadora.__init__(self,2) #Le digo que al llamar la clase padre solo puede usar dos valore
  def suma(self):
    a,b = self.datos
    s = a + b
    print('El resultado es ', s)
  def resta(self):
    a,b = self.datos
    r = a - b
    print('El resultado es ', r)

class Raiz(Calculadora):
  pass
  def __init__(self):
    Calculadora.__init__(self, 1)

  def raiz_cuadrada (self):
    import math
    a = self.datos
    print('El resultado es ',math.sqrt(a))

ejemplo = Op_basicas()
print(isinstance(ejemplo,Op_basicas)) #Confirmar que operacion se esta relaizando


