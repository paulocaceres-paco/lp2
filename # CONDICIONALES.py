# CONDICIONALES
# Ejercicio 1: Control de acceso
#Solicite al usuario su edad y si posee documento de identidad (S/N).
#Permitir el ingreso únicamente si:
#Tiene 18 años o más.
#Posee documento de identidad.
#En caso contrario, informar el motivo por el cual no puede ingresar.

#edad = int(input("Ingrese su edad: "))
#documento = input("¿Posee documento de identidad? (S/N): ").strip().upper()
#if edad >= 18 and documento == "S":
#    print("Acceso permitido. Bienvenido.")
#elif edad < 18 and documento != "S":
#    print("Acceso denegado: es menor de edad y no posee documento de identidad.")
#elif edad < 18:
#    print("Acceso denegado: es menor de edad.")
#else:
#    print("Acceso denegado: no posee documento de identidad.")


#Ejercicio 2: Descuento en una tienda
#Solicite el monto de una compra.
#Aplicar los siguientes descuentos:
#20% si supera Gs. 500.000
#10% si supera Gs. 200.000
#Sin descuento en cualquier otro caso
#Mostrar:
#Monto original
#Descuento aplicado
#Total a pagar

#monto = float(input("Ingrese el monto de la compra (Gs.): "))
#if monto > 500000:
#    porcentaje = 20
#elif monto > 200000:
#    porcentaje = 10
#else:
#    porcentaje = 0
#descuento = monto * porcentaje / 100
#total = monto - descuento
#print(f"Monto original: Gs. {monto}")
#print(f"Descuento aplicado ({porcentaje}%): Gs. {descuento}")
#print(f"Total a pagar: Gs. {total}")

#Ejercicio 3: Semáforo inteligente
#Solicite el color del semáforo:
#Verde
#Amarillo
#Rojo
#Mostrar la acción correspondiente:
#Avanzar
#Reducir velocidad
#etenerse
#Si el color ingresado no es válido, mostrar un mensaje de error.

#color = input("Ingrese el color del semáforo (verde/amarillo/rojo): ").strip().lower()
#if color == "verde":
#    print("Avanzar")
#elif color == "amarillo":
#    print("Reducir velocidad")
#elif color == "rojo":
#    print("Detenerse")
#else:
#    print("Error: color no válido.")

#Ejercicio 4: Nivel de batería
#Solicite el porcentaje de batería de un teléfono móvil.
#Mostrar:
#Crítica (0% a 10%)
#Baja (11% a 30%)
#Normal (31% a 80%)
#Alta (81% a 100%)
#Validar que el porcentaje ingresado sea correcto.

#bateria = int(input("Ingrese el porcentaje de batería: "))
#if bateria < 0 or bateria > 100:
#    print("Error: el porcentaje debe estar entre 0 y 100.")
#elif bateria <= 10:
#    print("Batería crítica")
#elif bateria <= 30:
#    print("Batería baja")
#elif bateria <= 80:
#    print("Batería normal")
#else:
#    print("Batería alta")

#Ejercicio 5: Evaluación climática
#Solicite la temperatura actual.
#Mostrar:
#Mucho frío (menos de 10°C)
#Templado (10°C a 24°C)
#Caluroso (25°C a 34°C)
#Muy caluroso (35°C o más)

#temperatura = float(input("Ingrese la temperatura actual (°C): "))
#if temperatura < 10:
#    print("Mucho frío")
#elif temperatura < 25:
#    print("Templado")
#elif temperatura < 35:
#    print("Caluroso")
#else:
#    print("Muy caluroso")