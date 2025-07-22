import random as rd

PALABRAS = ['kevin', 'estiven', 'yepes', 'villareal', 'developer']


# Funciones 
def elegir_palabra(palabras):
    """Devuelve una palabra elegida al azar de la lista."""
    return rd.choice(palabras)


def crear_guiones(palabra):
    """Crea la lista de guiones inicial según la longitud de la palabra."""
    return ["_"] * len(palabra)


def mostrar_progreso(guiones):
    """Imprime la palabra parcial con espacios."""
    print("Palabra:", " ".join(guiones))


def actualizar_guiones(palabra, guiones, letra):
    """
    Reemplaza guiones por la letra cuando acierta.
    Devuelve True si la letra estaba en la palabra, False si no.
    """
    acierto = False
    for i, c in enumerate(palabra): # el índice (posición) de cada letra , el carácter de esa posicion
        if c == letra:
            guiones[i] = letra
            acierto = True
    return acierto


def palabra_completa(guiones):
    """True si ya no quedan guiones."""
    return "_" not in guiones


# --------------------------
# Lógica principal del juego
# --------------------------
def jugar_ahorcado(palabras=PALABRAS, vidas=5):
    palabra = elegir_palabra(palabras)
    guiones = crear_guiones(palabra)

    print("¡Bienvenido al juego de adivinar la palabra!")
    mostrar_progreso(guiones)

    while vidas > 0:
        letra = input("Dime una letra para adivinar tu palabra: ").lower().strip()
        if not letra:
            print("No ingresaste nada. Intenta de nuevo.")
            continue
        letra = letra[0]  # por si el usuario escribe más de un carácter

        acierto = actualizar_guiones(palabra, guiones, letra)

        if acierto:
            print(f"¡Bien! La letra está en la palabra: {' '.join(guiones)}")
        else:
            vidas -= 1
            print(f"No está en la palabra: {' '.join(guiones)}. Te quedan {vidas} vidas.")

        if palabra_completa(guiones):
            print(f"¡Felicidades! Adivinaste la palabra: {palabra}")
            return True  # Ganaste

    print(f"Has perdido. La palabra era: {palabra}")
    return False  # Perdiste



# Ejecutar solo si es script principal
if __name__ == "__main__":
    jugar_ahorcado()
