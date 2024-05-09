def imprime_nome(nome):
    print(f'Nome: {nome}')

def piramide(num):
    for x in range(1,num+1):
        for y in range(1,x+1):
            print(x, end=" ")
        print()

def piramide2(num):
    for x in range(1,num+1):
        for y in range(1,x+1):
            print(y, end=" ")
        print()
