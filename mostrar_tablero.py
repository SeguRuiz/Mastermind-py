import itertools
from colored import Fore, Back, Style, fore, style, back
import random


class RenderTablero:
    def __init__(self, forma: str, filas: int, columnas: int) -> None:
        self.__tablero = []
        self.__fila = []
        self.__validar_tipo(forma, str)
        self.__validar_tipo(filas, int)
        self.__validar_tipo(columnas, int)
        self.__forma = forma
        self.__filas = filas
        self.__columnas = columnas
        self.__formar_tablero()

    def __formar_tablero(self):
        
        for x in range(self.__columnas):
            self.__tablero.append([['o', 'white'], ['o', 'white'],['o', 'white'],['o', 'white'],['o', 'white']])

    def print_tablero(self, segundo_tablero=[]):
        if segundo_tablero == []:
             for i in range(len(self.__tablero)):

                for j in range(len(self.__tablero[i])):

                    print(
                        f"{fore(self.__tablero[i][j][1])}{self.__tablero[i][j][0]}{Style.reset} ",
                        end=" ",
                    )
                print()
        else:
            for i in range(len(self.__tablero)):

                for j in range(len(self.__tablero[i])):

                    print(
                        f"{fore(self.__tablero[i][j][1])}{self.__tablero[i][j][0]}{Style.reset} ",
                        end=" ",
                    )

                for j in range(len(self.__tablero[i])):

                    print(
                        f"{fore(segundo_tablero[i][j][1])}{segundo_tablero[i][j][0]}{Style.reset} ",
                        end=" ",
                    )

                print()

    def __validar_tipo(self, dato, tipo):
        if not isinstance(dato, tipo):
            raise TypeError(f"ese tipo no es permitido: {type(dato).__name__}")

    @property
    def tablero(self):
        return self.__tablero
    
    def cambiar_color(self,color, coordenadaX, coordenadaY):
        self.__tablero[coordenadaX][coordenadaY][1] = color
        
        
        


tablero_principal = RenderTablero("k", 5, 12)
tablero_principal2 = RenderTablero("o", 5, 12)

tablero_principal.cambiar_color('red', 4, 1)
tablero_principal.cambiar_color('blue', 4, 2)
tablero_principal.print_tablero()

