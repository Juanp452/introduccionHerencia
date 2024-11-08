# estudiantes.py
from persona import Persona

class Estudiantes(Persona):
    def __init__(self):
        super().__init__()
        self._matricula = ""
        self._carrera = ""
        self._semestre = ""

    # Getter y Setter
    def get_carrera(self):
        return self._carrera

    def set_carrera(self, carrera):
        self._carrera = carrera

    def get_semestre(self):
        return self._semestre

    def set_semestre(self, semestre):
        self._semestre = semestre

    def get_matricula(self):
        return self._matricula

    def set_matricula(self, matricula):
        self._matricula = matricula

    def mostrar_informacion(self):
        base_info = super().mostrar_informacion()
        return f"{base_info}, Matrícula: {self._matricula}, Semestre: {self._semestre}, Carrera: {self._carrera}"
