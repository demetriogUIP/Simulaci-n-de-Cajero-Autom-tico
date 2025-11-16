def retiro_monto(data):
    ###RETIRO DE DINERO##
    print("\n🏧 RETIRO DE DINERO")
    try:
        monto = float(input("Ingresa el monto a retirar: "))
    except ValueError:
        print("❌ Monto inválido. Debes ingresar un número.")
        return

    if monto <= 0:
        print("❌ El monto debe ser mayor que 0.")
        return

    if monto > data["saldo"]:
        print(f"❌ Saldo insuficiente. Tu saldo actual es: ${data['saldo']:.2f}")
        return

    # Actualizamos saldo y registramos en historial
    data["saldo"] -= monto
    data["historial"].append(f"Retiro: -${monto:.2f}")
    
    print("✅ Retiro realizado correctamente.")
    print(f"Nuevo saldo: ${data['saldo']:.2f}")