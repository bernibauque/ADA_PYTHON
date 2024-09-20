# Crear el diccionario con la base de datos de empleados
empresa = {
    'nombre_empresa': 'Tech Solutions',
    'empleados': [
        {'id_empleado': 101, 'nombre': 'Ana', 'departamento': 'Desarrollo', 'salario': 50000},
        {'id_empleado': 102, 'nombre': 'Luis', 'departamento': 'Marketing', 'salario': 45000},
        {'id_empleado': 103, 'nombre': 'Carlos', 'departamento': 'Recursos Humanos', 'salario': 47000}
    ]
}

# Función para buscar y actualizar el salario de un empleado
def actualizar_salario(id_empleado, nuevo_salario):
    # Encontrar el índice del empleado con el id dado
    empleado_101 = empresa['empleados'][0] if empresa['empleados'][0]['id_empleado'] == id_empleado else None
    empleado_102 = empresa['empleados'][1] if empresa['empleados'][1]['id_empleado'] == id_empleado else None
    empleado_103 = empresa['empleados'][2] if empresa['empleados'][2]['id_empleado'] == id_empleado else None
    
    # Elegir el empleado encontrado
    empleado_encontrado = empleado_101 or empleado_102 or empleado_103

    if empleado_encontrado:
        # Actualizar el salario del empleado
        empleado_encontrado['salario'] = nuevo_salario
        print("Información del empleado después de la actualización:")
        print(f"ID: {empleado_encontrado['id_empleado']}")
        print(f"Nombre: {empleado_encontrado['nombre']}")
        print(f"Departamento: {empleado_encontrado['departamento']}")
        print(f"Salario: {empleado_encontrado['salario']}")
    else:
        print("Empleado no encontrado")

# Actualizar el salario del empleado con id 102
actualizar_salario(102, 48000)
