#LISTAS
mi_lista = [1,2,3,4,5]
print(mi_lista)
print("largo de la lista: " + len(mi_lista))

#Accedder a los elementos de la lista por indice
print("Accedo al valor del indice 4: " + mi_lista[4]) #Resultado = 5
print("Accedo al ultimo valor: " + mi_lista[-1]) #Resultado = 5

#Modificar los elementos de una lista
mi_lista[1] = 10 #Asigno el valor de 10 al indice 1

#Añado un elemento al final de la lista
mi_lista.append(6)

#Añado un elemento en una posicion especifica de la lista
mi_lista.insert(2,15) #en el indice 2 añado el 15

#Elimino elemento de la lista
mi_lista.remove(5) #Paso el VALOR q quiero eliminar de la lista
mi_lista.pop(1) #De esta forma le paso la posicion y elimina el numero q hay en esa posicion
del mi_lista[2] #Aqui paso la posicion tambien


#TUPLAS
"""
Las tuplas son similares a las listas, pero son inmutables, lo que significa que
NO pueden modificarse después de su creación
"""
# Definición de una tupla
mi_tupla = (1, 2, 3, 4, 5)
print(mi_tupla)
print("Largo de la tupla:", len(mi_tupla))

# Acceder a elementos de una tupla por índice
print("Accedo al valor del índice 2:", mi_tupla[2])  # Resultado = 3
print("Accedo al último valor:", mi_tupla[-1])       # Resultado = 5

# Intento de modificar un valor en la tupla (esto causará un error porque las tuplas son inmutables)
# mi_tupla[1] = 10  # Esto generará un TypeError

# Uso de tuplas en asignaciones múltiples
a, b, c = (10, 20, 30)
print("Valores de a, b y c:", a, b, c)



#CONJUNTOS
"""
Los conjuntos son colecciones no ordenadas y no permiten elementos duplicados. 
Son útiles para operaciones de conjuntos matemáticos como unión, intersección, etc.
"""

# Definición de un conjunto
mi_conjunto = {1, 2, 3, 4, 5}
print(mi_conjunto)
print("Largo del conjunto:", len(mi_conjunto))

# Añadir elementos a un conjunto
mi_conjunto.add(6)  # Añade el elemento 6
print("Después de añadir 6:", mi_conjunto)

# Eliminar elementos de un conjunto
mi_conjunto.remove(3)  # Elimina el elemento 3 (si no está, generará un error)
print("Después de eliminar 3:", mi_conjunto)

# Eliminar con 'discard' (si el elemento no está, no genera error)
mi_conjunto.discard(10)  # No pasa nada si el elemento 10 no está

#compruebo si el valor 8 existe en mi conjunto (false porque no existe)
print("Existe el 8 en el conjunto? " + {8 in mi_conjunto})

# Operaciones de conjuntos
otro_conjunto = {4, 5, 6, 7}
union = mi_conjunto | otro_conjunto      # Unión
interseccion = mi_conjunto & otro_conjunto  # Intersección (lo que hay igual en ambos conjuntos)
diferencia = mi_conjunto - otro_conjunto  # Diferencia (lo que hay diferente)

print("Unión:", union)
print("Intersección:", interseccion)
print("Diferencia:", diferencia)


#DICCIONARIOS
"""
Los diccionarios almacenan datos en pares clave-valor. Las claves deben ser únicas.
"""
# Definición de un diccionario
mi_diccionario = {"nombre": "Juan", "edad": 30, "ciudad": "Madrid"}
print(mi_diccionario)

# Acceder a un valor por su clave
print("Nombre:", mi_diccionario["nombre"])  # Resultado = "Juan"

# Añadir un nuevo par clave-valor
mi_diccionario["ocupacion"] = "Ingeniero"
print("Después de añadir 'ocupacion':", mi_diccionario)

# Modificar un valor existente
mi_diccionario["edad"] = 31
print("Después de modificar 'edad':", mi_diccionario)

# Eliminar un par clave-valor
del mi_diccionario["ciudad"]
print("Después de eliminar 'ciudad':", mi_diccionario)

# Métodos útiles para diccionarios
claves = mi_diccionario.keys()       # Devuelve todas las claves
valores = mi_diccionario.values()    # Devuelve todos los valores
items = mi_diccionario.items()       # Devuelve pares clave-valor

print("Claves:", claves)
print("Valores:", valores)
print("Items:", items)
