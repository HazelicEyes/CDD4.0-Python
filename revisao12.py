anos = int(input("Quantos anos voce viveu? "))
meses = int(input("Quantos meses voce viveu? "))
dias = int(input("Quantos dias voce viveu? "))
ano=365
mes=30
"""ou simplesmente idade = anos*365 + meses*30 + dias"""
anosParaDias = anos * ano
mesesParaDias = meses * mes
idade = anosParaDias + mesesParaDias + dias
print(f'Voce viveu por {idade} dias.')