
import os

class Contato:
    """
    Classe para representar um contato.
    """
    def __init__(self, nome, telefone, email):
        """
        Inicializa um novo contato. 
        
        Args:
            nome (str): Nome do contato.
            telefone (str): Telefone do contato.
            email (str): Email do contato.
        """
        self.nome = nome
        self.telefone = telefone
        self.email = email

    def __str__(self):
        """
        Retorna uma representação em string do contato.
        """
        return f"Nome: {self.nome}, Telefone: {self.telefone}, Email: {self.email}"
    
class Agenda: 
    """
    Classe para gerenciar uma agenda de contatos.
    """
    def __init__(self):
        """
        Inicializa a agenda com uma lista vazia de contatos.
        """
        self.contatos = []
    
    def adicionar_contato(self, nome, telefone, email):
        """
        Adiciona um novo contato à agenda.
        
        Args:
            nome (str): Nome do contato.
            telefone (str): Telefone do contato.
            email (str): Email do contato.
        """
        contato = Contato(nome, telefone, email)
        self.contatos.append(contato)
        print(f"Contato {nome} adicionado com sucesso!")
        input("Pressione Enter para voltar ao menun principal ...")
    
    def salvar_agenda(self, nome_arquivo):
        """
        Salva a agenda em um arquivo CSV.
        
        Args:
            nome_arquivo (str): Nome do arquivo onde a agenda será salva.
        """
        with open(nome_arquivo, 'w') as arquivo:
            for contato in self.contatos:
                arquivo.write(f"{contato.nome},{contato.telefone},{contato.email}\n")
        print(f"\nAgenda salva em {nome_arquivo} com sucesso!", "\n")
        input("Pressione Enter para voltar ao menu principal...")

    def carregar_agenda(self, nome_arquivo):
        """
        Carrega a agenda de um arquivo CSV.
        
        Args:
            nome_arquivo (str): Nome do arquivo de onde a agenda será carregada.
        """
        if os.path.exists(nome_arquivo):
            self.contatos = [] # Limpa a lista de contatos antes de carregar
            with open(nome_arquivo, 'r') as arquivo:
                for linha in arquivo:
                    nome, telefone, email = linha.strip().split(',')
                    contato = Contato(nome, telefone, email)
                    self.contatos.append(contato)
            print(f"Agenda carregada de {nome_arquivo} com sucesso!", "\n")
            print("Agenda atual: ")
            for contato in self.contatos:
                print(contato)
        else:
            print(f"Arquivo {nome_arquivo} não encontrado.")
        input("\nPressione Enter para voltar ao menu principal...")

if __name__ == "__main__":
    agenda = Agenda()
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\nMenu:")
        print("1. Adicionar contato")
        print("2. Salvar agenda")
        print("3. Carregar agenda")
        print("4. Sair", "\n")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            nome = input("Nome: ")
            telefone = input("Telefone: ")
            email = input("Email: ")
            agenda.adicionar_contato(nome, telefone, email)
        elif opcao == '2':
            nome_arquivo = input("Nome do arquivo para salvar a agenda: ")
            agenda.salvar_agenda(nome_arquivo)
        elif opcao == '3':
            nome_arquivo = input("Nome do arquivo para carregar a agenda: ")
            agenda.carregar_agenda(nome_arquivo)
        elif opcao == '4':
            break
        else:
            print("Opção inválida. Tente novamente.")