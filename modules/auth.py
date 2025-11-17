from data.users_data import usuarios

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

