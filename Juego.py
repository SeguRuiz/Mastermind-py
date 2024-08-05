import time
import random
from ValidacionTipos import ValidacionTipos
from ControlTrunos import ControlTurnos
from PrintearTablero import PrintTableros
from CrearTablero import CrearTablero
from Bot import Bot


class Juego(ValidacionTipos):
    def __init__(self, intentos: int) -> None:
        self.__bot = Bot(["red", "green", "yellow", "blue", "cyan", "black", "white"],5)
        self.__tablero_principal = CrearTablero("O", intentos)
        self.__tablero_pistas = CrearTablero("o", intentos)
        self.__mostrar_tableros = PrintTableros(
            self.__tablero_principal, self.__tablero_pistas
        ).print_tablero
        self.__control_juego = ControlTurnos(
            self.__tablero_pistas, self.__tablero_principal, self.__bot.bot_respuesta
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
        while True:
           print('Deseas jugar como adivinador o que el bot adivine?')
           respuesta = input('a: ser adivinador, b: que el bot adivine, q: para salirse: ').lower()
        
           if respuesta not in ['a', 'b', 'q']:
               print('La respuesta no es valida')
            
           if respuesta == 'q':
               break
        
           if respuesta == 'a':
               self.__juego_defecto()
        
           
    def __juego_defecto(self) -> None:
        while not self.__control_juego.verificar_final():
            colores_jugador = input("Indica tus colores: ").strip().lower().split()

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

    
    def __juego_bot(self):
        
        pass
    
    def __comprobar_colores(self, colores: list[str]) -> bool:
        combinacion_no_permitida = False
        for i in colores:
            if (
                i not in ["red", "green", "yellow", "blue", "cyan", "black", "white"]
                or len(colores) != 5
            ):
                combinacion_no_permitida = True

        return combinacion_no_permitida


nuevo_juego = Juego(12)
nuevo_juego.iniciar_juego()
