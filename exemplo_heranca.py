

class Ave:

    def __init__(self, nome: str, cor: str, peso: float, 
                 comprimento_perna_em_metros: float):
        
        self.nome: str = nome
        self.cor: str = cor
        self.peso: float = peso
        self.comprimento_perna_em_metros: float = comprimento_perna_em_metros

    def voar(self):
        print("A ave está voando.")

    def comer(self):
        print("A ave está comendo.")

    def correr(self):
        print("A ave está correndo.")

    def nadar(self):
        print("A ave está nadando.")



class Avestruz(Ave):

    def __init__(self, nome: str, cor: str, peso: float, 
                 comprimento_perna_em_metros: float):
        
        
        super().__init__(nome, cor, peso, comprimento_perna_em_metros)

    def voar(self):
        print("Avestruz não voa.")
        # super().voar()


    def montar(self):
        print("Montei na Avestruz.")

if __name__ == "__main__":
    

    
    avestruz = Ave("Avestruz", "Branco", 100, 1.5)


    selecionar_de_ave = {
        "Avestruz": Avestruz
    }

    ave_builder = selecionar_de_ave["Avestruz"]
    ave = ave_builder("Avestruz", "Branco", 100, 1.5)
    ave.voar()
    ave.comer()
    ave.correr()
    ave.nadar()

    # print(type(ave))

    print(ave.comprimento_perna_em_metros)
