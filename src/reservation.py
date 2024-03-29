# -*- coding: utf-8 -*-
"""Copia de RESERVATION.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_dECYLGIRu6CBtyjSa8GlYnwmqLCkfyf

**INSTITUTO TECNOLÓGICO Y DE ESTUDIOS SUPERIORES DE MONTERREY CAMPUS EDUCACIÓN DIGITAL**

**ASIGNATURA:**
PRUEBAS DE SOFTWARE Y ASEGURAMIENTO DE LA CALIDAD

**ACTIVIDAD 6.2:**
EJERCICIO DE PROGRAMACIÓN 3 Y PRUEBAS DE UNIDAD - RESERVATION

**ESTUDIANTE:**
ESTEBAN SÁNCHEZ RETAMOZA A01740631

**EQUIPO DOCENTE:**
DR. GERARDO PADILLA ZÁRATE PROFESOR TITULAR &
MTRA. YETNALEZI QUINTAS RUIZ PROFESOR ASISTENTE
"""

"""
RESERVATION
"""

import json
from google.colab import files


class Hotel:
    """Representa un hotel: detalles y habitaciones."""

    def __init__(self, hotel_data):
        self.hotel_id = hotel_data["hotel_id"]
        self.name = hotel_data["name"]
        self.rooms = hotel_data["rooms"]

    def display_info(self):
        """Imprime la información en la consola."""
        print(f"Detalles del Hotel '{self.name}' (ID: {self.hotel_id}):")
        print("Habitaciones:")
        for room_number, details in self.rooms.items():
            reser_s = "Reservada" if details["is_reserved"] else "Disponible"
            custinf = (f" por Cliente ID: {details['customer_id']}"
                       if details["customer_id"] else "")
            print(f"  Habitación {room_number}: {reser_s}{custinf}")
        print("\n")

    def save_to_json(self, filename='hotel_updated.json'):
        """Guarda los datos del hotel en un archivo JSON y lo descarga."""
        hotel_data = {
            "hotel_id": self.hotel_id,
            "name": self.name,
            "rooms": self.rooms
        }
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(hotel_data, file, indent=4)
        files.download(filename)
        print(f"Archivo '{filename}' guardado y descargado con éxito.\n")


def upload_file():
    """Solicita al usuario que cargue un archivo y devuelve el contenido."""
    uploaded = files.upload()
    if uploaded:
        file_name = next(iter(uploaded))
        print(f"\nArchivo '{file_name}' cargado con éxito.\n")
        return json.loads(uploaded[file_name].decode('utf-8'))
    print("\nNo se cargó ningún archivo.\n")
    return {}


def create_reservation(hotel, room_number, customer_id):
    """Crea una reserva en un hotel para una habitación."""
    room = hotel.rooms.get(room_number)
    if room:
        if not room["is_reserved"]:
            room["is_reserved"] = True
            room["customer_id"] = customer_id
            print(f"Reserva creada para la habitación {room_number}.")
        else:
            print("La habitación ya está reservada.")
    else:
        print("La habitación no existe en este hotel.")
    # Mostrar información actualizada
    hotel.display_info()
    # Guardar y descargar el nuevo JSON
    hotel.save_to_json()


def cancel_reservation(hotel, room_number):
    """Cancela una reserva en un hotel para una habitación."""
    room = hotel.rooms.get(room_number)
    if room:
        if room["is_reserved"]:
            room["is_reserved"] = False
            room["customer_id"] = None
            print(f"Reserva cancelada para la habitación {room_number}.")
        else:
            print("La habitación no está reservada.")
    else:
        print("La habitación no existe en este hotel.")
    # Mostrar información actualizada
    hotel.display_info()
    # Guardar y descargar el nuevo JSON
    hotel.save_to_json()


def main():
    """Flujo principal de ejecución."""
    # Solicitar al usuario que cargue el archivo JSON del hotel
    print("Por favor, cargue el archivo JSON del hotel:")
    hotels_data = upload_file()

    if not hotels_data:
        print("No se proporcionó ningún archivo. Saliendo del programa.")
        return

    # Crear instancia del hotel
    hotel = Hotel(hotels_data)

    while True:
        print("Reservation")
        print("a. Create a Reservation")
        print("b. Cancel a Reservation")
        print("x. Exit")

        choice = input("Select an option: ").lower()

        if choice == 'a':
            room_number = input("Enter the room number: ")
            customer_id = input("Enter the customer ID: ")
            create_reservation(hotel, room_number, customer_id)
        elif choice == 'b':
            room_number = input("Enter the room number: ")
            cancel_reservation(hotel, room_number)
        elif choice == 'x':
            print("Exiting the program.")
            break
        else:
            print("Invalid option, please select a valid option.\n")


if __name__ == "__main__":
    main()