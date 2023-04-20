
import random
from robo import BaseRobo
from robo_felipe import RoboZim
from robo_haooni import RoboHaoni
from robolucas import RoboLucas

class Arena():

    def __init__(self, robo_vermelho: BaseRobo, robo_azul: BaseRobo) -> None:
        self.robo_vermelho:BaseRobo = robo_vermelho
        self.robo_azul:BaseRobo = robo_azul

        

    def temos_um_vencedor(self):
        if self.robo_vermelho.hitpoint <= 0:
            print(f"O robo {self.robo_azul.Modelo} venceu a luta")
            return True
        elif self.robo_azul.hitpoint <= 0:
            print(f"O robo {self.robo_vermelho.Modelo} venceu a luta")
            return True
        
        return False

    def fight(self):

        while True:
            ataque, defesa = self.iniciativa()
            ataque.bater_com_braco_esquerdo(defesa)
            if self.temos_um_vencedor():
                print(f"O robo {ataque.Modelo} tem {ataque.hitpoint} de vida")
                print(f"O robo {defesa.Modelo} tem {defesa.hitpoint} de vida")
                break

            ataque, defesa = self.iniciativa()
            ataque.bater_com_braco_direito(defesa)
            if self.temos_um_vencedor():
                print(f"O robo {ataque.Modelo} tem {ataque.hitpoint} de vida")
                print(f"O robo {defesa.Modelo} tem {defesa.hitpoint} de vida")
                break

            ataque, defesa = self.iniciativa()
            ataque.chutar_com_perna_direita(defesa)
            if self.temos_um_vencedor():
                print(f"O robo {ataque.Modelo} tem {ataque.hitpoint} de vida")
                print(f"O robo {defesa.Modelo} tem {defesa.hitpoint} de vida")
                break

            ataque, defesa = self.iniciativa()
            ataque.chutar_com_perna_esquerda(defesa)
            if self.temos_um_vencedor():
                print(f"O robo {ataque.Modelo} tem {ataque.hitpoint} de vida")
                print(f"O robo {defesa.Modelo} tem {defesa.hitpoint} de vida")
                break


    def iniciativa(self):
        self.oponentes = [self.robo_vermelho, self.robo_azul]

        x = random.randint(0, 1)
        ataque = self.oponentes[x]

        self.oponentes.remove(ataque)

        defesa = self.oponentes[0]

        return ataque,defesa



if __name__ == "__main__":

    roboHaoni = RoboHaoni("RoboHaoni")
    roboZim = RoboZim()

    roboLucas = RoboLucas("RoboLucas", None, None, None, None)

    arena = Arena(roboLucas, roboHaoni)
    arena.fight()