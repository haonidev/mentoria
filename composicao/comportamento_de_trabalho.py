

from abc import ABC, abstractmethod


class ComportamentoDeTabalhar(ABC):

    @abstractmethod
    def trabalhar(self):
        pass


class ComportamentoDeTrabalharComoLutier(ComportamentoDeTabalhar):

    def trabalhar(self):
        print("Trabalhando como Lutier")


class ComportamentoDeTrabalharComoEngenheiroDeIA(ComportamentoDeTabalhar):

    def trabalhar(self):
        print("Trabalhando como Engenheiro de IA")