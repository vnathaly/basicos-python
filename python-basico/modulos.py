#Librerias, hay 3 tipos de modulos. Los creados por uno mismo, los descargados o los que da el mismo python
#Para usarlos usamos el import seguido por el nombre del modulo
import datetime 

#Los metodos los buscamos en la documentacion, ejemplo con el date.today()
print(datetime.date.today())

#Otra forma es especificar los metodos que voy a utilizar desde un inicio y ya no tendremos que escribir datetime para acceder a sus metodos cada vez
from datetime import timedelta, date

print(date.today())

#----PYPI pagina para sacar modulos----
