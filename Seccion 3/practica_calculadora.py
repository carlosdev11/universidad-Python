print("CALCULADORA")

salir = False
while salir == False:
    print('''Operaciones que puedes realizar: 
    1- Sumar
    2- Restar
    3- Dividir
    4- Multiplicar
    5- Salir''')
    opcion = int(input("Elige una opcion: "))
    valor1 = float(input("Introduce primer valor: "))
    valor2 = float(input("Introduce segundo valor: "))
    if opcion == 1:
        resultado = valor1 + valor2
        print("Resultado = " + resultado)
    elif opcion == 2:
        resultado = valor1 - valor2
        print("Resultado = " + resultado)
    elif opcion == 3:
        resultado = valor1 * valor2
        print("Resultado = " + resultado)
    elif opcion == 4:
        resultado = valor1 / valor2
        print("Resultado = " + resultado)
    elif opcion == 5:
        print("Saliendo del programa...")
        salir = True
    else:
        print("Opcion no valida, introduce de nuevo")