
from strategy_example.Exercicio.robo import BaseRobo


class Arena():


    def __init__(self, robo_vermelho: BaseRobo, robo_azul: BaseRobo) -> None:
        self.robo_vermelho = robo_vermelho
        self.robo_azul = robo_azul


    def temos_um_vencedor(self):
        if self.robo_vermelho.hitpont <= 0:
            print("O robo azul venceu a luta")
            return True
        elif self.robo_azul.hitpont <= 0:
            print("O robo vermelho venceu a luta")
            return True
        
        return False

    def fight(self):
        while True:
            self.robo_vermelho.bater_com_braco_esquerdo(self.robo_azul)
            self.robo_azul.bater_com_braco_esquerdo(self.robo_vermelho)
            if self.temos_um_vencedor():
                break

            self.robo_vermelho.bater_com_braco_direito(self.robo_azul)
            self.robo_azul.bater_com_braco_direito(self.robo_vermelho)
            if self.temos_um_vencedor():
                break

            self.robo_vermelho.chutar_com_perna_direita(self.robo_azul)
            self.robo_azul.chutar_com_perna_direita(self.robo_vermelho)
            if self.temos_um_vencedor():
                break

            self.robo_vermelho.chutar_com_perna_esquerda(self.robo_azul)
            self.robo_azul.chutar_com_perna_esquerda(self.robo_vermelho)
            if self.temos_um_vencedor():
                break

            print(f"O robo vermelho tem {self.robo_vermelho.hitpont} de vida")
            print(f"O robo azul tem {self.robo_azul.hitpont} de vida")


