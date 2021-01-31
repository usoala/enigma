from rotor import rotor1, rotor2, rotor3
from reflector import reflector1

rotor1.rotor = [('A', 'O'), ('B', 'Ñ'), ('C', 'G'), ('D', 'J'), ('E', 'H'), ('F', 'X'), ('G', 'I'), ('H', 'Q'), ('I', 'W'), ('J', 'K'), ('K', 'R'), ('L', 'S'), ('M', 'Z'), ('N', 'U'), ('Ñ', 'N'), ('O', 'P'), ('P', 'L'), ('Q', 'M'), ('R', 'A'), ('S', 'E'), ('T', 'F'), ('U', 'T'), ('V', 'C'), ('W', 'Y'), ('X', 'B'), ('Y', 'D'), ('Z', 'V')]
rotor2.rotor = [('A', 'Ñ'), ('B', 'B'), ('C', 'I'), ('D', 'Z'), ('E', 'S'), ('F', 'J'), ('G', 'D'), ('H', 'H'), ('I', 'K'), ('J', 'G'), ('K', 'X'), ('L', 'M'), ('M', 'F'), ('N', 'N'), ('Ñ', 'U'), ('O', 'P'), ('P', 'A'), ('Q', 'L'), ('R', 'T'), ('S', 'E'), ('T', 'V'), ('U', 'Q'), ('V', 'R'), ('W', 'Y'), ('X', 'W'), ('Y', 'O'), ('Z', 'C')]
rotor3.rotor = [('A', 'P'), ('B', 'D'), ('C', 'V'), ('D', 'G'), ('E', 'O'), ('F', 'M'), ('G', 'S'), ('H', 'Z'), ('I', 'Ñ'), ('J', 'K'), ('K', 'Y'), ('L', 'Q'), ('M', 'T'), ('N', 'J'), ('Ñ', 'I'), ('O', 'U'), ('P', 'W'), ('Q', 'B'), ('R', 'A'), ('S', 'N'), ('T', 'X'), ('U', 'E'), ('V', 'H'), ('W', 'R'), ('X', 'C'), ('Y', 'F'), ('Z', 'L')]
reflector1.reflector = [('A', 'F'), ('B', 'H'), ('C', 'R'), ('D', 'M'), ('E', 'G'), ('F', 'A'), ('G', 'E'), ('H', 'B'), ('I', 'L'), ('J', 'Q'), ('K', 'N'), ('L', 'I'), ('M', 'D'), ('N', 'K'), ('Ñ', 'V'), ('O', 'Z'), ('P', 'Y'), ('Q', 'J'), ('R', 'C'), ('S', 'U'), ('T', 'X'), ('U', 'S'), ('V', 'Ñ'), ('W', 'W'), ('X', 'T'), ('Y', 'P'), ('Z', 'O')]

def codifica(l, posicion):
    if (posicion // 27)%3 == 0:
        p1 = posicion % 27
        p2 = 0
        p3 = 0
    elif (posicion // 27)%3 == 1:
        p1 = 0
        p2 = posicion % 27
        p3 = 0
    elif (posicion // 27)%3 == 2:
        p1 = 0
        p2 = 0
        p3 = posicion % 27    
    for t in rotor1.rotor:
        if l == t[0]:
            p = (rotor1.rotor.index(t)+p1)%27
            res1 = rotor1.rotor[p][1]
    for t in rotor2.rotor:
        if res1 == t[0]:
            p = (rotor2.rotor.index(t)+p2)%27
            res2 = rotor2.rotor[p][1]
    for t in rotor3.rotor:
        if res2 == t[0]:
            p = (rotor3.rotor.index(t)+p3)%27
            res3 = rotor3.rotor[p][1]
    for t in reflector1.reflector:
        if res3 == t[0]:
            res4 = reflector1.reflector[reflector1.reflector.index(t)][1]
    for t in rotor3.rotor:
        if res4 == t[1]:
            p = (rotor3.rotor.index(t)-p3)%27
            res5 = rotor3.rotor[p][0]
    for t in rotor2.rotor:
        if res5 == t[1]:
            p = (rotor2.rotor.index(t)-p2)%27
            res6 = rotor2.rotor[p][0]
    for t in rotor1.rotor:
        if res6 == t[1]:
            p = (rotor1.rotor.index(t)-p1)%27
            print(rotor1.rotor[p][0], end="")