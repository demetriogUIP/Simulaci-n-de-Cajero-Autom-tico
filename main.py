import sys
# ============================================
#   CAJERO AUTOMÁTICO - USUARIOS
#   Yohel
# ============================================

# Creamos 5 usuarios con diferentes pines pero
# aún sin información de cada uno
# otro compañero va a estar alimentando esta parte

usuarios = {
    "1111": {"saldo": 0.00, "historial": []},
    "2222": {"saldo": 0.00, "historial": []},
    "3333": {"saldo": 0.00, "historial": []},
    "4444": {"saldo": 0.00, "historial": []},
    "5555": {"saldo": 0.00, "historial": []},
}

# Funciones para el login del usuario y cambio de usuario
def login_usuario():
    # Solicita el PIN con un límite de 3 intentos.
    # Retorna el PIN activo si es exitoso, o None si se acaban los intentos.
    intentos_maximos = 3
    print("\n--- INICIO DE SESIÓN (3 intentos) ---")

    for intento in range(intentos_maximos):
        # calculamos cuántos intentos quedan
        intentos_restantes = intentos_maximos - (intento + 1)

        pin_ingresado = input("Ingrese su PIN de 4 dígitos: ")

        if pin_ingresado in usuarios:
            print("✅ PIN correcto. Bienvenido.")
            return pin_ingresado
        else:
            if intentos_restantes > 0:
                print(f"❌ PIN incorrecto. Le quedan {intentos_restantes} intento(s).")
            else:
                # si el bucle termina, se agotaron los intentos (Bloqueo)
                print("\nIntentos agotados. Sesión bloqueada.")
                return None

    return None


def cambiar_usuario():
    # Función para cambiar de usuario. Llama a login_usuario
    print("\n--- CAMBIO DE USUARIO ---")
    return login_usuario()  # Retorna el nuevo PIN activo o None


# ============================================
#   CAJERO AUTOMÁTICO - BASE
#   Demetrio FASE1
# ============================================

opcion = 0    # opción inicial
pin_activo = None  # Necesario para controlar el login


def mostrar_menu():
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Consultar saldo")
    print("2. Depositar dinero")
    print("3. Retirar dinero")
    print("4. Ver historial de movimientos")
    print("5. Cambiar usuario")
    print("6. Salir")


print("🔥 Bienvenido al Cajero Automático")

# Bucle inicial: Valida el PIN antes de entrar al menú principal
while pin_activo is None:
    pin_activo = login_usuario()
    if pin_activo is None:
        sys.exit("Programa finalizado.")

# Bucle principal del menú
while opcion != 6:

    # Obtenemos los datos del usuario activo en cada iteración
    datos_usuario = usuarios[pin_activo]

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

    # ================================
    #   FASE 3 –  OPERACIONES: CONSULTAR / DEPOSITAR / RETIRAR
    #    JOHN
    # ================================

    # 1. Consultar saldo
    if opcion == 1:
        print("\n💰 CONSULTAR SALDO")
        print(f"Tu saldo actual es: ${datos_usuario['saldo']:.2f}")

    # 2. Depositar dinero
    elif opcion == 2:
        print("\n💵 DEPÓSITO DE DINERO")
        try:
            monto = float(input("Ingresa el monto a depositar: "))
        except ValueError:
            print("❌ Monto inválido. Debes ingresar un número.")
            continue

        if monto <= 0:
            print("❌ El monto debe ser mayor que 0.")
            continue

        # Variable acumulativa: actualizamos el saldo
        datos_usuario["saldo"] += monto
        # Registramos el movimiento en el historial
        datos_usuario["historial"].append(f"Depósito: +${monto:.2f}")

        print("✅ Depósito realizado correctamente.")
        print(f"Nuevo saldo: ${datos_usuario['saldo']:.2f}")

    # 3. Retirar dinero
    elif opcion == 3:
        print("\n🏧 RETIRO DE DINERO")
        try:
            monto = float(input("Ingresa el monto a retirar: "))
        except ValueError:
            print("❌ Monto inválido. Debes ingresar un número.")
            continue

        if monto <= 0:
            print("❌ El monto debe ser mayor que 0.")
            continue

        if monto > datos_usuario["saldo"]:
            print(f"❌ Saldo insuficiente. Tu saldo actual es: ${datos_usuario['saldo']:.2f}")
            continue

        # Actualizamos saldo y registramos en historial
        datos_usuario["saldo"] -= monto
        datos_usuario["historial"].append(f"Retiro: -${monto:.2f}")

        print("✅ Retiro realizado correctamente.")
        print(f"Nuevo saldo: ${datos_usuario['saldo']:.2f}")

    # 4. Ver historial de movimientos
    elif opcion == 4:
        print("\n📜 HISTORIAL DE MOVIMIENTOS")

        if not datos_usuario["historial"]:
            print("📭 No tienes movimientos registrados todavía.")
        else:
            for i, mov in enumerate(datos_usuario["historial"], start=1):
                print(f"{i}. {mov}")

    # 5. Cambiar usuario (llama a tu función y actualiza pin_activo)
    elif opcion == 5:
        # Nota: la llamada a cambiar_usuario se integra aquí
        print("➡️ [FUNCION Cambiar Usuario] – Ejecutando...")
        pin_activo = cambiar_usuario()
        if pin_activo is None:
            opcion = 6  # Si el nuevo login falla, salimos del menú

    # 6. Salir
    elif opcion == 6:
        print("➡️ Saliendo del sistema... Gracias por usar el cajero.")

print("Programa finalizado.")
