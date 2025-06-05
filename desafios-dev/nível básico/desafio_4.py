"""
Desafio 4 - Gerador de senhas 
Este módulo gera senhas aleatórias,
Com base em caracteres alfanuméricos e símbolos especiais.
"""

import random  # Importa o módulo random para gerar números aleatórios
import string  # Importa o módulo string para manipulação de strings

# Classe utilitária: é uma classe que só tem métodos estáticos e não precisa ser instanciada
# Método estático: Não depende de atributos da instância self. Apenas executa uma função,
# geralmente útil para lógica independente de estado.
class GeradorSenha:
    """
    Classe para gerar senhas aleatórias.
    """
    @staticmethod
    def generate_password(tamanho=8):
        """
        Método estático para gerar uma senha aleatória.
        Gera uma senha aleatória com o tamanho especificado.
        """
        # Define uma string com todas as letrars, dígitos e símbolos especiais
        # string.ascii_letters: letras maiúsculas e minúsculas
        caracteres = string.ascii_letters + string.digits + string.punctuation
        # Gera a senha aleatória escolhendo para cada posição,
        # um caractere aleatório da string de caracteres
        # ''.join(): junta os caracteres gerados em uma única string
        senha = ''.join(random.choice(caracteres) for _ in range(tamanho))

        return senha

# Chama o método estático da classe GeradorSenha para gerar uma senha de 12 caracteres
# O valor padrão é 8, mas pode ser alterado para qualquer valor desejado
senha = GeradorSenha.generate_password(12)
print(f"\nA senha gerada é: {senha}", "\n")
