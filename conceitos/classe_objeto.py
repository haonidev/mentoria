



# classe está para uma receita de bolo, assim como objeto está para o bolo.



class Bolo():

    def __init__(self, massa, recheio, cobertura):
        self.massa = massa
        self.recheio = recheio
        self.cobertura = cobertura

    def cortar_bolo(self):
        print("Cortando o bolo")
    

bolo_de_aniversario = Bolo("chocolate", "brigadeiro", "chocolate")

bolo_de_aniversario.cortar_bolo()
