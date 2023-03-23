class Inventario: 

    def __init__(self,unidades,sucursal):
        self.__unidades = unidades
        self.__sucursal = sucursal

    def getUnidades(self):
        return self.__unidades
    
    def getSucursal(self):
        return self.__sucursal
    
    def setUnidades(self, unidades):
        self.__unidades = unidades

    def setSucursal(self, sucursal):
        self.__sucursal = sucursal