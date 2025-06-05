"""
Desafio 2 - Simulador de Conta Bancária
Este módulo permite simular operações básicas de uma conta bancária
"""
import os

class ContaBancaria:
    """Classe que representa uma conta bancária simples."""
    def __init__(self, titular, saldo=0):
        """
        Inicializa uma nova conta bancária.

        Args:
            titular (str): Nome do titular da conta.
            saldo (float, opcional): Saldo inicial da conta. Padrão é 0.
        """
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        """
        Realiza um depósito na conta, se o valor for positivo.

        Args:
            valor (float): Valor a ser depositado.
        """
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor:.2f} realizado com sucesso!")
        else:
            print("Valor de depósito inválido.")

    def sacar(self, valor):
        """
        Realiza um saque na conta, se houver saldo suficiente e o valor for válido.

        Args:
            valor (float): Valor a ser sacado.
        """
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado com sucesso!")
        else:
            print("Valor de saque inválido ou saldo insuficiente.")

    def exibir_saldo(self):
        """Exibe o saldo atual da conta formatado em reais."""
        print(f"Saldo atual: R${self.saldo:.2f}")

if __name__ == "__main__":
    conta = ContaBancaria("Anna Kamimura", 0)
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\nMenu:")
        print("1. Depositar")
        print("2. Sacar")
        print("3. Exibir Saldo")
        print("4. Sair", "\n")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            valor_deposito = float(input("Digite o valor a depositar: "))
            conta.depositar(valor_deposito)
            input("Pressione Enter para voltar ao menu principal ...")
        elif opcao == "2":
            valor_saque = float(input("Digite o valor a sacar: "))
            conta.sacar(valor_saque)
            input("Pressione Enter para voltar ao menu principal ...")
        elif opcao == "3":
            conta.exibir_saldo()
            input("Pressione Enter para voltar ao menu principal ...")
        elif opcao == "4":
            break
        else:
            print("Opção inválida.")
