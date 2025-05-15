# desafio 1 - Cadastro de Usuários
import os # Importa o módulo os usado para comandos do sistema operacional, como limpar a tela

# Classe: é uma "fábrica" que define como criar objetos (instâncias) com atributos e métodos específicos
# Objeto: é uma instância de uma classe, que possui seus próprios valores para os atributos definidos na classe
# Analogia: Classe = molde de bolo Objeto = bolo pronto. Você pode fazer vários bolos (objetos) a partir do mesmo molde (classe), cada um com seus próprios ingredientes (dados)

"""Criar um sistema para cadastrar e listar usuários em memória"""
class Usuario: # Define a classe Usuario, que representa cada usuário cadastrado
    """Classe que representa um usuário do sistema."""
    def __init__(self, nome, idade, email): # método init para inicializar os atributos do usuário
        """
        Inicializa um novo usuário.

        Args:
            nome (str): Nome do usuário.
            idade (str): Idade do usuário.
            email (str): Email do usuário.
        """
        self.nome = nome
        self.idade = idade
        self.email = email
        self.ativo = False  # Inicialmente o usuário é inativo

    def ativar(self):
        """Ativa o usuário."""
        self.ativo = True

    def desativar(self):
        """Desativa o usuário."""
        self.ativo = False

    def __str__(self): # método que define como o usuário será exibido ao ser impresso, mostrando todos os dados e o status
        """Retorna uma representação em string do usuário, incluindo status."""
        status = "Ativo" if self.ativo else "Inativo"
        return f"Nome: {self.nome}, Idade: {self.idade}, Email: {self.email}, Status: {status}"

class CadastroUsuarios: # classe que gerencia todos os usuários cadastrados
    """Classe para gerenciar o cadastro de usuários em memória."""
    def __init__(self): # inicializa uma lista vazia para armazenar os usuários
        """Inicializa o cadastro com uma lista vazia de usuários."""
        self.usuarios = []

    def cadastrar_usuario(self, nome, idade, email): # cria um novo usuário e adiciona à lista de usuários
        """
        Cadastra um novo usuário como inativo.

        Args:
            nome (str): Nome do usuário.
            idade (str): Idade do usuário.
            email (str): Email do usuário.
        """
        usuario = Usuario(nome, idade, email)
        self.usuarios.append(usuario)
        print(f"Usuário {nome} cadastrado com sucesso! (Status: Inativo)")
        input("Pressione Enter para continuar...")

    def listar_usuarios(self): # lista todos os usuários cadastrados, mostrando o índice e os dados, se não houver usuário, exibe uma mensagem apropriada
        """Lista todos os usuários cadastrados e seus status."""
        if not self.usuarios:
            print("Nenhum usuário cadastrado.")
        else:
            for i, usuario in enumerate(self.usuarios):
                print(f"{i + 1}. {usuario}")

    def ativar_usuario(self, indice):
        """
        Ativa o usuário pelo índice informado.

        Args:
            indice (int): Índice do usuário na lista.
        """
        if 0 <= indice < len(self.usuarios):
            self.usuarios[indice].ativar()
            print(f"Usuário {self.usuarios[indice].nome} ativado com sucesso!")
        else:
            print("Índice inválido.")

    def desativar_usuario(self, indice):
        """
        Desativa o usuário pelo índice informado.

        Args:
            indice (int): Índice do usuário na lista.
        """
        if 0 <= indice < len(self.usuarios):
            self.usuarios[indice].desativar()
            print(f"Usuário {self.usuarios[indice].nome} desativado com sucesso!")
        else:
            print("Índice inválido.")
 
if __name__ == "__main__":
    cadastro = CadastroUsuarios() # Criando/instanciando um objeto chamado cadastro a partir da classe CadastroUsuarios
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Menu Principal", "\n")
        print("Escolha uma opção:")
        print("1. Cadastrar Usuário")
        print("2. Listar Usuários")
        print("3. Ativar Usuário")
        print("4. Desativar Usuário")
        print("5. Sair", "\n")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Digite o nome do usuário: ")
            idade = input("Digite a idade do usuário: ")
            email = input("Digite o email do usuário: ")
            cadastro.cadastrar_usuario(nome, idade, email)
        elif opcao == "2":
            cadastro.listar_usuarios()
            input("Pressione Enter para continuar...")
        elif opcao == "3":
            cadastro.listar_usuarios()
            indice = int(input("Escolha o número do usuário que deseja ativar: ")) - 1
            cadastro.ativar_usuario(indice)
            input("Pressione Enter para continuar...")
        elif opcao == "4":
            cadastro.listar_usuarios()
            indice = int(input("Escolha o número do usuário que deseja desativar: ")) - 1
            cadastro.desativar_usuario(indice)
            input("Pressione Enter para continuar...")
        elif opcao == "5":
            break
        else:
            print("Opção inválida.")
