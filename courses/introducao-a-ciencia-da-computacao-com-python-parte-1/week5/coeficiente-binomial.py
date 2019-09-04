# Week 5 - Exercícios Complementar
# Exercício - Coeficiente Binomial
# Sugerido pelo Prof. Fabio Kon em aula

# Faça um programa em Python que utilize funções para calcular o fatorial
# de determinados números e após, utilize essa função para calcular o
# Coeficiente binomial.
# Fórmula: https://pt.wikipedia.org/wiki/Coeficiente_binomial

# Aluno: Paulo Freitas Nobrega

# Retorna o valor númerico fornecido pelo usuário
def PegarEntrada(label):
    return int(input("Forneça o valor de {}: ".format(label)))

# Calcula o fatorial de um número
def Fatorial(n):
    fatorial = 1
    for numeroCorrente in range(n, 0, -1):
        fatorial *= numeroCorrente

    return fatorial

# Calcula o coeficiente binomial de um número
def CoeficienteBinomial(n, k):
    return Fatorial(n) / (Fatorial(k) * Fatorial(n - k))

n = PegarEntrada("n")
k = PegarEntrada("k")
print(CoeficienteBinomial(n, k))

print(sum(len('abc')+len('a')))

# Guia de Testes
# (5,3) = 10
# (4,1) = 4
# (6,6) = 1
