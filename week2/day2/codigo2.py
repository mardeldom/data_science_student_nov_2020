import random
espadas = list(range(1,11))
bastos = list(range(1,11))
copas = list(range(1,11))
oros = list(range(1,11))
baraja = [espadas, bastos, copas, oros]
def baraja_random(x):
    for elem1,elem2, elem3, elem4 in range(len(baraja)):
        return random.choice(elem)
s = baraja_random(x=baraja)
print(s)
 