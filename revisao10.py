soma = 0
for x in range(4):
    nota = float(input(f'Digite o {x+1}º numero: '))
    soma = soma + nota
media = soma / 4
print(f'A media é {media}')
