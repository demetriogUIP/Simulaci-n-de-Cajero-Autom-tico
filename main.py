import sys
# ===================================================
#   CAJERO AUTOMÁTICO - USUARIOS
#   Yohel
# ===================================================

#Creamos 5 usuarios con diferentes pines pero 
#aun sin informacion de cada uno
#otro companero va a estar aalimentando esta parte

usuarios = {
    "1111": {"saldo": 0.00, "historial": []},
    "2222": {"saldo": 0.00, "historial": []},
    "3333": {"saldo": 0.00, "historial": []},
    "4444": {"saldo": 0.00, "historial": []},
    "5555": {"saldo": 0.00, "historial": []}
}

#funciones para el login del usuario y cambio de usuario 
def login_usuario():
    #Solicita el PIN con un limite de 3 intentos.
    #Retorna el PIN activo si es exitoso, o None si se acaban los intentos.
    
    intentos_maximos = 3
    print("\n--- INICIO DE SESIÓN (3 intentos) ---")
    
    for intento in range(intentos_maximos):
        # calculamos cuantos intentos quedan
        intentos_restantes = intentos_maximos - (intento + 1)
        
        pin_ingresado = input("Ingrese su PIN de 4 dígitos: ")

        if pin_ingresado in usuarios:
            print(f" PIN correcto. Bienvenido.") 
            return pin_ingresado 
        else:
            if intentos_restantes > 0:
                print(f"PIN incorrecto. Le quedan {intentos_restantes} intento(s).") 
    
    # si el bucle termina, se agotaron los intentos (Bloqueo)
    print("\nIntentos agotados. Sesión bloqueada.") 
    return None

def cambiar_usuario():
#Función para cambiar de usuario. Llama a login_usuario
    print("\n--- CAMBIO DE USUARIO ---")
    return login_usuario() # Retorna el nuevo PIN activo o None


# ===========================
#   CAJERO AUTOMÁTICO - BASE
#   Demetrio FASE1
# ===========================

opcion = 0 ; 
pin_activo = None # Necesario para controlar el login

def mostrar_menu():
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Consultar saldo")
    print("2. Depositar dinero")
    print("3. Retirar dinero")
    print("4. Ver historial de movimientos")
    print("5. Cambiar usuario")
    print("6. Salir")


print("💰 Bienvenido al Cajero Automático")

# Bucle inicial: Valida el PIN (tu lógica) antes de entrar al menú principal
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

    # Aquí solo mostramos mensajes temporales
    if opcion == 1:
        print(f"👉 [FUNCION Consultar Saldo] — Aún no implementada. Saldo: ${datos_usuario['saldo']:.2f}") 
    elif opcion == 2:
        print(f"👉 [FUNCION Depositar] — Aún no implementada. (Usuario {pin_activo})") 
    elif opcion == 3:
        print(f"👉 [FUNCION Retirar] — Aún no implementada. (Usuario {pin_activo})") 
    elif opcion == 4:
        print(f"👉 [FUNCION Ver Historial] — Aún no implementada. Historial: {datos_usuario['historial']}") 
        
    # 5. Cambiar usuario (Llama a tu función y actualiza pin_activo)
    elif opcion == 5:
        # Nota: La llamada a cambiar_usuario se integra aquí
        print("👉 [FUNCION Cambiar Usuario] — Ejecutando...") 
        pin_activo = cambiar_usuario()
        if pin_activo is None:
            opcion = 6 # Si el nuevo login falla, salimos del menú
            
    # 6. Salir
    elif opcion == 6:
        print("👋 Saliendo del sistema... Gracias por usar el cajero.") 

print("Programa finalizado.")