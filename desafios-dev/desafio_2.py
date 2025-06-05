from typing import List
from abc import ABC, abstractmethod

class ContaBancaria(ABC):
    def __init__(self, numero: str, titular: str, saldo: float):
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo

        if saldo < 0:
            raise ValueError("O saldo não pode ser negativo")
        if titular == "":
            raise ValueError("O titular não pode ser vazio")

    def get_info(self) -> str:
        return f"Conta {self.__numero}, Titular: {self.__titular}, Saldo: R$ {self.__saldo:.2f}"
    
    def get_saldo(self) -> float:
        return self.__saldo
    
    def set_saldo(self, novo_saldo: float) -> None:
        self.__saldo = novo_saldo

    @abstractmethod
    def sacar(self, valor: float) -> bool:
        pass

class ContaCorrente(ContaBancaria):
    def sacar(self, valor: float) -> bool:
        if valor <= self.get_saldo() + 500:
            self.set_saldo(self.get_saldo() - valor)
            return True
        return False

class ContaPoupanca(ContaBancaria):
    def sacar(self, valor: float) -> bool:
        if valor <= 0:
            raise ValueError("O valor do saque não pode ser negativo")
        if valor > self.get_saldo():
            return False
        self.set_saldo(self.get_saldo() - valor)
        return True

class Banco:
    def __init__(self, contas: List[ContaBancaria]):
        self.__contas = contas

    def adicionar_conta(self, conta: ContaBancaria) -> None:
        self.__contas.append(conta)

    def mostrar_saldos(self) -> None:
        for conta in self.__contas:
            print(conta.get_info())

