#Clases y Objetos

class Jugador_1 :
  name = "Rigoerto"
  age = 22

class Jugador_2 :
  name = "Pancho"
  age = 23

print(Jugador_1.name)

#Clases sin valores

class Person :
  pass

victoria = Person()
maria = Person()

victoria.edad = 20
victoria.name = "victoria"
victoria.statura = 5.6

maria.edad = 20
maria.apellido = "Cruz"
maria.name = "Maria"
maria.statura = 5.7

print(maria.edad)
print(victoria.name)
