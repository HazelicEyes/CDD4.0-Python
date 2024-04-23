anterior = 0
for x in range(3):
    numero = int(input(f'Digite o {x+1}º numero: '))
    if numero > anterior:
        anterior = numero
print(anterior)