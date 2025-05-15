""" 
Desafio 5 - Conversor de temperatura com Factory Simples
Este módulo converte temperaturas entre Celsius, Fahrenheit e Kelvin.
"""

# °F = (°C × 9/5) + 32
# °C = (°F − 32) × 5/9
# °K = °C + 273.15
# °C = °K - 273.15
# °F = °K × 9/5 - 459.67
# °K = (°F + 459.67) × 5/9
class Fahrenheit:
    def converter_para(self, valor):
        """
        Método para converter Fahrenheit para Celsius.
        """
        return (valor - 32) * 5/9

class Kelvin:
    def converter_para(self, valor):
        """
        Método para converter Kelvin para Celsius e Fahrenheit.
        """
        return valor - 273.15

class ConversorFactory:
    """
    Classe de fábrica para criar conversores de temperatura.
    """
    @staticmethod
    def obter_conversor(tipo):
        """
        Método estático para obter o conversor de temperatura apropriado.
        """
        if tipo == "Fahrenheit":
            return Fahrenheit()
        elif tipo == "Kelvin":
            return Kelvin()
        else:
            return None

print("\nConversor de Temperatura", "\n")

while True:
    tipo = input("Digite o tipo de temperatura de origem (Fahrenheit ou Kelvin): ")
    conversor = ConversorFactory.obter_conversor(tipo)
    if conversor:
        break
    else:
        print("Tipo de conversor inválido. Escolha Fahrenheit ou Kelvin!", "\n")

while True: 
    valor = float(input(f"Digite o valor em {tipo}: "))
    resultado = conversor.converter_para(valor)
    print(f"O valor em Celsius é: {resultado:.2f}°C", "\n")
    exit()