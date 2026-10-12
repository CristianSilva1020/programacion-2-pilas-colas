#Programa 2. Cola para la agenda diaria
from collections import deque

print("========================================")
print("       AGENDA DIARIA DEL CONSULTORIO")
print("========================================")

fecha_agenda = input("Ingrese la fecha de la agenda (dd/mm/aaaa): ")

# Crear la cola
cola_atencion = deque()

print()
print("Ingrese los clientes en el mismo orden definido por la agenda.")

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

    # Crear el registro del cliente
    cliente = {
        "cedula": cedula,
        "nombre": nombre,
        "telefono": telefono,
        "tipo_atencion": tipo_atencion
    }

    # Encolar el cliente
    cola_atencion.append(cliente)

    print("Cliente agregado a la cola de atención.")

    # Preguntar si vamos a incluir otro cliente
    print()

    while True:
        continuar = input("¿Desea agregar otro cliente a la agenda? (s/n): ").lower()

        if continuar == "s" or continuar == "n":
            break
        else:
            print("Opción inválida. Escriba s o n.")

    if continuar == "n":
        break


# Mostrar la agenda
print()
print("========================================")
print("AGENDA DEL DÍA", fecha_agenda)
print("========================================")

turno = 1

for cliente in cola_atencion:

    print(
        "Turno:", turno,
        "- Cédula:", cliente["cedula"],
        "- Nombre:", cliente["nombre"],
        "- Atención:", cliente["tipo_atencion"]
    )

    turno = turno + 1


# Atender los clientes utilizando la cola
print()
print("========================================")
print("ATENCIÓN DE CLIENTES")
print("========================================")

while len(cola_atencion) > 0:

    # Retirar el primer cliente de la cola
    cliente = cola_atencion.popleft()

    print()
    print("Atendiendo a:", cliente["nombre"])
    print("Cédula:", cliente["cedula"])
    print("Tipo de atención:", cliente["tipo_atencion"])

    # Consultar quién sigue sin eliminarlo
    if len(cola_atencion) > 0:
        print("Siguiente cliente:", cola_atencion[0]["nombre"])
    else:
        print("No quedan clientes pendientes en la cola.")

print()
print("Agenda del día finalizada.")