from TipoCarro import TipoCarro
from Carro import Carro

tipo_carro = TipoCarro("Camioneta","Carga","Vehículo de doble tracción")

# tipo_carro.setTipo("Camion")
# tipo_carro.setUso("Transporte de carga pesada")
# tipo_carro.setDescripcion("Esta es la descripción del camión")

# print("*** Tipo de carro *** ")
# print("---------------------------")

# print(tipo_carro.getTipo())
# print(tipo_carro.getUso())
# print(tipo_carro.getDescripcion())

# print("---------------------------")

print("*** Carro *** ")

carro = Carro("camioneta","Transporte","Vehículo familiar",2023,"Foton","Azul","ERT-567","10","Principal")

print(carro.getModelo())
print(carro.getMarca())
print(carro.getColor())
print(carro.getPlaca())
print(carro.getTipo())
print(carro.getUso())
print(carro.getDescripcion())
print(carro.getUnidades())
print(carro.getSucursal())


print(Carro.contador)


# print("Tipo = " +)
print("---------------------------")

