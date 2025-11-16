def historial_moviemientos(data):
    print("\n📜 HISTORIAL DE MOVIMIENTOS")
    if not data["historial"]:
        print("📭 No tienes movimientos registrados todavía.")
    else:
        for i, mov in enumerate(data["historial"], start=1):
            print(f"{i}. {mov}")
