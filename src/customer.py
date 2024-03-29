# -*- coding: utf-8 -*-
"""Copia de Customer.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/16ez9GjoOYgz2aWvC024HQAd-MpxTZVN5

**INSTITUTO TECNOLÓGICO Y DE ESTUDIOS SUPERIORES DE MONTERREY CAMPUS EDUCACIÓN DIGITAL**

**ASIGNATURA:**
PRUEBAS DE SOFTWARE Y ASEGURAMIENTO DE LA CALIDAD

**ACTIVIDAD 6.2:**
EJERCICIO DE PROGRAMACIÓN 3 Y PRUEBAS DE UNIDAD - CUSTOMER

**ESTUDIANTE:**
ESTEBAN SÁNCHEZ RETAMOZA A01740631

**EQUIPO DOCENTE:**
DR. GERARDO PADILLA ZÁRATE PROFESOR TITULAR &
MTRA. YETNALEZI QUINTAS RUIZ PROFESOR ASISTENTE
"""

"""
Gestionador de Clientes.
"""

import json
import time
from google.colab import files


class Customer:
    """Representa un cliente."""

    def __init__(self, customer_id, name, email):
        self.customer_id = customer_id
        self.name = name
        self.email = email

    def to_dict(self):
        """Convierte los detalles del cliente a un diccionario."""
        return {"name": self.name, "email": self.email}

    def save_to_file(self, filename='customers.json'):
        """Guarda la info actualizada en un archivo JSON y lo descarga."""
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump({self.customer_id: self.to_dict()}, file, indent=4)
        files.download(filename)  # Descarga el archivo actualizado

    def display_info(self):
        """Imprime la información del cliente en la consola."""
        print(f"Info del Cliente '{self.name}' (ID: {self.customer_id}):")
        print(f"Nombre: {self.name}")
        print(f"Correo electrónico: {self.email}\n")


def upload_customers_file():
    """Solicita al usuario cargar un archivo de clientes."""
    uploaded = files.upload()
    if uploaded:
        file_name = next(iter(uploaded))
        print(f"\nArchivo '{file_name}' cargado con éxito.\n")
        return json.loads(uploaded[file_name].decode('utf-8'))
    print("\nNo se cargó ningún archivo.\n")
    return {}


def create_customer(customers_data):
    """Crea un nuevo cliente."""
    print("Creación de un nuevo cliente:")
    customer_id = input("Ingrese el ID del cliente: ")
    name = input("Ingrese el nombre del cliente: ")
    email = input("Ingrese el correo electrónico del cliente: ")
    customers_data[customer_id] = {"name": name, "email": email}
    print(f"Cliente '{name}' creado con éxito.\n")


def delete_customer(customers_data):
    """Elimina un cliente."""
    print("Eliminación de un cliente:")
    customer_id = input("Ingrese el ID del cliente que desea eliminar: ")
    if customer_id in customers_data:
        del customers_data[customer_id]
        print(f"Cliente con ID '{customer_id}' eliminado con éxito.\n")
    else:
        print(f"No se encontró ningún cliente con ID '{customer_id}'.\n")


def display_customer_info(customers_data):
    """Muestra la información de un cliente."""
    print("Visualización de la información de un cliente:")
    customer_id = input("Ingrese el ID del cliente que desea visualizar: ")
    if customer_id in customers_data:
        name = customers_data[customer_id]["name"]
        email = customers_data[customer_id]["email"]
        customer = Customer(customer_id, name, email)
        customer.display_info()
    else:
        print(f"No se encontró ningún cliente con ID '{customer_id}'.\n")


def modify_customer_info(customers_data):
    """Modifica la información de un cliente."""
    print("Modificación de la información de un cliente:")
    customer_id = input("Ingrese el ID del cliente que desea modificar: ")
    if customer_id in customers_data:
        name = input("Ingrese el nuevo nombre del cliente: ")
        email = input("Ingrese el nuevo correo electrónico del cliente: ")
        customers_data[customer_id]["name"] = name
        customers_data[customer_id]["email"] = email
        print(f"Info del cliente con ID '{customer_id}' realizado exitoso.\n")
    else:
        print(f"No se encontró ningún cliente con ID '{customer_id}'.\n")


def main():
    """Flujo principal de ejecución para gestionar clientes."""
    start_time = time.time()

    # Cargar información inicial de clientes si existe
    customers_data = upload_customers_file()  # Carga del archivo

    while True:
        print("Clientes")
        print("a. Crear Cliente")
        print("b. Eliminar Cliente")
        print("c. Mostrar Información del Cliente")
        print("d. Modificar Información del Cliente")
        print("x. Salir")

        choice = input("Seleccione una opción: ").lower()

        if choice == 'a':
            create_customer(customers_data)
        elif choice == 'b':
            delete_customer(customers_data)
        elif choice == 'c':
            display_customer_info(customers_data)
        elif choice == 'd':
            modify_customer_info(customers_data)
        elif choice == 'x':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida, seleccione una opción válida.\n")

    # Guardar información actualizada de clientes
    if customers_data:
        with open('customers.json', 'w', encoding='utf-8') as file:
            json.dump(customers_data, file, indent=4)
        files.download('customers.json')  # Descarga el archivo actualizado

    # Imprimir información de los clientes
    print("\nInformación de los clientes:")
    for customer_id, customer_info in customers_data.items():
        name = customer_info["name"]
        email = customer_info["email"]
        customer = Customer(customer_id, name, email)
        customer.display_info()

    end_time = time.time()
    print(f"Tiempo de ejecución: {end_time - start_time:.2f} segundos.\n")


if __name__ == "__main__":
    main()