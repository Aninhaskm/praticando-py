"""Sabor Express - Aplicativo de Cadastro de Restaurantes"""
import os

restaurantes = []
# Variável global: uma variável que pode ser acessada em qualquer parte do código

def exibir_nome_do_app():
    """Exibe o nome do aplicativo na tela."""
    print("Sabor Express\n")

def exibir_opcoes():
    """Exibe as opções do menu principal para o usuário."""
    print("Escolha uma opção:")
    print("1. Cadastrar Restaurante")
    print("2. Listar Restaurantes")
    print("3. Ativar Restaurante")
    print("4. Sair\n")

# função: um bloco de código que vai realizar uma determinada ação
def finalizar_app():
    """Limpa a tela e exibe mensagem de finalização do aplicativo."""
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Finalizando o aplicativo...\n")

def opcao_invalida():
    """Exibe mensagem de opção inválida e retorna ao menu principal."""
    print("Opção inválida.\n")
    input("Pressione Enter para voltar ao menu principal.")
    main()

def cadastrar_restaurante():
    """
    Solicita os dados do restaurante ao usuário, cadastra como inativo
    e retorna ao menu principal.
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Cadastrar Restaurante")

    nome = input("Digite o nome do restaurante: ")
    endereco = input("Digite o endereço do restaurante: ")
    telefone = input("Digite o telefone do restaurante: ")
    restaurantes.append({
        "nome": nome,
        "endereco": endereco,
        "telefone": telefone,
        "ativo": False
    })

    print(f"Restaurante {nome} cadastrado com sucesso! (Status: Inativo)\n")
    input("Pressione Enter para voltar ao menu principal.")
    main()

def listar_restaurantes():
    """Lista todos os restaurantes cadastrados e seus status (Ativo/Inativo)."""
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Listar Restaurantes")

    if len(restaurantes) == 0:
        print("Nenhum restaurante cadastrado.\n")
    else:
        for i, restaurante in enumerate(restaurantes):
            status = "Ativo" if restaurante.get("ativo") else "Inativo"
            print(f"{i + 1}. {restaurante['nome']} (Status: {status})")

    input("Pressione Enter para voltar ao menu principal.")
    main()

def ativar_restaurante():
    """
    Permite ao usuário ativar um restaurante cadastrado,
    alterando seu status para Ativo.
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Ativar Restaurante")

    if len(restaurantes) == 0:
        print("Nenhum restaurante cadastrado.\n")
    else:
        for i, restaurante in enumerate(restaurantes):
            status = "Ativo" if restaurante.get("ativo") else "Inativo"
            print(f"{i + 1}. {restaurante['nome']} (Status: {status})")
        try:
            opcao = int(input("Escolha o número do restaurante que deseja ativar: "))

            if 1 <= opcao <= len(restaurantes):
                restaurantes[opcao - 1]["ativo"] = True
                print(f"Restaurante {restaurantes[opcao - 1]['nome']} ativado com sucesso!\n")
            else:
                print("Opção inválida.\n")

        except ValueError:
            print("Entrada inválida. Por favor, insira um número.\n")

    input("Pressione Enter para voltar ao menu principal.")
    main()

def escolher_opcao():
    """Lê a opção do usuário e executa a função correspondente do menu."""
    try:
        opcao_escolhida = int(input("Escolha uma opção: "))

        if opcao_escolhida == 1:
            cadastrar_restaurante()

        elif opcao_escolhida == 2:
            listar_restaurantes()

        elif opcao_escolhida == 3:
            ativar_restaurante()

        elif opcao_escolhida == 4:
            finalizar_app()

        else:
            opcao_invalida()
    except ValueError:
        opcao_invalida()

def main():
    """Função principal que inicia o aplicativo."""
    exibir_nome_do_app()
    exibir_opcoes()
    escolher_opcao()

if __name__ == "__main__":
    main()
