


class DataSource():

    def get_image(self):
        return "imagem"
    

class ProcessadorImagem():

    def processar(self, imagem):
        return "imagem processada"
    

class S3Bucket():

    def upload(self, imagem):
        print("imagem salva")


class Inicio:


    def __init__(self, data_source: DataSource, processador_imagem: ProcessadorImagem, S3Bucket: S3Bucket) -> None:
        self.data_source = data_source
        self.processador_imagem = processador_imagem
        self.S3Bucket = S3Bucket


    def start(self):

        imagem_data_source = self.data_source.get_image()

        imagem_processada = self.processaoor_imagem.processar(imagem_data_source)

        imagem_salva = self.S3Bucket().upload(imagem_processada)



if __name__ == "__main__":

    programa = Inicio(DataSource(), ProcessadorImagem(), S3Bucket())
    programa.start()


    programa.data_source = DataSource()
    programa.start()