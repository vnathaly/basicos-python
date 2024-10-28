#----Funciones Python----
def hello():
  print("Hello Word")

hello()

def hey(n):
  print("Hello Word " + n)

hey("Nath")

#Funciones mas cortas con lambda
add = lambda num1, num2: num1 + num2

print(add(5, 7))
