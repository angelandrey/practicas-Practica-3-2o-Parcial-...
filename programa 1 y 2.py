# Programa para manejar divisas y almacenar información del usuario.

# 1. Guardar el diccionario de divisas
divisas = {
    'Euro': '€',    # Símbolo del Euro
    'Dollar': '$',  # Símbolo del Dólar
    'Yen': '¥'      # Símbolo del Yen
}

# Solicitar al usuario que ingrese una divisa
divisa_input = input("Introduce una divisa (Euro, Dollar, Yen): ")

# Verificar si la divisa ingresada está en el diccionario
if divisa_input in divisas:
    # Si está, mostrar el símbolo correspondiente
    print(f"El símbolo de {divisa_input} es: {divisas[divisa_input]}")
else:
    # Si no está, mostrar un mensaje de error
    print("La divisa no está en el diccionario.")

# 2. Preguntar al usuario por sus datos personales
nombre = input("Introduce tu nombre: ")
edad = input("Introduce tu edad: ")
direccion = input("Introduce tu dirección: ")
telefono = input("Introduce tu número de teléfono: ")

# Crear un diccionario para almacenar los datos del usuario
datos_usuario = {
    'nombre': nombre,      # Almacena el nombre del usuario
    'edad': edad,          # Almacena la edad del usuario
    'direccion': direccion, # Almacena la dirección del usuario
    'telefono': telefono    # Almacena el teléfono del usuario
}

# Mostrar los datos del usuario en un formato legible
print(f"\n{datos_usuario['nombre']} "
      f"tiene {datos_usuario['edad']} años, "
      f"vive en {datos_usuario['direccion']} "
      f"y su número de teléfono es {datos_usuario['telefono']}.")
