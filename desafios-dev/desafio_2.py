# desafio 2 - Simulador de Conta Bancária

class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor:.2f} realizado com sucesso!")
        else:
            print("Valor de depósito inválido.")

    def sacar(self, valor):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado com sucesso!")
        else:
            print("Valor de saque inválido ou saldo insuficiente.")
    
    def exibir_saldo(self):
        print(f"Saldo atual: R${self.saldo:.2f}")

if __name__ == "__main__":
    conta = ContaBancaria()
    while True:
        print("\nMenu:")
        print("1. Depositar")
        print("2. Sacar")
        print("3. Exibir Saldo")
        print("4. Sair", "\n")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            valor = float(input("Digite o valor a depositar: "))
            conta.depositar(valor)
        elif opcao == "2":
            valor = float(input("Digite o valor a sacar: "))
            conta.sacar(valor)
        elif opcao == "3":
            conta.exibir_saldo()
        elif opcao == "4":
            break
        else:
            print("Opção inválida.")
