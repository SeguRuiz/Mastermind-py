import random 
from ValidacionTipos import ValidacionTipos
colores_disponibles = ["red", "green", "yellow", "blue", "cyan", "black", "white"]

class Bot(ValidacionTipos):
    def __init__(self, opciones: list, cantidad_respuestas: int) -> None:
        self.validar_tipos(list, opciones)
        self.validar_tipos(int, cantidad_respuestas)
        self.__opciones = opciones
        self.__cantidad_respuestas = cantidad_respuestas

    
    @property
    def bot_respuesta(self):
        return random.sample(self.__opciones, self.__cantidad_respuestas)
        
    
bot1 = Bot(colores_disponibles,5)

