from typing import List
from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, nome: str, idade: int, dono: str):
        self.__nome = nome
        self.__idade = idade
        self.__dono = dono

        if idade < 0:
            raise ValueError("A idade não pode ser negativa")
        if dono == "":
            raise ValueError("O dono não pode ser vazio")
        if nome == "":
            raise ValueError("O nome não pode ser vazio")

    def get_nome(self) -> str:
        return self.__nome
    
    def get_idade(self) -> int:
        return self.__idade
    
    def get_dono(self) -> str:
        return self.__dono

    @abstractmethod
    def emitir_som(self) -> str:
        pass    

class Cachorro(Animal):
    def emitir_som(self) -> str:
        return "Woof!"

class Gato(Animal):
    def emitir_som(self) -> str:
        return "Meow!"

class Papagaio(Animal):
    def emitir_som(self) -> str:
        return "Squawk!"

class PetShop:
    def __init__(self, animais: List[Animal]):
        self.__animais = animais

    def cadastrar_animal(self, animal: Animal) -> None:
        self.__animais.append(animal)

    def exibir_sons(self) -> None:
        for animal in self.__animais:
            print(f"{animal.get_nome()}: {animal.emitir_som()}")

