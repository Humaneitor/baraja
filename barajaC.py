import baraja

class Baraja():

    def __init__(self, palos, numeros):
        self.__palos = palos
        self.__numeros = numeros
        self.mazacote = baraja.creaBaraja(palos, numeros)

    def barajar(self):
        baraja.barajar(self.mazacote)

    def repartir(self, num_jugadores, num_cartas):
        jugadores = []
        for i in range(num_jugadores):
            jugadores.append([])
        
        for jugador in range (num_jugadores):
            for carta in range (num_cartas):
                jugadores[jugador].append(self.mazacote.pop(0))

        return jugadores


