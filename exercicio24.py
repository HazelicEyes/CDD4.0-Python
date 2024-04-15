senha1 = "1234"
senha2 = input("Digite a senha: ")
contador = 1

if senha2 == senha1:
    print("Senha correta, acesso liberado")
while senha2 != senha1:
    input("Senha incorreta, digite novamente: ")
    contador += 1
    if contador == 3:
        print("Errou a senha 3 vezes, acesso bloqueado")
        break