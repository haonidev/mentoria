


# Criar uma classe de um robo, que possa ser complementada 
# de acordo com as peça que o dono do robo poderá adiquiri futuramente.

class BaseRobo():

    def __init__(self, Modelo: str, braco_esquerdo: any, braco_direito: any, perna_esquerda: any, perna_direita: any):
        self.Modelo = Modelo
        self.braco_esquerdo = braco_esquerdo
        self.braco_direito = braco_direito
        self.perna_esquerda = perna_esquerda
        self.perna_direita = perna_direita

        self.hitpont = 10

    