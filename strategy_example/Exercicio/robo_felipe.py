from robo import BaseRobo

def arm_left_power():
    print("Escudo Estrela Do Mar")

def arm_right_power():
    print("Espada Do Mar")

def leg_left_power():
    print("Perna De Siri HighSpeed")

def leg_right_power():
    print("Chute do Molusco")

def montar_robo():
    modelo         = "BobEsponja"
    
    braco_esquerdo = arm_left_power()
    braco_direito  = arm_right_power()
    
    perna_esquerda = leg_left_power()
    perna_direita  = leg_right_power()
    
    base_robo = BaseRobo(modelo,braco_esquerdo, braco_direito, perna_esquerda, perna_direita)
    
    print("Robo Montado")
    return base_robo

def ataques():
    base_bot = montar_robo()
    base_bot.bater_com_braco_esquerdo(base_bot.braco_esquerdo)
    base_bot.hitpoint -= 5
    base_bot.bater_com_braco_direito(base_bot.braco_direito)
    base_bot.hitpoint -= 3
    base_bot.chutar_com_perna_esquerda(base_bot.perna_esquerda)
    base_bot.hitpoint -= 2
    

class RoboZim(BaseRobo):

    def __init__(self):
        super().__init__("RoboZim", None, None, None, None)

    def bater_com_braco_esquerdo(self, robo):
        print("Espada Do Mar")
        robo.hitpoint -= 1

    def bater_com_braco_direito(self, robo):
        print("Escudo Do Mar")
        robo.hitpoint -= 1
        
    def chutar_com_perna_direita(self, robo):
        print("Chute de Lula")
        robo.hitpoint -= 1

    def chutar_com_perna_esquerda(self, robo):
        print("Chute de Arpão")
        robo.hitpoint -= 1
        