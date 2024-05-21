class Atleta:
    def __init__(self):
        self.aposentado = False
        self.peso = 0

    def aposentar(self):
        if self.aposentado == False:
            self.aposentado = True
            print(f'O atleta foi APOSENTADO. Bom descanso.')
        else:
            print(f'O atleta ja esta APOSENTADO.')

    def aquecer(self):
        print(f' O atleta esta AQUECENDO.')

class Corredor(Atleta):
    def __init__(self):
        super().__init__()
    def correr(self):
        print(f' O atleta esta correndo')

class Nadador(Atleta):
    def __init__(self):
        super().__init__()
    def nadar(self):
        print(f' O atleta esta nadando')

class Ciclista(Atleta):
    def __init__(self):
        super().__init__()
    def pedalar(self):
        print(f' O atleta esta pedalando')

class TriAtleta(Corredor, Nadador, Ciclista):
    def __init__(self):
        super().__init__()

#atividade casa = para o atleta fazer qualoquer acao, ele tem que aquecer e nao estar aposentado