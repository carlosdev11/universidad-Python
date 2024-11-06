#range(inicio,fin,incremento) inicio e incremento opcional
print("secuencia del 0 al 4")
for i in range(5):
    print(i, end=" ")
    

print("\n\nsecuencia del 10 al 20") #el incremento sera de 1 si no se especifica
for i in range(10,21):
    print(i, end=" ")
    
print("\n\nsecuencia del 20 al 30 de dos en dos") 
for i in range(20,31,2):
    print(i, end=" ")
    
print("\n\nRepeticion de un mensaje con range") 
mensaje = input("Introduce el mensaje a repetir ")
numero_repeticiones = int(input("cuantas veces quieres que se repita?"))

for i in range(numero_repeticiones):
    print(f"{i} - {mensaje}")
    
    
print("\n\nEjemplo BREAK ") 
for numero in range(1,10):
    if numero % 2 == 0: #Si el numero es par...
        print(numero) #imprimo el primer numero par y salgo del bucle
        break #salimos del ciclo inmediatamente
    
    
print("\n\nEjemplo CONTINUE") 
for numero in range(1,10):
    if numero % 2 == 1: #Si el numero es impar...
        continue #si es impar continua y vuelve a revisar si es par para imprimirlo
    print(numero) #imprimo los numeros pares