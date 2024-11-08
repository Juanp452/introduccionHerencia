# empleado_limpieza.py
from empresa import Empresa
from persona import Persona

class EmpleadoLimpieza(Persona, Empresa):
    def __init__(self):
        Persona.__init__(self)
        Empresa.__init__(self)
        self._numero_empleado = ""
        self._turno = ""

    # Getter y Setter para número de empleado
    def get_area (self):
        return self._turno

    def set_turno (self, turno):
        self._turno = turno

    def get_numero_empleado(self):
        return self._numero_empleado

    def set_numero_empleado(self, numero_empleado):
        self._numero_empleado = numero_empleado

    def mostrar_informacion(self):
        # Llamamos directamente al método de mostrar_informacion de Persona y Empresa
        base_info_persona = Persona.mostrar_informacion(self)
        base_info_empresa = Empresa.mostrar_informacion_empresa(self)
        return f"{base_info_persona}, Número de Empleado: {self._numero_empleado}, {base_info_empresa}, turno: {self._turno}"
