# Simulaci-n-de-Cajero-Autom-tico

## Simulación de Cajero Automático – Versión Base

Proyecto académico que simula el funcionamiento básico de un cajero automático utilizando Python.

---

## Funcionalidad desarrollada por el Integrante 1 (Demetrio)

Esta sección corresponde al desarrollo inicial del programa, creando la estructura base donde se integrarán las funciones de los demás integrantes.

### Estructura implementada:

- Menú principal del cajero (Consultar saldo, Depositar, Retirar, Historial, Cambiar usuario, Salir).
- Uso de un bucle `while` para mantener el menú activo.
- Validación de entradas mediante `try / except`.
- Control del rango de opciones válidas (1–6).
- Mensajes temporales indicando dónde se integrarán las funciones completas.

---

## Funcionalidad desarrollada por el Integrante 2 (Yohel)

Esta sección implementa el sistema de seguridad y la estructura de datos que permite manejar la información de múltiples usuarios.

### Estructura implementada:

- Estructura de Usuarios: Definición del diccionario `usuarios` que almacena 5 PINs (`1111` a `5555`), sirviendo como base para el almacenamiento futuro de `saldo` e `historial`.
- Sistema de PIN (Función `login_usuario`): Implementación de la autenticación al inicio del programa.
- Límite de Intentos: Se limita la validación del PIN a un máximo de 3 intentos. Si se falla, el programa termina por seguridad.
- Cambio de Usuario (Función `cambiar_usuario`): Implementación de la opción para finalizar la sesión actual e iniciar una nueva.
-Flujo de Control: El menú principal ya no se ejecuta hasta que un usuario ha iniciado sesión con éxito.

---

## Funcionalidad desarrollada por el Integrante 3 (John)

Esta sección corresponde a la implementación de las funciones principales del cajero relacionadas con la gestión del dinero y el saldo del usuario.

### Funcionalidades implementadas:

* **Consultar saldo:** Muestra el saldo actual de la cuenta del usuario activo.
* **Depositar dinero:** Permite ingresar un monto válido, suma dicho monto al saldo y registra el movimiento en el historial.
* **Retirar dinero:** Permite retirar un monto válido. El sistema verifica que el usuario tenga fondos suficientes y registra el movimiento en el historial.

### Validaciones aplicadas:

* Impedir montos negativos o iguales a cero.
* Evitar montos no numéricos mediante `try/except`.
* Verificación de saldo suficiente antes de permitir un retiro.

### Registro de movimientos:

Cada operación se almacena en la lista `historial` del usuario activo en formato descriptivo, por ejemplo:

* `"Depósito: +$50.00"`
* `"Retiro: -$20.00"`

---

## Guía de Uso Rápida

Para iniciar el cajero y probar la autenticación:

1.  El sistema pedirá un PIN. Ingresa uno de los PINs válidos: `1111`, `2222`, `3333`, `4444`, o `5555`.
2.  Si fallas el PIN 3 veces, el programa se cerrará automáticamente.
3.  Una vez dentro del menú, puedes probar la opción 5. Cambiar usuario para volver a la pantalla de login.

---
