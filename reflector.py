import random
import itertools

class Reflector():

    def __init__(self,abecedario="ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"):
        self.abecedario=abecedario
        self.reflector = []
        otrasLetras = list(abecedario)
        for l in abecedario:
            if l in list(itertools.chain(*self.reflector)):
                self.reflector.append((l,letrasUsadas[letrasUsadas.index(l)-1]))
            else:
                n = random.randrange(len(otrasLetras))
                if l == otrasLetras[n]:
                    try:
                        self.reflector.append((l,otrasLetras[n+1]))
                    except:
                        self.reflector.append((l,otrasLetras[n]))
                else:
                    self.reflector.append((l,otrasLetras[n]))
                letrasUsadas = list(itertools.chain(*self.reflector))
                otrasLetras.remove(letrasUsadas[-1])
                try:
                    otrasLetras.remove(letrasUsadas[-2])
                except:
                    pass
           
                

reflector1 = Reflector()
reflector2 = Reflector()
reflector3 = Reflector()

