import uuid



class Produto():

    def __init__(self, nome, marca, preco):

        self.id = uuid.uuid1()
        self.nome = nome
        self.marca = marca
        self.preco = preco

