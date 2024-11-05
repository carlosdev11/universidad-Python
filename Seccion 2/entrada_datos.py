#CONVERSION DE TIPO DE DATOS

#1.DE CADENA A INT
numero_cadena = "10"
numero_entero = int(numero_cadena)

#2.DE CADENA A FLOAT
numero_cadena = "1.5"
numero_flotante = float(numero_cadena)

#3.DE NUMERO A CADENA
numero = "15"
numero_cadena = str(numero)

#3.CONVERTIR A BOOLEANO
# REGRESA FALSE SI EL NUMERO ES 0 o LA CADENA ESTA VACIA
# REGRESA TRUE SI EL NUMERO NO ES 0 o LA CADENA NO ESTA VACIA
numero = 0
booleano = bool(numero)
print("valor = " + booleano) #devuelve false, si no es 0 devulve true

#CUANDO PIDO UNA ENTRADA DE DATOS POR CONSOLA ENTRA COMO STRING POR LO QUE SI ES UN NUMERO LO TENGO QUE CONVERTIR A INT
edad = int(input("dime tu edad: ")) #De esta forma el numero se guardara como entero
print("Tu edad es: " + edad)
