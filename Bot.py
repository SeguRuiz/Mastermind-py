import random
from ValidacionTipos import ValidacionTipos

colores_disponibles = [
    "red",
    "green",
    "yellow",
    "blue",
    "cyan",
    "black",
    "white",
    "magenta",
]

class Bot(ValidacionTipos):
    def __init__(self, opciones: list, cantidad_respuestas: int) -> None:
        self.validar_tipos(list, opciones)
        self.validar_tipos(int, cantidad_respuestas)
        self.__opciones = opciones
        self.__cantidad_respuestas = cantidad_respuestas

    @property
    def bot_respuesta(self):
        return random.sample(self.__opciones, self.__cantidad_respuestas)


bot1 = Bot(colores_disponibles, 5)


class Bot_2:
    def __init__(self, tablero_principal, tablero_pistas, intentos_actuales, no_tocar) -> None:
        self.__tablero_principal = tablero_principal
        self.__tablero_pistas = tablero_pistas
        self.__intentos_actuales = intentos_actuales
        self.__no_tocar = no_tocar

    def prueba(self):
        opciones = [
            "red",
            "green",
            "yellow",
            "blue",
            "cyan",
            "black",
            "white",
            "magenta",
        ]

        if self.__intentos_actuales == 0:
            return random.sample(
                ["red", "green", "yellow", "blue", "cyan", "black", "white", "magenta"],
                5,
            )
        else:
            respuesta = ["white" for n in range(5)]
            for x in range(len(self.__tablero_pistas[self.__intentos_actuales])):
                
                if self.__tablero_pistas[self.__intentos_actuales - 1][x][1] == "green":
                    respuesta[x] = self.__tablero_principal[
                        self.__intentos_actuales - 1
                    ][x][1]
                elif self.__tablero_pistas[self.__intentos_actuales - 1][x][1] == "white":
                    self.__no_tocar.append(self.__tablero_principal[self.__intentos_actuales - 1][x][1])
                    for n in opciones:
                        if n != self.__tablero_principal[self.__intentos_actuales - 1][x][1]:

                            respuesta[x] = n
                else:
                    print(self.__no_tocar)
                    respuesta[x] = random.choice([c for c in opciones if c not in self.__no_tocar])
                
        return respuesta

