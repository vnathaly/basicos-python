#---------Format % s---------
#Lo utilizamos para concatenar objetos
curso = 'python'
print('Turoriales de % s'%curso)

#Tomar muchisimo en cuenta porque esta es la utilidad inicial y la mas vista
nombre = 'victor'
edad = 22
print('Hola soy, % s y tengo % s de edad.'%(nombre, edad))

#---------Format str.format()----------
nombre = 'victor'
edad = 22
print('Que tal mi nombre es {} y mi edad es {}'.format(nombre, edad))

#---------Format f.format()----------
#Nueva forma, una actualizacion mas reciente y genial
nombre = 'victor'
edad = 22
print(f'Hola soy {nombre} y mi edad es {edad}')

#----------------------------------Ejercicio de ejemplo----------------------------------
class Estudiante:
  def __init__(self, nombre, apellido, edad):
    self.nombre = nombre
    self.apellido = apellido
    self.edad = edad
  def __str__(self): #Se usa para la ejecucion de codigo de forma inmediata e informal
    return (f'Mi nombre es {self.nombre}{self.apellido} y tiene {self.edad}')

nuevo_estudiante = Estudiante('Nathaly', 'Victoriano', 22)
print(f'{nuevo_estudiante}')