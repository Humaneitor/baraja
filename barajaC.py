import baraja

class Baraja():

    def __init__(self, palos, numeros):
        self.__palos = palos
        self.__numeros = numeros
        self.mazacote = baraja.creaBaraja(palos, numeros)

    def barajar(self):
        baraja.barajar(self.mazacote)
