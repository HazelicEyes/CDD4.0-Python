pergunta = "S"
while pergunta == "S" or pergunta == 's':
    numero = int(input("Digite um numero:"))
    if numero < 0:
        print(f'O numero {numero} é negativo')
    else:
        print(f'O numero {numero} é positivo')
    pergunta = input("Deseja continuar? S para sim e N para não: ")
else:
    print("Ok, tenha um bom dia")

