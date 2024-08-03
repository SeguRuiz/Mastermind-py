from colored import Fore, Back, Style, fore, style, back

from ValidacionTipos import ValidacionTipos
from CrearTablero import CrearTablero, tablero1, tablero2

class PrintTableros(ValidacionTipos):

    def __init__(self, tablero: CrearTablero, tablero_pistas: CrearTablero) -> None:
        self.validar_tipos(CrearTablero, tablero)
        self.validar_tipos(CrearTablero, tablero_pistas)
        self.__tablero = tablero.tablero
        self.__tablero_pistas = tablero_pistas.tablero

    def print_tablero(self):

        for i in range(len(self.__tablero)):

            for j in range(len(self.__tablero[i])):

                print(
                    f"{fore(self.__tablero[i][j][1])}{self.__tablero[i][j][0]}{Style.reset} ",
                    end=" ",
                )

            for j in range(len(self.__tablero[i])):

                print(
                    f"{    fore(self.__tablero_pistas[i][j][1])}{self.__tablero_pistas[i][j][0]}{Style.reset}",
                    end=" ",
                )

            print()


tablero1.cambiar_color_fila(2,["red", "blue", "green", "cyan", "red"])
Printeo = PrintTableros(tablero=tablero1, tablero_pistas=tablero2)
Printeo.print_tablero()
