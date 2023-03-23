class TipoCarro :
    
    def __init__(self, tipo, uso, descripcion):
        self.__tipo = tipo
        self.__uso = uso
        self.__descripcion = descripcion

    #GETTERS

    def getTipo(self):
        return self.__tipo
    
    def getUso(self):
        return self.__uso
    
    def getDescripcion(self):
        return self.__descripcion
    
    #SETTERS

    def setTipo(self,tipo):
        self.__tipo = tipo

    def setUso(self, uso) :
        self.__uso = uso

    def setDescripcion(self, descripcion) :
        self.__descripcion = descripcion

    # def getDetalles(self) :
    #     detalles = {
    #         "tipo" : self.__tipo,
    #         "uso" : self.__uso,
    #         "descripcion": self.__descripcion
    #     }
    #     return detalles