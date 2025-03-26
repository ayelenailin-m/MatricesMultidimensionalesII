# Lista principal donde se guardarán todas las personas
personas = []

def ingresar_persona():
    print("\n--- Ingreso de nueva persona ---")
    nombre = input("Ingresa el nombre: ").strip().capitalize()
    apellido = input("Ingresa el apellido: ").strip().capitalize()
    dni = input("Ingresa el DNI: ").strip()

    telefonos_input = input("Ingresa los teléfonos separados por comas: ")
    telefonos = [tel.strip() for tel in telefonos_input.split(",") if tel.strip() != ""]

    hijos_input = input("Ingresa los nombres de los hijos separados por comas: ")
    hijos = [hijo.strip().capitalize() for hijo in hijos_input.split(",") if hijo.strip() != ""]

    persona = [nombre, apellido, dni, telefonos, hijos]
    personas.append(persona)
    print(" Persona ingresada correctamente.")

def mostrar_todos():
    print("\n--- Datos de todas las personas ---")
    if not personas:
        print("No hay personas cargadas.")
        return
    
    print("\nMatriz de datos:")
    print(personas)

    print("\nListado detallado:")
    for p in personas:
        nombre, apellido, dni, telefonos, hijos = p
        print(f"{nombre} {apellido}, DNI: {dni}, Teléfonos: {len(telefonos)} teléfono(s), Hijos: {len(hijos)} hijo(s)")

def filtrar_por_dni():
    print("\n--- Buscar persona por DNI ---")
    dni_buscar = input("Ingresa el DNI para filtrar: ").strip()
    encontrado = False

    for p in personas:
        if p[2] == dni_buscar:
            nombre, apellido, dni, telefonos, hijos = p
            print(f"\nDatos de {nombre} {apellido}:")
            print(f"DNI: {dni}")
            print(f"Teléfonos: {len(telefonos)} teléfono(s)")
            print(f"Hijos: {len(hijos)} hijo(s)")
            encontrado = True
            break
    
    if not encontrado:
        print("⚠️ No se encontró una persona con ese DNI.")

# Menú principal
def menu():
    while True:
        print("""
--- Menú ---
1. Ingresar nueva persona
2. Mostrar todos los datos
3. Filtrar por DNI
4. Salir
""")
        opcion = input("Elige una opción: ").strip()

        if opcion == "1":
            ingresar_persona()
        elif opcion == "2":
            mostrar_todos()
        elif opcion == "3":
            filtrar_por_dni()
        elif opcion == "4":
            print("👋 Saliendo del programa...")
            break
        else:
            print("❌ Opción inválida. Intentá de nuevo.")

# Ejecutar el programa
menu()
