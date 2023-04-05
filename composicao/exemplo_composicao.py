
from abc import ABC, abstractmethod
from composicao.comportamento_de_estudar import ComportamentoDeEstudar, ComportamentoDeEstudarHipnose, ComportamentoDeEstudarIA

from composicao.comportamento_de_trabalho import ComportamentoDeTrabalharComoEngenheiroDeIA, ComportamentoDeTrabalharComoLutier


class PessoaAbstrata(ABC):

    @abstractmethod
    def trabalhar(self):
        pass

    @abstractmethod
    def estudar(self):
        pass


class Fefito(PessoaAbstrata):

    def __init__(self, comportamento_de_trabalhar: ComportamentoDeTrabalharComoLutier, 
                 comportamento_de_estudar: ComportamentoDeEstudar) -> None:
        self.comportamento_de_trabalhar = comportamento_de_trabalhar
        self.comportamento_de_estudar = comportamento_de_estudar

    def trabalhar(self):
        self.comportamento_de_trabalhar.trabalhar()

    def estudar(self):
        self.comportamento_de_estudar.estudar()


class Lucas(PessoaAbstrata):

    def __init__(self, comportamento_de_trabalhar: ComportamentoDeTrabalharComoLutier, 
                 comportamento_de_estudar: ComportamentoDeEstudar) -> None:
        self.comportamento_de_trabalhar = comportamento_de_trabalhar
        self.comportamento_de_estudar = comportamento_de_estudar

    def trabalhar(self):
        self.comportamento_de_trabalhar.trabalhar()

    def estudar(self):
        self.comportamento_de_estudar.estudar()



if __name__ == "__main__":

    Trabalhar_ComoLutier = ComportamentoDeTrabalharComoLutier()
    Estudar_IA = ComportamentoDeEstudarIA()

    TrabalharComoEngenheiroDeIA = ComportamentoDeTrabalharComoEngenheiroDeIA()
    EstudarHipnose = ComportamentoDeEstudarHipnose()

    fefito = Fefito(Trabalhar_ComoLutier, Estudar_IA)

    fefito.trabalhar()
    fefito.estudar()

    fefito.comportamento_de_trabalhar = TrabalharComoEngenheiroDeIA
    fefito.comportamento_de_estudar = EstudarHipnose

    fefito.trabalhar()
    fefito.estudar()

