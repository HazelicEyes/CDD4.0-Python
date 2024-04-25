inicio = int(input("Digite o horario de inicio: "))
final = int(input("Digite o horario de fim: "))

if inicio < final:
    duracao = final - inicio
else:
    duracao = 24 - inicio + final

print(f"A partida durou {duracao} horas")