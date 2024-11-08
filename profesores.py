# profesores.py
from persona import Persona

class Profesores(Persona):
    def __init__(self):
        super().__init__()
        self._departamento = ""
        self._categorías = ""
        self._máximo_grado_de_estudios = ""

    # Getter y Setter
    def get_categorias(self):
        return self._categorías

    def set_categorias(self, categorias):
        self._categorías = categorias

    def get_maximo_grado_de_estudios(self):
        return self._departamento

    def set_maximo_grado_de_estudios(self, maximo_grado_estudios):
        self._departamento = maximo_grado_estudios

    def get_departamento(self):
        return self._departamento

    def set_departamento(self, departamento):
        self._departamento = departamento

    def mostrar_informacion(self):
        base_info = super().mostrar_informacion()
        return f"{base_info}, Departamento: {self._departamento}, categorias: {self.get_categorias()}, maximo_grado_estudios: {self._departamento}"
