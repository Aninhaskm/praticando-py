from typing import List

class Veiculo:
    def __init__(self, placa: str, modelo: str, consumo_medio: float):
        self.__placa = placa
        self.__modelo = modelo
        self.__consumo_medio = consumo_medio

        if consumo_medio <= 0:
            raise ValueError("O consumo médio deve ser maior que 0")
        if placa == "":
            raise ValueError("A placa não pode ser vazia")
        if modelo == "":
            raise ValueError("O modelo não pode ser vazio")
        
    def get_info(self) -> str:
        return f"Placa: {self.__placa}, Modelo: {self.__modelo}, Consumo Médio: {self.__consumo_medio} km/l"

    def calcular_custo_viagem(self, distancia: float, preco_combustivel: float) -> float:
        return distancia / self.__consumo_medio * preco_combustivel

class Carro(Veiculo):
    def __init__(self, placa: str, modelo: str, consumo_medio: float):
        super().__init__(placa, modelo, consumo_medio)

    def calcular_custo_viagem(self, distancia: float, preco_combustivel: float) -> float:
        custo_base = super().calcular_custo_viagem(distancia, preco_combustivel)
        return custo_base * 0.7

class Moto(Veiculo):
    def __init__(self, placa: str, modelo: str, consumo_medio: float):
        super().__init__(placa, modelo, consumo_medio)

    def calcular_custo_viagem(self, distancia: float, preco_combustivel: float) -> float:
        custo_base = super().calcular_custo_viagem(distancia, preco_combustivel)
        return custo_base * 0.5

class Caminhao(Veiculo):
    def __init__(self, placa: str, modelo: str, consumo_medio: float):
        super().__init__(placa, modelo, consumo_medio)

    def calcular_custo_viagem(self, distancia: float, preco_combustivel: float) -> float:
        custo_base = super().calcular_custo_viagem(distancia, preco_combustivel)
        return custo_base * 0.9

class Frota:
    def __init__(self, veiculos: List[Veiculo]):
        self.veiculos = veiculos

    def gerar_relatorio_custos(self, distancia: float, preco_combustivel: float) -> None:
        for veiculo in self.veiculos:
            custo = veiculo.calcular_custo_viagem(distancia, preco_combustivel)
            print(f"Veiculo: {veiculo.get_info()}, Custo da viagem: R$ {custo:.2f}")








        

        
