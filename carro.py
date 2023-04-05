


class Carro:

    def __init__(self, marca, modelo, cor, ano, preco):

        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
        self.preco = preco


    def andar(self):
        print("O carro está andando.")

    def parar(self):
        print("O carro parou.")

    def virar(self):
        print("O carro virou.")

    def buzinar(self):
        print("O carro está buzina.")




if __main__ == "__main__":

    carro1 = Carro("Fiat", "Uno", "Vermelho", 2010, 20000)