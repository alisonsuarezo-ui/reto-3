# 1. Creamos el tablero como una lista de listas (3x3)
def crear_tablero():
    return [[" " for _ in range(3)] for _ in range(3)]

# 2. Función para mostrar el tablero con "estilo"
def mostrar_tablero(tablero):
    print("\n")
    for i in range(3):
        # Unimos los elementos de la fila con un separador "|"
        print(" " + " | ".join(tablero[i]))
        if i < 2:
            print("---+---+---")
    print("\n")

# 6. El "Juez": Verifica si alguien ha ganado
def verificar_ganador(tablero, jugador):
    # Revisar filas
    for fila in tablero:
        if all(casilla == jugador for casilla in fila):
            return True
    
    # Revisar columnas
    for col in range(3):
        if all(tablero[fila][col] == jugador for fila in range(3)):
            return True
            
    # Revisar las 2 diagonales
    if tablero[0][0] == tablero[1][1] == tablero[2][2] == jugador:
        return True
    if tablero[0][2] == tablero[1][1] == tablero[2][0] == jugador:
        return True
        
    return False

# 7. Detección de empate (¿está lleno?)
def tablero_lleno(tablero):
    return all(casilla != " " for fila in tablero for casilla in fila)

# --- EL BUCLE PRINCIPAL DEL JUEGO ---
def jugar():
    tablero = crear_tablero()
    jugador_actual = "X"
    
    print("¡Bienvenido al Tres en Raya!")
    print("Introduce fila y columna (0, 1 o 2)")

    while True:
        mostrar_tablero(tablero)
        print(f"Turno del jugador: {jugador_actual}")

        # 5. Realización de una jugada con validación
        try:
            fila = int(input("Introduce fila (0-2): "))
            col = int(input("Introduce columna (0-2): "))
            
            if fila not in range(3) or col not in range(3):
                print("¡Error! Solo números del 0 al 2. Intenta de nuevo.")
                continue
                
            if tablero[fila][col] != " ":
                print("¡Esa casilla ya está ocupada! Elige otra.")
                continue
        except ValueError:
            print("¡Entrada inválida! Por favor, escribe números.")
            continue

        # Actualizar el tablero
        tablero[fila][col] = jugador_actual

        # 6 y 8. Revisar resultado y anunciar
        if verificar_ganador(tablero, jugador_actual):
            mostrar_tablero(tablero)
            print(f"¡Felicidades, el jugador '{jugador_actual}' ha ganado!")
            break
            
        if tablero_lleno(tablero):
            mostrar_tablero(tablero)
            print("¡La partida ha terminado en empate!")
            break

        # 4. Cambio de turno
        jugador_actual = "O" if jugador_actual == "X" else "X"

# Iniciar el juego
if __name__ == "__main__":
    jugar()