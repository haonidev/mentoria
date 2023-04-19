class RoboLucas(BaseRobo):
    
    def __init__(self, Modelo: str, braco_esquerdo: any, braco_direito: any, perna_esquerda: any, perna_direita: any):
        self.braco_esquerdo = braco_esquerdo
        self.braco_direito = braco_direito
        self.perna_esquerda = perna_esquerda
        self.perna_direita = perna_direita
    
        self.hitpoint = 10
  
    def bater_com_braco_esquerdo(self, robo):
        print("Soco com o braco esquerdo")
        robo.hitpoint -= 3

    def bater_com_braco_direito(self, robo):
        print("Soco com o braco direito")
        robo.hitpoint -= 3

    def bater_com_perna_esquerda(self, robo):
        print("Soco com o perna esquerda")
        robo.hitpoint -= 2

    def bater_com_perna_direita(self, robo):
        print("Soco com o perna direita")
        robo.hitpoint -= 2

# Hora da porrada
robo_lucas = RoboLucas(Modelo = "Megazord")