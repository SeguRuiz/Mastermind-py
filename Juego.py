import random
from ValidacionTipos import ValidacionTipos
from ControlTrunos import ControlTurnos
from PrintearTablero import PrintTableros
from CrearTablero import CrearTablero


class Juego(ValidacionTipos):
    def __init__(self, intentos: int, adivinar: list[str]) -> None:
        self.__tablero_principal = CrearTablero("O", intentos)
        self.__tablero_pistas = CrearTablero("o", intentos)
        self.__mostrar_tableros = PrintTableros(
            self.__tablero_principal, self.__tablero_pistas
        ).print_tablero
        self.__control_juego = ControlTurnos(
            self.__tablero_pistas, self.__tablero_principal, adivinar
        )

    def iniciar_juego(self):
        print()
        print(
            "Los posibles colores a encontrar son: red, green, yellow, blue, cyan, black, white"
        )
        print(
            "Solo puedes escojer 5 de ellos y esperar que esten en la combinacion oculta"
        )
        print()
        print("Al lado del tablero principal estaran las pistas:")
        print(
            "Verde: el color esta en la posicion correcta, Amarillo: el color esta, pero no en el lugr correcto, Blanco: El color no se encuentra"
        )
        self.__mostrar_tableros()

        while not self.__control_juego.verificar_final():
            colores_jugador = input("Inidica tus colores: ").strip().lower().split()

            if self.__comprobar_colores(colores_jugador):
                print("Intenta denuevo")
            else:
                self.__control_juego.agregar_jugadas(colores_jugador)
                self.__control_juego.agregar_pistas()
                self.__mostrar_tableros()

        if self.__control_juego.limite == self.__control_juego.turnos_pasados:
            print("Se acabaron los intentos")
        else:
            print("Hurra ganaste....")

    def __comprobar_colores(self, colores: list[str]) -> bool:
        resultado = False
        for i in colores:
            if (
                i not in ["red", "green", "yellow", "blue", "cyan", "black", "white"]
                or len(colores) != 5
            ):
                resultado = True

        return resultado


nuevo_juego = Juego(12, ["red", "green", "blue", "white", "yellow"])

nuevo_juego.iniciar_juego()
