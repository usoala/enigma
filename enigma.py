import random

rotor = [("A","R")]

letras = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"

def creaRotor():
    resultado = []
    otrasLetras = list(letras)
    for l in letras:
        n = random.randrange(len(otrasLetras))
        resultado.append((l,otrasLetras[n]))
        otrasLetras.pop(n)
    return resultado
    
r = creaRotor()