from rotor import rotor1, rotor2, rotor3
from reflector import reflector1
from codifica import codifica
from decodifica import decodifica

rotor1.rotor = [('A', 'O'), ('B', 'Ñ'), ('C', 'G'), ('D', 'J'), ('E', 'H'), ('F', 'X'), ('G', 'I'), ('H', 'Q'), ('I', 'W'), ('J', 'K'), ('K', 'R'), ('L', 'S'), ('M', 'Z'), ('N', 'U'), ('Ñ', 'N'), ('O', 'P'), ('P', 'L'), ('Q', 'M'), ('R', 'A'), ('S', 'E'), ('T', 'F'), ('U', 'T'), ('V', 'C'), ('W', 'Y'), ('X', 'B'), ('Y', 'D'), ('Z', 'V')]
rotor2.rotor = [('A', 'Ñ'), ('B', 'B'), ('C', 'I'), ('D', 'Z'), ('E', 'S'), ('F', 'J'), ('G', 'D'), ('H', 'H'), ('I', 'K'), ('J', 'G'), ('K', 'X'), ('L', 'M'), ('M', 'F'), ('N', 'N'), ('Ñ', 'U'), ('O', 'P'), ('P', 'A'), ('Q', 'L'), ('R', 'T'), ('S', 'E'), ('T', 'V'), ('U', 'Q'), ('V', 'R'), ('W', 'Y'), ('X', 'W'), ('Y', 'O'), ('Z', 'C')]
rotor3.rotor = [('A', 'P'), ('B', 'D'), ('C', 'V'), ('D', 'G'), ('E', 'O'), ('F', 'M'), ('G', 'S'), ('H', 'Z'), ('I', 'Ñ'), ('J', 'K'), ('K', 'Y'), ('L', 'Q'), ('M', 'T'), ('N', 'J'), ('Ñ', 'I'), ('O', 'U'), ('P', 'W'), ('Q', 'B'), ('R', 'A'), ('S', 'N'), ('T', 'X'), ('U', 'E'), ('V', 'H'), ('W', 'R'), ('X', 'C'), ('Y', 'F'), ('Z', 'L')]
reflector1.reflector = [('A', 'F'), ('B', 'H'), ('C', 'R'), ('D', 'M'), ('E', 'G'), ('F', 'A'), ('G', 'E'), ('H', 'B'), ('I', 'L'), ('J', 'Q'), ('K', 'N'), ('L', 'I'), ('M', 'D'), ('N', 'K'), ('Ñ', 'V'), ('O', 'Z'), ('P', 'Y'), ('Q', 'J'), ('R', 'C'), ('S', 'U'), ('T', 'X'), ('U', 'S'), ('V', 'Ñ'), ('W', 'W'), ('X', 'T'), ('Y', 'P'), ('Z', 'O')]

posicionInicial = 0


def codificaMensaje(mensaje, posicion):
    letras = list(mensaje)
    while " " in letras:
        letras.remove(" ")
    for l in letras:
        codifica(l, posicion)
        posicion += 1

def decodificaMensaje(mensaje, posicion):
    for l in mensaje:
        decodifica(l, posicion)
        posicion += 1


decodificaMensaje("DVCEMFHÑRXK", 2)