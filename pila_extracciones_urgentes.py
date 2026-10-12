#Programa 1. Pila de clientes para extracciones urgentes
from datetime import datetime

print("========================================")
print("   PLAN DE CONTINGENCIA - EXTRACCIONES")
print("========================================")

# Lista temporal para guardar los clientes que cumplen los criterios
clientes_urgentes = []

while True:

    print()

    # Datos básicos del cliente
    cedula = input("Ingrese la cédula del cliente: ")
    nombre = input("Ingrese el nombre del cliente: ")
    telefono = input("Ingrese el teléfono del cliente: ")

    # Tipo de atención
    print()
    print("Tipo de atención:")
    print("1. Limpieza")
    print("2. Calzas")
    print("3. Extracción")
    print("4. Diagnóstico")

    while True:
        opcion_atencion = input("Seleccione una opción: ")

        if opcion_atencion == "1":
            tipo_atencion = "Limpieza"
            break
        elif opcion_atencion == "2":
            tipo_atencion = "Calzas"
            break
        elif opcion_atencion == "3":
            tipo_atencion = "Extracción"
            break
        elif opcion_atencion == "4":
            tipo_atencion = "Diagnóstico"
            break
        else:
            print("Opción inválida. Intente nuevamente.")

    # Prioridad
    print()
    print("Prioridad:")
    print("1. Normal")
    print("2. Urgente")

    while True:
        opcion_prioridad = input("Seleccione una opción: ")

        if opcion_prioridad == "1":
            prioridad = "Normal"
            break
        elif opcion_prioridad == "2":
            prioridad = "Urgente"
            break
        else:
            print("Opción inválida. Intente nuevamente.")

    # Fecha de la cita
    while True:
        fecha_texto = input("Ingrese la fecha de la cita (dd/mm/aaaa): ")

        try:
            fecha_cita = datetime.strptime(fecha_texto, "%d/%m/%Y")
            break
        except ValueError:
            print("Fecha inválida. Utilice el formato dd/mm/aaaa.")

    # Crear el registro del cliente
    cliente = {
        "cedula": cedula,
        "nombre": nombre,
        "telefono": telefono,
        "tipo_atencion": tipo_atencion,
        "prioridad": prioridad,
        "fecha_cita": fecha_cita
    }

    # Solo incluimos extracciones con prioridad urgente
    if tipo_atencion == "Extracción" and prioridad == "Urgente":
        clientes_urgentes.append(cliente)
        print("Cliente agregado al plan de contingencia.")
    else:
        print("El cliente no cumple los criterios para la pila de contingencia.")

    # Preguntar si vamos a registrar otro cliente
    print()

    while True:
        continuar = input("¿Desea registrar otro cliente? (s/n): ").lower()

        if continuar == "s" or continuar == "n":
            break
        else:
            print("Opción inválida. Escriba s o n.")

    if continuar == "n":
        break


# Ordenamos desde la fecha más lejana hasta la más cercana.
# Así, al apilar, la fecha más cercana quedará en el tope.
for i in range(len(clientes_urgentes) - 1):
    for j in range(len(clientes_urgentes) - 1 - i):

        if clientes_urgentes[j]["fecha_cita"] < clientes_urgentes[j + 1]["fecha_cita"]:

            auxiliar = clientes_urgentes[j]
            clientes_urgentes[j] = clientes_urgentes[j + 1]
            clientes_urgentes[j + 1] = auxiliar


# Crear la pila
pila_clientes = []

for cliente in clientes_urgentes:
    pila_clientes.append(cliente)


# Informe de la pila
print()
print("========================================")
print("INFORME DE LA PILA DE CLIENTES URGENTES")
print("========================================")

if len(pila_clientes) == 0:
    print("No hay clientes urgentes para extracción.")

else:
    print("Orden de llamado: fecha más cercana a fecha más lejana.")
    print()

    # Recorremos desde el tope hacia la base
    for i in range(len(pila_clientes) - 1, -1, -1):

        cliente = pila_clientes[i]

        print("Cédula:", cliente["cedula"])
        print("Nombre:", cliente["nombre"])
        print("Teléfono:", cliente["telefono"])
        print("Atención:", cliente["tipo_atencion"])
        print("Prioridad:", cliente["prioridad"])
        print("Fecha:", cliente["fecha_cita"].strftime("%d/%m/%Y"))
        print("----------------------------------------")


# Simular el llamado de clientes utilizando POP
print()
print("========================================")
print("LLAMADO DE CLIENTES DESDE LA PILA")
print("========================================")

while len(pila_clientes) > 0:

    cliente = pila_clientes.pop()

    print(
        "Llamando a:",
        cliente["nombre"],
        "- Fecha:",
        cliente["fecha_cita"].strftime("%d/%m/%Y")
    )

print("Pila finalizada.")