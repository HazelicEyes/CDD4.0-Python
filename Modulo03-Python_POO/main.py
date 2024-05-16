from classes import *

p1 = Pessoa("Joao",65,23)
p2 = Pessoa("Maria",55,20)

print(f'O nome da pessoa 1 é {p1.nome} e ela pesa {p1.peso}')
p1.nome = "Henrique"
p1.comer("Coxinha", "Coca")
p1.falar("Alguma coisa")

