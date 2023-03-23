from TipoCarro import TipoCarro 
from Inventario import Inventario

class Carro(TipoCarro,Inventario) :

    contador = 0;

    def __init__(self,tipo,uso,descripcion,modelo,marca,color,placa,unidades,sucursal):
        TipoCarro.__init__(self,tipo,uso,descripcion)
        Inventario.__init__(self,unidades,sucursal)
        self.__modelo = modelo
        self.__marca = marca
        self.__color = color
        self.__placa = placa
        Carro.contador += 1

    #GETTERS

    def getModelo(self):
        return self.__modelo
    
    def getMarca(self):
        return self.__marca
    
    def getColor(self):
        return self.__color
    
    def getPlaca(self):
        return self.__placa
    
    #SETTERS

    def setModelo(self, modelo) :
        self.__modelo = modelo

    def setMarca(self, marca) :
        self.__marca = marca

    def setColor(self, color): 
        self.__color = color

    def setPlaca(self, placa) :
        self.__placa = placa 