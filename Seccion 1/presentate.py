x = input("tu nombre: ")
y = input("edad: ")
z = input("ciudad: ")
print("hola " + x + " tienes " + y + " años y eres de " + z)

#Recuperar un caracter de una cadena
cadena = "Hola mundo" #tambien se puede entre comillas simples
#cadena[1] = "O" #Daría error, no deja cambiar los caracteres de una cadena ya que estas son inmutables
caracter1 = cadena[0]
print(caracter1)

nombre = "carlos"
edad = 22
mensaje = f"Hola me llamo {nombre} y tengo {edad} años"
print(mensaje.upper()) #.lower() -> minusculas  .strip() -> elimina los espacios al principio y al final
mensaje2 = "Hola me llamo {} y tengo {} años".format("carlos",22)
print(mensaje2)
largo_cadena = len(mensaje2) #Muestra cuantos caracteres tiene la cadena
print("caracteres en la cadena = " + largo_cadena)

cadena2 = "Me gusta jugar al movil"
indice = cadena2.find("al")  # Dice en que posicion se encuentra la primera palabra movil (18)
print(indice)
reemplazo = cadena2.replace("movil","pc") #Reemplazo la palabra movil por pc
print(reemplazo)

#MULTIPLICACION DE CADENAS
texto = "hola "
veces = 5
resultado = texto * veces
print(resultado)


print("***GENERADOR DE EMAILS***") # Resultado debe ser carlos.primo.rico@gmail.com
nombre = "Carlos Primo Rico"
empresa = "gmail"
dominio = ".com"
nombre = nombre.lower()
nombre = nombre.replace(" ",".")
print(nombre + "@" + empresa + dominio)


#CARACTERES ESPECIALES
#Para hacer un salto de linea \n
#Para tabular \t  EJ de 2 tabulaciones: print("\t\t Pyton es genial")
#Para añadir comillas dobles o simples en una cadena \' o \"
#Para añadir una barra invertida \\