def depositos(data):
    print("\n💵 DEPÓSITO DE DINERO")
    try:
            monto = float(input("Ingresa el monto a depositar: "))
    except ValueError:
        print("❌ Monto inválido. Debes ingresar un número.")
        return

    if monto <= 0:
        print("❌ El monto debe ser mayor que 0.")
        return

    # Variable acumulativa: actualizamos el saldo
    data["saldo"] += monto
    # Registramos el movimiento en el historial
    data["historial"].append(f"Depósito: +${monto:.2f}")

    print("✅ Depósito realizado correctamente.")
    print(f"Nuevo saldo: ${data['saldo']:.2f}")