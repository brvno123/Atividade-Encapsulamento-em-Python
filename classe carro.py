class Carro:
    def __init__(self, modelo):
        self.modelo = modelo
        self.__velocidade = 0  # velocidade inicial

    def acelerar(self, valor):
        if valor > 0:
            self.__velocidade += valor
            print(f"{self.modelo} acelerou em {valor} km/h.")
        else:
            print("Erro: o valor de aceleração deve ser positivo.")

    def frear(self, valor):
        if valor > 0:
            if self.__velocidade - valor < 0:
                self.__velocidade = 0
            else:
                self.__velocidade -= valor
            print(f"{self.modelo} reduziu a velocidade em {valor} km/h.")
        else:
            print("Erro: o valor de frenagem deve ser positivo.")

    def mostrar_velocidade(self):
        return self.__velocidade


carro = Carro("Fusca")

print(f"Modelo: {carro.modelo}")
print(f"Velocidade inicial: {carro.mostrar_velocidade()} km/h")

carro.acelerar(30)
print(f"Velocidade atual: {carro.mostrar_velocidade()} km/h")

carro.acelerar(20)
print(f"Velocidade atual: {carro.mostrar_velocidade()} km/h")

carro.frear(10)
print(f"Velocidade atual: {carro.mostrar_velocidade()} km/h")

carro.frear(50)  # Deve zerar a velocidade
print(f"Velocidade atual: {carro.mostrar_velocidade()} km/h")