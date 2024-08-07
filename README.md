
En esta ocasion realice un mastermind, utilizando python y usando la estrategia POO,
a continuacion hare un listado de las clases principales y su rol.

## CrearTablero

**Uso general:** Tener un control en la creacion y manipulacion del tablero.

1. Al ser inicializado crea un tablero de 5 columnas y de x filas, dependiendo
del segundo parametro que reciba, encargado de definir la cantidad de columnas.

2. Recibir un array de strings (serian los turnos dados) y en base a eso,
cambiar los colores por defecto de el tablero creado.

3. Reiniciar el tablero a sus colores originales el cual seria 'white'.

## ValidacionTipos

**Uso general:** Ser reutilizable en las otras clases, para no repetir funciones necesarias de validacion tipo.

1. Las demas clases heredan de esta para tener acceso a sus funciones necesarias
en todas estas y no repetirme mucho.

2. Sus dos funciones reciben un tipo de dato y otro a comparar, para asi reutilizarlo
en ls clases que necesiten un tipo de dato en especifico.

## ControlTurnos

**Uso general:** Tener las funciones importantes que el juego necesita para luego ser utilizada después.

1. Recibe dos datos de tipo CrearTablero y una lista de colores a comparar.

2. Agregar una lista de colores escojidos a otra para luego utilizar las funcionalidades
de CrearTablero y cambiar el color de su tablero en especifico.

3. Comparar la lista de los colores escojidos y dependiendo de esto, asignar los diferentes
colores de pista al segundo tablero, utilizando las funciones de CrearTablero.

3. Tener en cuenta el largo de los turnos pasados y si este llega al limite de turnos, define
el fin del juego y reinici los dos tableros junto con las pistas y turnos.

## PrintearTablero

**Uso general:** Recibir dos tableros de CrearTablero y printearlos con su color por defecto.

1. Leer dos tableros, y en base a su par de (forma, color) printear la matriz en forma de tablero.

## Bot

**Uso general:** Retornar un array de colores al ser llamado

1. Cuando el modo de juego es el bot, es utilizado para tomar su respuesta a ControlTurnos.

## Juego

**Uso general:** Contener los dos modos de juegos principales e inicializar el juego.

1. Contener las clases los colores permitiods a escojer, e inicializar las demas clases 
anteriores para ser utilizadas en el flujo del juego.

2. Recibir las espuestas del usuario en cada intento y por me medio de las funciones de ControlTurnos.

3. Dependiendo de la respuesta del usuario inicializar la funcion de juego por defecto o juego con el bot.


## Bot 

**Uso general:** Terner un array random de 5 colores diferentes a disposicion.

1. Es utilizado para definir la lista oculta de colores en cada partida normal del jugador

## Bot_2

**Uso general:** Tomar el rol del bot, cuando este tiene que adivinar.

1. Al ser inicializado recibe los dos tableros, el turno actual, y una lista de colores a no escojer

2. Al ser el primer turno retornara de respuesta un array de colores random y despues de esto comparara sus
elecciones anteriores, como si el color anterior fue correcto para no utilizarlo o si fue un color que no esta
para nunca utilizarlo.

