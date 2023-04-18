


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
 
    def bater_com_braco_esquerdo(self, robo):
        self.bater_com_braco_esquerdo(robo)
        

    def bater_com_braco_direito(self, robo):
        self.bater_com_braco_direito(robo)
        
    
    def chutar_com_perna_direita(self, robo):
        self.chutar_com_perna_direita(robo)


    def chutar_com_perna_esquerda(self, robo):
        self.chutar_com_perna_esquerda(robo)
        