import random 
from ValidacionTipos import ValidacionTipos
colores_disponibles = ["red", "green", "yellow", "blue", "cyan", "black", "white", "magenta"]

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

class Bot_2(ValidacionTipos):
    def __init__(self, tablero_principal, tablero_pistas, intentos_actuales) -> None:
        self.validar_tipos(list, tablero_principal)
        self.validar_tipos(list, tablero_pistas)
        self.validar_tipos(int, intentos_actuales)
        self.__tablero_principal = tablero_principal
        self.__tablero_pistas = tablero_pistas
        self.__intentos_actuales = intentos_actuales
    
    def prueba(self):
       opciones = ["red", "green", "yellow", "blue", "cyan", "black", "white", "magenta"]
       if self.__intentos_actuales == 0:
           return random.sample(["red", "green", "yellow", "blue", "cyan", "black", "white", "magenta"], 5)
       else:
        respuesta = ['white' for n in range(5)]
        for x in range(len(self.__tablero_pistas[self.__intentos_actuales])):
            if self.__tablero_pistas[self.__intentos_actuales - 1][x][1] == 'green':
                respuesta[x] =  self.__tablero_principal[self.__intentos_actuales - 1][x][1]
            else:
                respuesta[x] = random.choice(opciones)
                  
                
        
        return respuesta

        

    
    
    