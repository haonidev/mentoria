


from abc import ABC, abstractmethod


class ComportamentoDeEstudar(ABC):
    
        @abstractmethod
        def estudar(self):
            pass


class ComportamentoDeEstudarIA(ComportamentoDeEstudar):
    
    def estudar(self):
        print("Estudando IA")


class ComportamentoDeEstudarHipnose(ComportamentoDeEstudar):
    
    def estudar(self):
        print("Estudando Hipnose")