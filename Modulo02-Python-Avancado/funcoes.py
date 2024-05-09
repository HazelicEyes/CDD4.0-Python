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
def contar_vogais(texto):
    contador = 0
    vogais = 'aeiouAEIOU'
    for x in texto:
        if x in "aeiouAEIOU":
            contador += 1
    print(contador)
def estoque(produto, quantidade, valor):
    total = valor*quantidade
    return total

def numero(n):
    if n > 0:
        return "Positivo"
    elif n < 0 :
        return 'Negativo'
    else:
        return 'Zero'