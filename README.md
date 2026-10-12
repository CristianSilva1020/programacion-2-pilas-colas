# Uso de estructuras dinámicas: Pilas y Colas

## Descripción

En esta actividad desarrollamos dos programas para aplicar las estructuras dinámicas Pilas y Colas en un consultorio odontológico.

El primer programa genera una pila con los clientes que requieren extracción dental y tienen prioridad urgente. En él, los clientes quedan organizados para ser llamados desde la fecha de cita más cercana hasta la más lejana.

El segundo programa genera una cola para gestionar la agenda diaria del consultorio y atender los clientes en el mismo orden en que se encuentran programados.

## Pila de extracciones urgentes

Para el plan de contingencia registramos los datos de los clientes y verificamos que cumplan dos condiciones:

- El tipo de atención debe ser Extracción.
- La prioridad debe ser Urgente.

Luego organizamos los clientes según la fecha de la cita. Utilizamos una pila para realizar los llamados, aplicando el principio LIFO para que el programa genere un informe con los clientes que deben ser atendidos prioritariamente.

## Cola de atención

Para la agenda diaria registramos los clientes en el mismo orden en que deben ser atendidos.

Utilizamos una cola para conservar este orden y aplicamos el principio FIFO, donde el primer cliente que entra es también el primero que sale para ser atendido.

El programa también permite consultar cuál es el siguiente cliente pendiente.

## Archivos

- `pila_extracciones_urgentes.py`: implementación de la pila.
- `cola_agenda.py`: implementación de la cola.

## Lenguaje utilizado

Python 3.

## Ejecución

Para ejecutar el programa de la pila:

```
py pila_extracciones_urgentes.py
```

Para ejecutar el programa de la cola:

```
py cola_agenda.py
```