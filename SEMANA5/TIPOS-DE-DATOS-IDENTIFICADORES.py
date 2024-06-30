# Programa para gestionar información básica de empleados
# Permite al usuario ingresar y mostrar datos como nombre, edad, salario y estado laboral.

# Definición de una función para ingresar datos del empleado
def ingresar_empleado():
    """
    Función para ingresar datos de un empleado.
    Returns:
        dict: Un diccionario con los datos ingresados del empleado.
    """
    print("Ingrese los datos del empleado:")
    nombre = input("Nombre:Juan Reyes ")
    edad = int(input("Edad:28 "))
    salario = float(input("Salario (en USD): 350"))
    activo = input("¿Está activo? (Sí/No): si").lower() == 'sí'

    empleado = {
        'nombre': nombre,
        'edad': edad,
        'salario': salario,
        'activo': activo
    }

    return empleado

# Función para mostrar los datos del empleado
def mostrar_empleado(empleado):
    """
    Función para mostrar los datos de un empleado.
    Args:
        empleado (dict): Diccionario con los datos del empleado a mostrar.
    """
    print("\nDatos del empleado:")
    print(f"Nombre: {empleado['nombre']}")
    print(f"Edad: {empleado['edad']} años")
    print(f"Salario: ${empleado['salario']:.2f}")
    estado = "Activo" if empleado['activo'] else "Inactivo"
    print(f"Estado: {estado}")

# Main code
if __name__ == "__main__":
    # Ingresar datos del empleado
    empleado1 = ingresar_empleado()

    # Mostrar los datos del empleado ingresado
    mostrar_empleado(empleado1)