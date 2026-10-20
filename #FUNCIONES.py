#FUNCIONES

#Ejercicio 1 - Estadísticas de una lista
#Crear una función llamada:
#estadisticas(numeros)
#que reciba una lista de números y retorne:
#El valor máximo.
#El valor mínimo.
#El promedio.

#def estadisticas(lista):
#    maximo = max(lista)
#    minimo = min(lista)
#    promedio = sum(lista)/len(lista)
  
#    return maximo, minimo, promedio

#Programa principal
#numeros = [10, 20, 30, 40, 50]
#mayor, menor, promedio = estadisticas(numeros)
#print(f'El mayor es {mayor}, el menor es {menor} y el promedio es {promedio}')

#Ejercicio 2 - Buscar un elemento
#Crear una función:
#buscar(lista, valor)
#que reciba una lista y un valor.
#La función debe retornar:
#True si el valor existe.
#False si el valor no existe.

#def buscar(lista, valor):
#    for nombre in lista:
#        if nombre == valor:
#            return True
    
#    return False

#Programa principal
#alumnos = ["Ana", "Luis", "Carlos", "Pedro", "Maria Luisa", "César"]
#nombre = input('Ingrese el nombre a buscar: ')
#resultado = buscar(alumnos, nombre)
#print(resultado)

#Ejercicio 3 - Eliminar duplicados
#Crear una función:
#eliminar_duplicados(lista)
#que reciba una lista y retorne una colección sin elementos repetidos utilizando un conjunto (set).

#def eliminar_duplicados(lista):
#    return set(lista)

#Programa principal
#numeros = [1, 2, 2, 3, 3, 3, 4]
#print(eliminar_duplicados(numeros))

#Ejercicio 4 - Frecuencia de elementos
#Crear una función:
#contar_frecuencia(lista)
#que reciba una lista y retorne un diccionario indicando cuántas veces aparece cada elemento.

#def contar_frecuencia(lista):
#    frecuencia = {}

#    for elemento in lista:
#        #Consultar si el elemento ya está en el diccionario o no
#        if elemento in frecuencia: #El elemento ya fue cargado previamente
#            frecuencia[elemento] += 1
#        else:
#            frecuencia[elemento] = 1

#    return frecuencia

#Programa principal
#lista = ["a", "b", "a", "c", "a", "b"]
#resultado = contar_frecuencia(lista)
#print(resultado)

#Ejercicio 5 - Promedio de notas
#Crear una función:
#calcular_promedio(notas)
#que reciba una lista de notas y retorne el promedio.
#Crear también una función:
#estado(promedio)
#que indique:
#"Aprobado" si el promedio es mayor o igual a 60.
#"Reprobado" en caso contrario.

#def calcular_promedio(notas):
#    promedio = sum(notas)/len(notas)
#    return promedio

#def estado(promedio):
#    if promedio >= 60:
#        return "Aprobado"
#    else:
#        return "Reprobado"

#Programa principal
#notas = [70, 80, 90, 60]
#promedio = calcular_promedio(notas)
#print(f'El promedio del alumno es {promedio}')
#print(f'El estado del alumno es ' + estado(promedio))

#Ejercicio 6 - Agenda telefónica
#Utilice un diccionario para almacenar contactos.

#agenda = {
#    "Juan": "098111111",
#    "Ana": "098222222"
#}
#Funciones
#def agregar_contacto():
#    nombre = input('Ingrese el nombre: ')
#    numero = input('Ingrse el número telefónico: ')

#    agenda[nombre] = numero
#    print('Contacto agregado correctamente..')

#def buscar_contacto():
#    nombre = input('Ingrese el nombre a buscar: ')
#    if nombre in agenda:
#        print(f'Teléfono de {nombre}: {agenda[nombre]}')
#    else:
#        print('Contacto no encontrado..')

#def mostrar_contactos():
#    if len(agenda) == 0:
#        print('La agenda está vacía..')
#    else:
#        print('\n --- Contactos ---')
#        for nombre, telefono in agenda.items():
#            print(f'{nombre}:{telefono}')

#Programa principal
#while True:
#    print('\n === AGENDA TELEFÓNICA ===')
#    print('1. Agregar contacto')
#    print('2. Buscar contacto')
#    print('3. Mostrar contactos')
#    print('4. Salir')

#    opcion = input('Seleccione una opción: ')
#    #Llama a la función en base a la opción de menú seleccionada
#    if opcion == '1':
#        agregar_contacto()
#    elif opcion == '2':
#        buscar_contacto()
#    elif opcion == '3':
#        mostrar_contactos()
#    elif opcion == '4':
#        #Salir del programa
#        print('Saliendo del programa...')
#        break
#    else:
#        print('Opción inválida')

#Ejercicio 7 - Producto más caro
#Dada la siguiente lista de tuplas:
#productos = [
#    ("Teclado", 150000),
#    ("Mouse", 80000),
#    ("Monitor", 1200000)
#]
#Crear una función:
#producto_mas_caro(productos)
#que retorne el nombre y precio del producto más caro.
#Salida esperada
#Producto: Monitor
#precio: 1200000

#def producto_mas_caro(productos):
#    return max(productos, key=lambda producto: producto[1])

#productos = [
#    ("Teclado", 150000),
#    ("Mouse", 80000),
#    ("Monitor", 1200000)
#]

#nombre, precio = producto_mas_caro(productos)
#print(f"Producto: {nombre}")
#rint(f"Precio: {precio}")

#Ejercicio 8 - Inventario de productos
#Utilizando el siguiente diccionario:
#inventario = {
#    "Teclado": 10,
#    "Mouse": 5,
#    "Monitor": 2
#}
#Crear las siguientes funciones:
#agregar_stock()
#vender_producto()
#consultar_stock()
#El programa debe permitir:
#Aumentar el stock de un producto.
#Registrar una venta.
#Consultar la cantidad disponible.

#def leer_entero(mensaje):
#    while True:
#        try:
#            return int(input(mensaje))
#        except ValueError:
#            print("Error: ingrese un número entero.")

#def agregar_stock(inventario):
#    producto = input("Producto: ").strip().title()
#    cantidad = leer_entero("Cantidad a agregar: ")
#
#    if cantidad <= 0:
#        print("Error: la cantidad debe ser mayor a 0.")
#        return

#    inventario[producto] = inventario.get(producto, 0) + cantidad
#    print(f"Stock actualizado: {producto} = {inventario[producto]}")

#def vender_producto(inventario):
#    producto = input("Producto: ").strip().title()

#    if producto not in inventario:
#        print("Error: el producto no existe.")
#        return

#    cantidad = leer_entero("Cantidad a vender: ")

#    if cantidad <= 0:
#        print("Error: la cantidad debe ser mayor a 0.")
#    elif cantidad > inventario[producto]:
#        print(f"Error: stock insuficiente (disponible: {inventario[producto]}).")
#    else:
#        inventario[producto] -= cantidad
#        print(f"Venta registrada. Stock restante: {inventario[producto]}")

#def consultar_stock(inventario):
#    producto = input("Producto: ").strip().title()

#    if producto in inventario:
#        print(f"{producto}: {inventario[producto]} unidades")
#    else:
#        print("Error: el producto no existe.")


#inventario = {
#    "Teclado": 10,
#    "Mouse": 5,
#    "Monitor": 2
#}

#opcion = ""
#while opcion != "4":
#    print("\n1. Agregar stock")
#    print("2. Vender producto")
#    print("3. Consultar stock")
#    print("4. Salir")
#    opcion = input("Elija una opción: ").strip()

#    if opcion == "1":
#        agregar_stock(inventario)
#   elif opcion == "2":
#       vender_producto(inventario)
#   elif opcion == "3":
#       consultar_stock(inventario)
#   elif opcion == "4":
#       print("Hasta luego.")
#   else:
#      print("Opción no válida.")

#Ejercicio 9 - Ranking de alumnos
#Dada la siguiente lista de tuplas:
#alumnos = [
#    ("Juan", 85),
#    ("Ana", 95),
#    ("Pedro", 70)
#]
#Crear funciones para:
#Obtener el mejor alumno.
#Obtener el peor alumno.
#Calcular el promedio general.
#Salida esperada
#Mejor alumno: Ana (95)
#Peor alumno: Pedro (70)
#Promedio general: 83.33

#def mejor_alumno(alumnos):
#    return max(alumnos, key=lambda alumno: alumno[1])

#def peor_alumno(alumnos):
#    return min(alumnos, key=lambda alumno: alumno[1])

#def promedio_general(alumnos):
#    total = sum(nota for nombre, nota in alumnos)
#    return total / len(alumnos)

#alumnos = [
#    ("Juan", 85),
#    ("Ana", 95),
#    ("Pedro", 70)
#]

#nombre_mejor, nota_mejor = mejor_alumno(alumnos)
#nombre_peor, nota_peor = peor_alumno(alumnos)
#print(f"Mejor alumno: {nombre_mejor} ({nota_mejor})")
#print(f"Peor alumno: {nombre_peor} ({nota_peor})")
#print(f"Promedio general: {promedio_general(alumnos)}")

#Ejercicio 10 - Sistema de gestión de estudiantes
#Utilizando un diccionario:
#estudiantes = {
#    "Juan": [70, 80, 90],
#    "Ana": [100, 95, 90]
#}
#Crear las siguientes funciones:
#agregar_estudiante()
#calcular_promedio()
#mostrar_promedios()
#mejor_estudiante()
#El programa debe mostrar el siguiente menú:
#1. Agregar estudiante
#2. Mostrar promedios
#3. Mostrar mejor estudiante
#4. Salir

