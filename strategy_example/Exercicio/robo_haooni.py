


from robo import BaseRobo


class RoboHaoni(BaseRobo):

    def __init__(self, Modelo):
        super().__init__(Modelo, None, None, None, None)


    def bater_com_braco_direito(self, robo) :
        print("Soco realmente sério!")
        robo.hitpoint -= 3
    
    def bater_com_braco_esquerdo(self, robo):
        print("Soco sério!")
        robo.hitpoint -= 3
    
    def chutar_com_perna_direita(self, robo):
        print("Chute forte com a perna!")
        robo.hitpoint -= 2
    
    def chutar_com_perna_esquerda(self, robo):
        print("Chute forte com a perna!")
        robo.hitpoint -= 2
    

if __name__ == "__main__":

    eu_robo = RoboHaoni("Haoni")

    eu_robo.bater_com_braco_direito(eu_robo)