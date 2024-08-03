from colored import Fore, Back, Style, fore, style, back
from ValidacionTipos import ValidacionTipos


class CrearTablero(ValidacionTipos):

    def __init__(self, forma: str, columnas: int) -> None:
        self.validar_tipos(str, forma)
        self.validar_tipos(int, columnas)
        self.__tablero: CrearTablero = []
        self.__forma = forma
        self.__columnas = columnas
        self.__formar_tablero()

    def __formar_tablero(self):

        for x in range(self.__columnas):
            self.__tablero.append(
                [
                    [self.__forma, "white"],
                    [self.__forma, "white"],
                    [self.__forma, "white"],
                    [self.__forma, "white"],
                    [self.__forma, "white"],
                ]
            )

    def cambiar_color_fila(self,colores: list[list] = []):
        self.validar_tipos(list, colores)
        self.validar_tipos_lista(list, colores)
        
        if colores == []:
            print("En espera")
        else:
            for i in range(len(colores)):
                for x in range(len(colores[i])):
                    self.__tablero[i][x][1] = colores[i][x]

    @property
    def tablero(self):
        return self.__tablero




tablero1 = CrearTablero("O", 12)
tablero2 = CrearTablero("o", 12)
