# Definición de una función simple
def saludar():
    print("Hola, bienvenido a Python!")

# Llamada a la función
saludar()  # Resultado: "Hola, bienvenido a Python!"



# Función que recibe un parámetro y lo utiliza
def saludar_persona(nombre):
    print("Hola, " + nombre + "!")

# Llamada a la función pasando un argumento
saludar_persona("Juan")  # Resultado: "Hola, Juan!"
saludar_persona("Ana")   # Resultado: "Hola, Ana!"



# Función que recibe dos números y devuelve su suma
def sumar(a, b):
    return a + b

# Llamada a la función y captura del valor devuelto
resultado = sumar(5, 3)
print("El resultado de la suma es:", resultado)  # Resultado: 8



# Función con parámetro por defecto
def elevar_potencia(base, exponente=2):
    return base ** exponente

# Llamadas a la función
print(elevar_potencia(3, 3))  # Resultado: 27 (3^3)
print(elevar_potencia(4))     # Resultado: 16 (4^2, usa el exponente por defecto)



#------------EJEMPLOS PRACTICOS---------------

#Funcion que calcula el area de un triangulo
def area_rectangulo(base, altura):
    return base * altura

print("El área del rectángulo es:", area_rectangulo(5, 3))  # Resultado: 15



# Función que verifica si un número es par
def es_par(numero):
    return numero % 2 == 0

# Ejemplo de uso
num = 7
if es_par(num):
    print(f"{num} es par")
else:
    print(f"{num} es impar")  # Resultado: "7 es impar"



# Función que cuenta las vocales en una cadena
def contar_vocales(cadena):
    vocales = "aeiouAEIOU"
    contador = 0
    for letra in cadena:
        if letra in vocales:
            contador += 1
    return contador

# Ejemplo de uso
cadena = "Hola Mundo"
print("Número de vocales:", contar_vocales(cadena))  # Resultado: 4
