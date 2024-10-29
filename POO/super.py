#La funcion super se utiliza para llamar metodos definidos
class Mamifero:
  def __init__(self, nombre):
    print('Es un animal de sangre caliente')

class Leon(Mamifero):
  def __init__(self):
    print('El leon es un animal de cuatro patas')
    super().__init__('Simba')
nuevo_leon = Leon()
