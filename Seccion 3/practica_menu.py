print("Menu para administrar cuentas")

salir = False
while salir == False:
    print('''MENU: 
    1- Crear Cuenta
    2- Eliminar cuenta
    3- Salir''')
    opcion = int(input("selecciona una opción: "))
    if opcion == 1:
        print("creando cuenta...\n")
    elif opcion == 2:
        print("eliminando cuenta...\n")
    elif opcion == 3:
        print("has salido del programa")
        salir = True
    else:
        print("opcion no valida, introduzca de nuevo\n")
    #elif opcion <= 0 or opcion > 3:
    #    print("opcion no valida, introduzca de nuevo")
        