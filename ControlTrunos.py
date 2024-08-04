
from ValidacionTipos import ValidacionTipos
from CrearTablero import CrearTablero


class ControlTurnos(ValidacionTipos):
    def __init__(
        self, tablero_pistas: CrearTablero, tablero_principal: CrearTablero, Adivinar: list[str]
    ) -> None:
        self.validar_tipos(CrearTablero, tablero_pistas)
        self.validar_tipos(CrearTablero, tablero_principal)
        self.validar_tipos(list, Adivinar)
        self.validar_tipos_lista(str, Adivinar)
        self.__tablero_pistas = tablero_pistas
        self.__tablero_principal = tablero_principal
        self.__limite_turnos = len(tablero_pistas.tablero)
        self.__lista_colores = Adivinar
        self.__turnos:list[list[str]] | list[None] = []
        self.__pistas:list[list[str]] | list[None] = []
        self.__turnos_pasados = 0
       

    def agregar_jugadas(self, colores: list[str]) -> None:
        self.validar_tipos(list, colores)
        self.__turnos.append(colores)
        self.__turnos_pasados = len(self.__turnos)
        self.__tablero_principal.cambiar_color_fila(self.__turnos)

    def agregar_pistas(self) -> None:
        
        resultado:list[str] = []
        
        for x in range(len(self.__lista_colores)):
            if self.__lista_colores[x] == self.__turnos[self.turnos_pasados - 1][x]:
                resultado.append("green")
            elif self.__turnos[self.turnos_pasados - 1][x] in self.__lista_colores:
                resultado.append("yellow")
            else:
                resultado.append("white")

        self.__pistas.append(resultado)
        self.__tablero_pistas.cambiar_color_fila(self.__pistas)

    def verificar_final(self) -> bool:
        fin_del_juego = False
        for i in self.__turnos:
            if (
                self.__lista_colores == i
                or self.__limite_turnos == self.__turnos_pasados
            ):
                fin_del_juego = True
                self.__turnos = []
                self.__pistas = []

        return fin_del_juego

    @property
    def turnos(self) -> list[list[str]] | list[None]:
        return self.__turnos

    @property
    def turnos_pasados(self) -> int:
        return self.__turnos_pasados

    @property
    def limite(self) -> int:
        return self.__limite_turnos





# def prueba():
#     Printeo.print_tablero()
#     while True:
#         respuesta_jugador = input("tus colores: ").strip()
#         myList = respuesta_jugador.split()
#         juego1.agregar_jugadas(myList)
        
#         juego1.agregar_pistas()
#         Printeo.print_tablero()

#         print(juego1.limite)
#         print(juego1.turnos_pasados)

#         if juego1.verificar_final():
#             break

# prueba()
