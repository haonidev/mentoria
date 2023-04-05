

class Pessoa:

    def __init__(self, nome, idade):

        self.nome = nome

        self.idade = idade

        self.vestimenta = "Nú"



class Seguranca:

    def __init__(self, nome, idade):

        self.nome = nome

        self.idade = idade

        self.vestimenta = "Uniforme"

    def revistar(self, pessoa: Pessoa):

        if pessoa.vestimenta == "Pato":

            print("Pessoa pode entrar.")

        else:

            print("Não pode entrar.")

class Pato:
    
    def __init__(self, nome, idade):

        self.nome = nome

        self.idade = idade

        self.vestimenta = "Pato"



if __name__ == "__main__":

    seguranca = Seguranca("João", 30)

    pessoa = Pessoa("Maria", 20)
    pessoa.vestimenta = "Cisnei"

    outraPessoa = Pato("Pato", 21)
    outraPessoa.vestimenta = "Pato"

    seguranca.revistar(pessoa)
    seguranca.revistar(outraPessoa)



