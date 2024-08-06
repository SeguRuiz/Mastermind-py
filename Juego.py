import time
from ValidacionTipos import ValidacionTipos
from ControlTrunos import ControlTurnos
from PrintearTablero import PrintTableros
from CrearTablero import CrearTablero
import time
from Bot import Bot, Bot_2


class Juego(ValidacionTipos):
    def __init__(self, intentos: int) -> None:
        self.validar_tipos(int, intentos)
        self.__colores_permitidos = [
            "red",
            "green",
            "yellow",
            "blue",
            "cyan",
            "black",
            "white",
            "magenta",
        ]
        self.__tablero_principal = CrearTablero("O", intentos)
        self.__tablero_pistas = CrearTablero("o", intentos)
        self.__mostrar_tableros = PrintTableros(
            self.__tablero_principal, self.__tablero_pistas
        ).print_tablero
       
        self.__control_juego = ControlTurnos(
            self.__tablero_pistas,
            self.__tablero_principal,
            Bot(
                self.__colores_permitidos,
                5,
            ).bot_respuesta,
        )

    def iniciar_juego(self):
        print()
        print(
            "Los posibles colores a encontrar son: red, green, yellow, blue, cyan, black, white, magenta"
        )
        print('Los colores pueden ser colocados de est forma: color color color color colo, sin comas solo espacios')
        print(
            "Solo puedes escojer 5 de ellos y esperar que esten en la combinacion oculta"
        )
        print()
        print("Al lado del tablero principal estaran las pistas:")
        print(
            "Verde: el color esta en la posicion correcta, Amarillo: el color esta, pero no en el lugr correcto, Blanco: El color no se encuentra"
        )
        self.__mostrar_tableros()
        while True:
            print("Deseas jugar como adivinador o que el bot adivine?")
            respuesta = input(
                "a: ser adivinador, b: que el bot adivine, q: para salirse: "
            ).lower()

            if respuesta not in ["a", "b", "q"]:
                print("La respuesta no es valida")

            if respuesta == "q":
                break

            if respuesta == "a":
                self.__juego_defecto()

            if respuesta == "b":
                self.__juego_bot()

    def __juego_defecto(self) -> None:
        self.__control_juego = ControlTurnos(
            self.__tablero_pistas,
            self.__tablero_principal,
            Bot(
                self.__colores_permitidos,
                5,
            ).bot_respuesta,
        )
        self.__mostrar_tableros()
        while not self.__control_juego.verificar_final():
            colores_jugador = input("Indica tus colores: ").strip().lower().split()

            if self.__comprobar_colores(colores_jugador):
                print("Intenta denuevo")
            else:
                self.__control_juego.agregar_jugadas(colores_jugador)
                self.__control_juego.agregar_pistas()
                self.__mostrar_tableros()
                self.__Bot_2 = Bot_2(self.__tablero_principal.tablero, self.__tablero_pistas.tablero, len(self.__control_juego.turnos) - 1)
                self.__Bot_2.prueba()

        if self.__control_juego.limite == self.__control_juego.turnos_pasados:
            print("Se acabaron los intentos")
        else:
            print("Ganaste!")

    def __juego_bot(self):
        respuesta = (
            input("indica los colores que debe adivinar el bot: ")
            .strip()
            .lower()
            .split()
        )

        if self.__comprobar_colores(respuesta):
            print("Intenta denuevo")
        else:
            self.__control_juego = ControlTurnos(
                self.__tablero_pistas, self.__tablero_principal, respuesta
            )
            while not self.__control_juego.verificar_final():
                self.__control_juego.agregar_jugadas(
                   Bot_2(self.__tablero_principal.tablero, self.__tablero_pistas.tablero, len(self.__control_juego.turnos)).prueba()
                )
                self.__control_juego.agregar_pistas()
                self.__mostrar_tableros()
                time.sleep(0.5)
            
            if self.__control_juego.limite == self.__control_juego.turnos_pasados:
                 print("Se acabaron los intentos")
            else:
                 print("El bot adivino")
      

    def __comprobar_colores(self, colores: list[str]) -> bool:
        combinacion_no_permitida = False
        for i in colores:
            if i not in self.__colores_permitidos or len(colores) != 5:
                combinacion_no_permitida = True

        return combinacion_no_permitida


nuevo_juego = Juego(12)
nuevo_juego.iniciar_juego()
