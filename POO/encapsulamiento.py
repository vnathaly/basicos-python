#Encapsulamiento
#Ocultar atributos de forma superficial
class Cliente:
  def __init__(self):
    #Con la __ ya lo encapsulo
    self.__codigo = 4321
  def __cuenta(self):
    print('Cuenta de procesamiento')
  #Para llamar los metodos encapsulados
  def getcodigo(self):
    return self.__codigo

#objeto._nombre de la clase_nombre del atributo
persona = Cliente()
print(persona._Cliente__codigo)


