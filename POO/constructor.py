#Atributos

class Persona :
  name = "Leo"
  apellido = "Diaz"
  edad = 22

doctor = Persona()
print( 'Los atributor son: ',getattr(doctor, 'name' , 'edad'))

#Constructores
class Persona :
  pass
  def __init__(self, nombre, edad):
    self.nombre = nombre
    self.edad = edad 
  def descripcion (self):
    return '{} tiene {}'.format(self.nombre, self.edad)
  def comentario (self, frase):
    return '{} dice: {}'.format(self.nombre,frase)

doctor = Persona('Jose', 22)
print(doctor.nombre)
print(doctor.descripcion())
print(doctor.comentario('Hola'))

#Modificar atibutos
class Email ():
  def __init__(self):
    self.enviado = False
  def enviar_correo(self):
    self.enviado = True

mi_correo = Email()
mi_correo.enviar_correo()
print(mi_correo.enviado)
   
