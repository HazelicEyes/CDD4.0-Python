class Pessoa():
# Classes tem Metodos e Atributos, (Metodos sao Funcoes e Atributos são Variaveis)
    def __init__(self, nomealuno, pesoaluno, idadealuno, comendo=False):
        self.nome = nomealuno
        self.peso = pesoaluno #esses 3 são atributos #atributos usam sempre self, atributos atribuem valores
        self.idade = idadealuno
    def falar(self, falar):
        flagFalar = true
        print(f'{self.nome} esta falando')
    def pararDeFalar(self, falar):
        flagFalar = false
        print(f'{self.nome} parou de falar')

    def comer(self, comida, bebida):
        flagComer = true
        print(f'{self.nome} foi comer {comida} e beber {bebida}')
    def pararDeComer(self, comida, bebida):
        flagComer = false
        print(f'{self.nome} parou de comer')

    def dormir(self, dormir):
        flagDormir = true
        print(f'{self.nome} esta dormindo')
    def acordar(self, acordar):
        flagDormir = false
        print(f'{self.nome} acordou.')
