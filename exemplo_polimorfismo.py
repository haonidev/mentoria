from abc import abstractmethod


class ProcessadorImagem:
    @abstractmethod
    def processar(self, imagem):
        pass

    @abstractmethod
    def _carregar(self, imagem):
        pass

    @abstractmethod
    def _converter(self, imagem):
        pass

    @abstractmethod
    def _salvar(self, imagem):
        pass


class ProcessadorImagemJpg(ProcessadorImagem):

    def processar(self, imagem):

        if imagem.endswith('.jpg'):
            imagem = self._carregar(imagem)
            imagem = self._converter(imagem)
            imagem = self._salvar(imagem)
      
        return imagem
    
    def _carregar(self, imagem):
        print('Carregando imagem')
        return imagem

    def _converter(self, imagem):
        print('Convertendo imagem')
        return imagem

    def _salvar(self, imagem):
        print('Salvando imagem')
        return imagem
    
class ProcessadorImagemPng(ProcessadorImagem):

    def processar(self, imagem):

        if imagem.endswith('.png'):
            imagem = self._carregar(imagem)
            imagem = self._converter(imagem)
            imagem = self._salvar(imagem)
      
        return imagem
    
    def _carregar(self, imagem):
        print('Carregando imagem png')
        return imagem

    def _converter(self, imagem):
        print('Convertendo imagem png')
        return imagem

    def _salvar(self, imagem):
        print('Salvando imagem png')
        return imagem
    

class ProcessadorImagemTiff(ProcessadorImagem):

    def processar(self, imagem):

        if imagem.endswith('.tiff'):
            imagem = self._carregar(imagem)
            imagem = self._converter(imagem)
            imagem = self._salvar(imagem)
      
        return imagem
    
    def _carregar(self, imagem):
        print('Carregando imagem tiff')
        return imagem

    def _converter(self, imagem):
        print('Convertendo imagem tiff')
        return imagem

    def _salvar(self, imagem):
        print('Salvando imagem tiff')
        return imagem
    
    
class ProcessadorImagemPdf(ProcessadorImagem):

    def processar(self, imagem):

        if imagem.endswith('.pdf'):
            imagem = self._carregar(imagem)
            imagem = self._converter(imagem)
            imagem = self._salvar(imagem)
      
        return imagem
    
    def _carregar(self, imagem):
        print('Carregando imagem pdf')
        return imagem

    def _converter(self, imagem):
        print('Convertendo imagem pdf')
        return imagem

    def _salvar(self, imagem):
        print('Salvando imagem pdf')
        return imagem

    
class ProcessadorImagemShape(ProcessadorImagem):

    def processar(self, imagem):

        if imagem.endswith('.shape'):
            imagem = self._carregar(imagem)
            imagem = self._converter(imagem)
            imagem = self._salvar(imagem)
      
        return imagem
    
    def _carregar(self, imagem):
        print('Carregando imagem shape')
        return imagem

    def _converter(self, imagem):
        print('Convertendo imagem shape')
        return imagem

    def _salvar(self, imagem):
        print('Salvando imagem shape')
        return imagem


if __name__ == "__main__":

    #    png, jpeg, pdf, shape, etc...
    imagem = 'imagem.tiff'

    selecionador = {
        '.jpg': ProcessadorImagemJpg,
        '.png': ProcessadorImagemPng,
        '.tiff': ProcessadorImagemTiff,
        '.pdf': ProcessadorImagemPdf,
        '.shape': ProcessadorImagemShape,
    }
    
    processador_imagem = selecionador.get(".tiff")()
    
    imagem = processador_imagem.processar(imagem)
    
    print(imagem)