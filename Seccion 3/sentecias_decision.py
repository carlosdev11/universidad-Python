#Sentencia if-else
edad = 30
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")
    
#Sentencia elif
'''Se utiliza cuando queremos verificar multiples condiciones, una tras otra.
Todos los que necesite, siempre entre el bloque if-else
'''
edad = 16
if edad >= 18:
   print("Eres mayor de edad") 
elif 13 <= edad < 18:
    print("Eres adolescente")
else:
    print("Eres un niño")
    
#SENTENCIA IF NOT
salir_sistema_txt = input("Deseas salir del sistema? (si/no)")
salir_sistema = salir_sistema_txt.strip().lower() == "si"

if not salir_sistema:
    print("Sigues dentro del sistema")
else:
    print("Has salido del sistema")
    

#OPERADOR TERNARIO
edad = int(input("Introduce tu edad"))
es_adulto = "si" if edad >= 18 else "no"
print("Es adulto??" + es_adulto)
    
  
  
#REVISAR SI UN NUMERO ES POSITIVO
numero = int(input("Introduce un numero para ver si es positivo o negativo"))

if numero > 0:
    print(f"El numero  {numero}  es positivo")
elif numero == 0:
    print(f"El numero {numero} es cero")
else:
    print(f"El numero {numero} es negativo")
    

#RETO SISTEMA DE DESCUENTOS
"""
Si compra mas de 1000€ y es miembro = 10% dto
Si solo es miembro = 5% dto
Si no es miembro ni compra mas de 1000€ = 0%dto
"""
compra_minima = 1000
descuento = 0

precio_compra = float(input("Introduce el total de tu compra"))
es_mienbro = input("Eres miembro? (Si/No)")
miembro = es_mienbro.upper()

if precio_compra >= compra_minima and miembro == "SI":
    descuento = 0.1 #descuento del 10
elif miembro == "SI": #Si solo es mienbro
    descuento = .05 #descuento del 5
elif precio_compra >= compra_minima: #Si supera la compra minima pero no es miembro
    descuento = .03 #descuento del 3
else: 
    descuento = 0
    
#Hago los calculos para obtener el precio final
if descuento != 0:
    precio_descuento = precio_compra * descuento
    precio_final = precio_compra - precio_descuento
    print(f"Has obtenido un descuento del {descuento * 100}%")
    print(f"Precio final de la compra {precio_final}€")
else:
    print(f"No Has obtenido un descuento")
    print(f"Precio final de la compra {precio_compra}€")
    
    
    
#RETO ESTACION DEL AÑO
mes = int(input("Introduce el numero del mes (1-12)"))    
estacion = None #Declaro la variable sin valor

if mes == 1 or mes == 2 or mes == 12:
    estacion = "invierno"
elif mes == 3 or mes == 4 or mes == 5:
    estacion = "primavera"
elif mes == 6 or mes == 7 or mes == 8:
    estacion = "verano"
elif mes == 9 or mes == 10 or mes == 11:
    estacion = "otoño"
else:
    estacion = "estacion desconocida"
print(f"La estacion para el mes {mes} es {estacion}")