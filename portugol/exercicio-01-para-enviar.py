'''
Algoritmo "media-aluno"

Var
// Seção de Declarações das variáveis
media:real
                                      '
Inicio
// Seção de Comandos, procedimento, funções, operadores, etc...
escreva("Digite a media do aluno: ")
leia(media)

se (media >= 7) entao
   escreva("Media:", media, ", Aluno aprovado")
senao
     se (media < 7) e (media >= 5) entao
        escreva("Media:", media, ", Aluno em recuperação")
     senao:
        escreva("Media:", media, ", Aluno reprovado")
        fimse
fimse

Fimalgoritmo
'''