#import random
from random import randint

#Generar numero aleatorio entre 1 y 10
numero = randint(1,10)
#numero = random.randint(1,10) DE ESTA FORMA SERIA SI SOLO IMPORTO EL MODULO RANDOM
print("el numero aleatorio es: " + numero)

#Simular un dado de 6 caras
dado = randint(1,6)
print("Resultado a lanzar el dado: " + dado)

#GENERADOR DE ID UNICO (el resultado debe ser las 2 primeras del nombre y apellido en mayusculas, los 2 ultimos del año y 4 aleatorios)
nombre = input("Introduce tu nombre: ")
apellido = input("Introduce tu primer apellido: ")
year = input("Introduce tu año de nacimiento (YYYY): ")

nombre2 = nombre.strip().upper()[0:2]
apellido2 = apellido.strip().upper()[0:2]
year2 = year.strip()[2:4] #[2:] Recupera hasta el ultimo caracter de la cadena
numeros_aleatorios = randint(1000,9999)

print("Tu ID único generado es: " + nombre2 + apellido2 + year2 + str(numeros_aleatorios)) #RESULTADO = CAPR027495