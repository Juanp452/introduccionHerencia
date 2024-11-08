# empresa.py
class Empresa:
    def __init__(self):
        self._nombre_empresa = ""
        self._direccion = ""

    # Getter y Setter
    def get_nombre_empresa(self):
        return self._nombre_empresa

    def set_nombre_empresa(self, nombre_empresa):
        self._nombre_empresa = nombre_empresa

    def get_direccion(self):
        return self._direccion

    def set_direccion(self, direccion):
        self._direccion = direccion

    def mostrar_informacion_empresa(self):
        return f"Empresa: {self._nombre_empresa}, Dirección: {self._direccion}"