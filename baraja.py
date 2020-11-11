import random
palos = ['o','c','e','b']
numeros = ['A','2','3','4','5','6','7','S','C','R']

def creaBaraja(palos, numeros):
    baraja = []
    for palo in palos:
        for numero in numeros:
            baraja.append(numero+palo)
    return baraja


def barajar(lista):
    for i in range(len(lista)):
        nueva_pos = random.randrange(len(lista))
        aux = lista[nueva_pos]
        lista[nueva_pos]=lista[i]
        lista[i] = aux
    return lista
