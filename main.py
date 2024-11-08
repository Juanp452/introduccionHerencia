# main.py
from estudiantes import Estudiantes
from profesores import Profesores
from administrativos import Administrativos
from empleado_limpieza import EmpleadoLimpieza

def main():
    # Crear objetos
    estudiante = Estudiantes()
    estudiante.get_nombre()
    print("La persona no tiene nombre")
    estudiante.set_apellido("Pérez")
    estudiante.set_edad(20)
    estudiante.set_matricula("123456")
    estudiante.set_carrera("Ingeniería")
    estudiante.set_semestre("5to")

    profesor = Profesores()
    profesor.set_nombre("María")
    profesor.set_apellido("López")
    profesor.set_edad(40)
    profesor.set_departamento("Matemáticas")
    profesor.set_categorias("Instructor")
    profesor.set_maximo_grado_de_estudios("Doctorado")

    administrativo = Administrativos()
    administrativo.set_nombre("Carlos")
    administrativo.set_apellido("González")
    administrativo.set_edad(35)
    administrativo.set_cargo("Secretario")
    administrativo.set_area("Areas basicas")

    empresa = EmpleadoLimpieza()
    empresa.set_nombre("Pedro")
    empresa.set_apellido("Martínez")
    empresa.set_edad(45)
    empresa.set_numero_empleado("E1234")
    empresa.set_nombre_empresa("Limpieza S.A.")
    empresa.set_direccion("Calle Ficticia 123")
    empresa.set_turno("Nocturno")

    # Mostrar información
    print("Estudiante:")
    print(estudiante.mostrar_informacion())

    print("\nProfesor:")
    print(profesor.mostrar_informacion())

    print("\nAdministrativo:")
    print(administrativo.mostrar_informacion())

    print("\nEmpleado de Limpieza:")
    print(empresa.mostrar_informacion())



main()