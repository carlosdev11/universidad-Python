a = 10
b = 3

#Division con numeros flotantes
division = a / b
print(division)

#Division entera (sin decimales)
division_entera = a // b
print(division_entera)

#Resto de la division
resto = a % b
print(resto)

#Exponente
exponente = a ** b #10 elevado a 3 == 10 * 10 *10
print(exponente)

#ASIGNACION MULTIPLE
x,y,z = 2, "hola", -4.3
print(f"x = {x}, y = {y}, z = {z}")

#ASIGNACION ENCADENADA
a = b = c = 10
print(f"a = {a}, b = {b}, c = {c}")

#INTERCAMBIO VALOR DE VARIABLES
x, y = 4,7
x, y = y, x #De esta forma ahora x vale 7 e y vale 4

#Recibir multiples valores de la entra del usuario
nombre, apellido = input("introduce tu nombre y apellido separados por coma: ").split(",") #De esta forma el nombre y el apellido se guardan en sus variables IMPORTANTE separarlos por coma

#OPERADOR DE IGUALDAD ==
#OPERADOR DE DISTINTO !=
#OPERADOR DE MAYOR QUE >
#OPERADOR DE MENOR QUE <
#OPERADOR DE MAYOR O IGUAL QUE >=
#OPERADOR DE MENOR O IGUAL QUE <=

#OPERADORES LOGICOS -> and, or, not


#AUTENTICACION DE USUARIO Y CONTRASEÑA
usuario_correcto = "admin"
contrasena_correcto = 123

user = input("introduce tu usuario: ")
paswd = int(input("introduce contra"))
if user == usuario_correcto and paswd == contrasena_correcto:
    print("datos correctos")
else:
    print("datos incorrectos")
