import random
import string
from abc import ABC, abstractmethod

class libros(ABC):
    def __init__(self, titulo, autor):
        self.__titulo = titulo
        self.__autor = autor
        self.__codigo = self.__generar_codigo()
        self.__prestado = False

    def __generar_codigo(self):
        return ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))

    def get_titulo(self):
        return self.__titulo

    def get_autor(self):
        return self.__autor

    def get_codigo(self):
        return self.__codigo

    def esta_prestado(self):
        return self.__prestado

    def prestar(self):
        if self.__prestado:
            print(f"El material '{self.__titulo}' ya está prestado.")
        else:
            self.__prestado = True
            print(f"Material '{self.__titulo}' prestado con éxito.")

    def devolver(self):
        if self.__prestado:
            self.__prestado = False
            print(f"Material '{self.__titulo}' devuelto con éxito.")
        else:
            print(f"El material '{self.__titulo}' no estaba prestado.")

    @abstractmethod
    def mostrar_info(self):
        pass
class Lf(libros):
    def __init__(self, titulo, autor, numero_ejemplar):
        super().__init__(titulo, autor)
        self.__numero_ejemplar = numero_ejemplar
        self.__dias_prestamo = 7
    def mostrar_info(self):
        estado = "Prestado" if self.esta_prestado() else "Disponible"
        print(f"[Libro Físico] Título: {self.get_titulo()}, Autor: {self.get_autor()}, "
              f"Código: {self.get_codigo()}, Ejemplar: {self.__numero_ejemplar}, "
              f"Días máx: {self.__dias_prestamo}, Estado: {estado}")
class Ld(libros):
    def __init__(self, titulo, autor, tamano_mb):
        super().__init__(titulo, autor)
        self.__tamano_mb = tamano_mb
        self.__dias_prestamo = 3
    def mostrar_info(self):
        estado = "Prestado" if self.esta_prestado() else "Disponible"
        print(f"[Libro Digital] Título: {self.get_titulo()}, Autor: {self.get_autor()}, "
              f"Código: {self.get_codigo()}, Tamaño: {self.__tamano_mb}MB, "
              f"Días máx: {self.__dias_prestamo}, Estado: {estado}")