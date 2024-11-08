# persona.py
class Persona:
    def __init__(self):
        self._nombre = ""
        self._apellido = ""
        self._edad = 0

    # Getters y Setters
    def get_nombre(self):
        return self._nombre

    def set_nombre(self, nombre):
        self._nombre = nombre

    def get_apellido(self):
        return self._apellido

    def set_apellido(self, apellido):
        self._apellido = apellido

    def get_edad(self):
        return self._edad

    def set_edad(self, edad):
        self._edad = edad

    def mostrar_informacion(self):
        return f"Nombre: {self._nombre} {self._apellido}, Edad: {self._edad}"
