import random

class Rotor():

    def __init__(self,abecedario="ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"):
        self.abecedario=abecedario
        self.rotor = []
        otrasLetras = list(abecedario)
        for l in abecedario:
            n = random.randrange(len(otrasLetras))
            self.rotor.append((l,otrasLetras[n]))
            otrasLetras.pop(n)


rotor1 = Rotor()
rotor2 = Rotor()
rotor3 = Rotor()
rotor4 = Rotor()
rotor5 = Rotor()
rotor6 = Rotor()
rotor7 = Rotor()
rotor8 = Rotor()
rotor9 = Rotor()
rotor10 = Rotor()
    

        
    
   