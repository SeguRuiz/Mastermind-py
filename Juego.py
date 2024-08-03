from PrintearTablero import PrintTableros, Printeo
from ValidacionTipos import ValidacionTipos
from CrearTablero import CrearTablero, tablero1, tablero2


class Juego(ValidacionTipos):
    def __init__(
        self,
        printear: PrintTableros,
        tablero_pistas: CrearTablero,
        tablero_principal: CrearTablero,
    ) -> None:
        self.validar_tipos(PrintTableros, printear)
        self.validar_tipos(CrearTablero, tablero_pistas)
        self.__tablero_principal = tablero_principal
        self.__tablero_pistas = tablero_pistas
        self.__limite_turnos = len(tablero_pistas.tablero)
        self.__turnos = []
        self.__pistas = []
        self.__turnos_pasados = 0
        self.__lista_colores = ["red", "red", "red", "red", "yellow"]

    def agregar_turno(self, colores: list[str]):
        self.__turnos.append(colores)
        self.__turnos_pasados = len(self.__turnos)

    def verificar_final(self) -> True:
        if self.__limite_turnos == self.__turnos_pasados:
            return True
        else:
            return False

    def pistas(self):
        resultado = []
        for x in range(len(self.__lista_colores)):
            if self.__lista_colores[x] == self.__turnos[self.turnos_pasados - 1][x]:
                resultado.append("green")
            elif self.__turnos[self.turnos_pasados - 1][x] in self.__lista_colores:
                resultado.append("yellow")
            else:
                resultado.append("black")

        self.__pistas.append(resultado)
        print(self.__pistas)
        self.__tablero_pistas.cambiar_color_fila(self.__pistas)

    @property
    def turnos(self):
        return self.__turnos

    @property
    def turnos_pasados(self):
        return self.__turnos_pasados

    @property
    def limite(self):
        return self.__limite_turnos


juego1 = Juego(Printeo, tablero2, tablero1)


def prueba():
    while True:
        guesses = input("tus colores: ").strip()
        myList = guesses.split()
        juego1.agregar_turno(myList)
        tablero1.cambiar_color_fila(juego1.turnos)
        juego1.pistas()
        Printeo.print_tablero()

        print(juego1.limite)
        print(juego1.turnos_pasados)

        if juego1.verificar_final():
            break


prueba()
