import random
import string
from abc import ABC, abstractmethod
from materiales import Lf, Ld

def menu():
    materiales = []

    while True:
        print("\n===== Biblioteca =====")
        print("1. Registrarlibrofísico")
        print("2. Registrarlibrodigital")
        print("3. Prestar")
        print("4. Devolver")
        print("5. Mostrar todo")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            titulo = input("Título: ")
            autor = input("Autor: ")
            ejemplar = input("Número de ejemplar: ")
            materiales.append(Lf(titulo, autor, ejemplar))
            print("Libro físico registrado.")

        elif opcion == "2":
            titulo = input("Título: ")
            autor = input("Autor: ")
            tamano = input("Tamaño del archivo (MB): ")
            materiales.append(Ld(titulo, autor, tamano))
            print("Libro digital registrado.")

        elif opcion == "3":
            codigo = input("Código del material a prestar: ")
            encontrado = False
            for m in materiales:
                if m.get_codigo() == codigo:
                    m.prestar()
                    encontrado = True
                    break
            if not encontrado:
                print("Material no encontrado.")

        elif opcion == "4":
            codigo = input("Código del material a devolver: ")
            encontrado = False
            for m in materiales:
                if m.get_codigo() == codigo:
                    m.devolver()
                    encontrado = True
                    break
            if not encontrado:
                print("Material no encontrado.")

        elif opcion == "5":
            if not materiales:
                print("No hay materiales registrados.")
            else:
                for m in materiales:
                    m.mostrar_info()

        elif opcion == "6":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")


if __name__ == "__main__":
    menu()
