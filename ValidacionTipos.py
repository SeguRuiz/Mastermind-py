class ValidacionTipos:
    def validar_tipos(self, tipo, *datos):
        for dato in datos:
            if not isinstance(dato, tipo):
                raise TypeError(
                    f"Se espera un dato de tipo: {tipo.__name__}, pero fue recibido: {type(dato).__name__}"
                )

    def validar_tipos_lista(self, tipo, datos: list | tuple):
        for dato in datos:
            if not isinstance(dato, tipo):
                raise TypeError(
                    f"Se espera un dato de tipo: {tipo.__name__}, pero fue recibido: {type(dato).__name__}"
                )
