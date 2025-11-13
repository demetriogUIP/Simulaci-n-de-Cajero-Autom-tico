# ===========================
#   CAJERO AUTOMÁTICO - BASE
#   Demetrio FASE1
# ===========================

opcion = 0  # opción inicial

def mostrar_menu():
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Consultar saldo")
    print("2. Depositar dinero")
    print("3. Retirar dinero")
    print("4. Ver historial de movimientos")
    print("5. Cambiar usuario")
    print("6. Salir")


print("💰 Bienvenido al Cajero Automático")

# (luego se añadirá el login del PIN aquí)
print("Sistema inicializando...")

while opcion != 6:
    mostrar_menu()

    # Validar entrada del usuario
    try:
        opcion = int(input("Selecciona una opción: "))
    except ValueError:
        print("❌ Entrada inválida. Por favor ingresa un número del 1 al 6.")
        continue

    # Validación del rango
    if opcion < 1 or opcion > 6:
        print("❌ Opción fuera de rango. Intenta nuevamente.")
        continue

    # Aquí solo mostramos mensajes temporales
    if opcion == 1:
        print("👉 [FUNCION Consultar Saldo] — Aún no implementada.")
    elif opcion == 2:
        print("👉 [FUNCION Depositar] — Aún no implementada.")
    elif opcion == 3:
        print("👉 [FUNCION Retirar] — Aún no implementada.")
    elif opcion == 4:
        print("👉 [FUNCION Ver Historial] — Aún no implementada.")
    elif opcion == 5:
        print("👉 [FUNCION Cambiar Usuario] — Aún no implementada.")
    elif opcion == 6:
        print("👋 Saliendo del sistema... Gracias por usar el cajero.")

print("Programa finalizado.")
