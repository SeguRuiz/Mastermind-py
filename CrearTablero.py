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

    def cambiar_color_fila(self, coordenadaY: int, colores: list[str]):
        self.validar_tipos(int, coordenadaY)
        self.validar_tipos(list, colores)
        self.validar_tipos_lista(str, colores)
        if len(colores) > 5:
            print("no se permiten mas de 5 colores")
        else:
            for i in range(len(colores)):
                self.__tablero[coordenadaY][i][1] = colores[i]

    @property
    def tablero(self):
        return self.__tablero


tablero1 = CrearTablero("O", 12)
tablero2 = CrearTablero("?", 12)



