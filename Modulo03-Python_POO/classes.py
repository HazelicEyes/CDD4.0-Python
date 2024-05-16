class Pessoa():
# Classes tem Metodos e Atributos, (Metodos sao Funcoes e Atributos são Variaveis)
    def __init__(self, nomealuno, pesoaluno, idadealuno, comendo=False):
        self.nome = nomealuno
        self.peso = pesoaluno #esses 3 são atributos #atributos usam sempre self, atributos atribuem valores
        self.idade = idadealuno
    def comer(self, comida, bebida):
        print(f'{self.nome} foi comer {comida} e beber {bebida}')
    def dormir(self, dormir):
        print(f'{self.nome} esta dormindo ')
    def falar(self, falar):
        print(f'{self.nome} esta falando ')
