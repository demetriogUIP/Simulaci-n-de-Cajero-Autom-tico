import sys
from modules.consultar_saldo import consultar_saldo
from modules.hacer_deposito import depositos
from modules.retiro_monto import retiro_monto
from modules.historial import historial_moviemientos
from modules.auth import login_usuario, cambiar_usuario
##DataImport
from data.users_data import usuarios
# Funciones para el login del usuario y cambio de usuario

# ============================================
#   CAJERO AUTOMÁTICO - BASE
#   Demetrio FASE1
# ============================================

def mostrar_menu():
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Consultar saldo")
    print("2. Depositar dinero")
    print("3. Retirar dinero")
    print("4. Ver historial de movimientos")
    print("5. Cambiar usuario")
    print("6. Salir")


def main():
    print("🔥 Bienvenido al Cajero Automático")
    
    opcion = 0    # opción inicial
    pin_activo = None  # Necesario para controlar el login
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
            opcion = 0 #Control si el usuario tipea 6 por error
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
            consultar_saldo(datos_usuario)
        # 2. Depositar dinero
        elif opcion == 2:
           depositos(datos_usuario)
        # 3. Retirar dinero
        elif opcion == 3:
          retiro_monto(datos_usuario)
        # 4. Ver historial de movimientos
        elif opcion == 4:
          historial_moviemientos(datos_usuario)
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

if __name__ == '__main__':
    main()