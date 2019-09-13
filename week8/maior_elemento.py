# Week 8 - Exercícios Adicionais (Opcionais)
# Exercício 1 - Maior elemento de uma lista

# Escreva a função maior_elemento que recebe como parâmetro uma lista com
# números inteiros e devolve um número inteiro correspondente ao maior valor
# presente na lista recebida.

#Aluno: Paulo Freitas Nobrega

# Você consegue resolver essa questão utilizando max(list). Para fim
# didático e fixação do conteúdo vou utilizar estruturas de repetição
# e condicionais

# recebe uma lista e retorna o maior número
def maior_elemento(numeros):
    maiorNumero = 0

    for numeroCorrente in numeros:
        if numeroCorrente > maiorNumero or maiorNumero == 0:
            maiorNumero = numeroCorrente

    return maiorNumero

print(maior_elemento([-90, -27, -12]))
