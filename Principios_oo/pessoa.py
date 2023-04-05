
class Pessoa:

    def __init__(self) -> None:
        pass


    def lavar(self, objeto):
        # //prepara os instrumentos

        # //prepara o objeto

        # //lava o objeto

        # //seca o objeto

        # //guarda os instrumentos
        print("Tá lavado")

class Pedreiro(Pessoa):
    
        def __init__(self) -> None:
            super().__init__()
    
        def construir(self, objeto):
            # //prepara os instrumentos
    
            # //prepara o objeto
    
            # //constrói o objeto
    
            # //guarda os instrumentos
            print("Tá construído")


class Medico():
        
            def __init__(self, pessoa: Pessoa) -> None:
                super().__init__()

                self.pessoa = pessoa

                
        
            def atender(self, objeto):

                # //prepara os instrumentos
        
                # //prepara o objeto
        
                # //atende o objeto
        
                # //guarda os instrumentos
                print("Tá atendido")

            def lavar(self, objeto):
                print("Modo de médico lavar ativado")
                self.pessoa.lavar(objeto)


if __name__ == "__main__":



    pedreiro = Pedreiro()
    pedreiro.lavar("casa")

    medico = Medico(pedreiro)
    medico.lavar("paciente")


    pessoa = Pessoa()
    pessoa.lavar(pedreiro)