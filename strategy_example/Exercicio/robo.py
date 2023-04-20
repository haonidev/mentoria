
# Criar uma classe de um robo, que possa ser complementada 
# de acordo com as peça que o dono do robo poderá adiquiri futuramente.

from abc import ABC, abstractmethod


class BaseRobo(ABC):

    def __init__(self, Modelo: str, braco_esquerdo: any, braco_direito: any, perna_esquerda: any, perna_direita: any):
        self.Modelo = Modelo
        self.braco_esquerdo = braco_esquerdo
        self.braco_direito = braco_direito
        self.perna_esquerda = perna_esquerda
        self.perna_direita = perna_direita

        self.hitpoint = 10
 
    @abstractmethod
    def bater_com_braco_esquerdo(self, robo):
        pass
        
    @abstractmethod
    def bater_com_braco_direito(self, robo):
        pass
        
    @abstractmethod
    def chutar_com_perna_direita(self, robo):
        pass

    @abstractmethod
    def chutar_com_perna_esquerda(self, robo):
        pass
