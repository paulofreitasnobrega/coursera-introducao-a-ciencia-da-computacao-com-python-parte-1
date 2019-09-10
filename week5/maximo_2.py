# Week 5 - Lista de Exercícios 4
# Exercício 1 - Máximo

# Escreva a função maximo que recebe 2 números inteiros como parâmetro
# e devolve o maior deles.

#Aluno: Paulo Freitas Nobrega

# Retorna o maior número
def maximo(numero1, numero2):
    return max(numero1, numero2)

# Testa a função maximo com numeros positivos
def test_NumeroPositivo():
    assert maximo(3, 4) == 4

# Testa a função maximo com numeros negativos
def test_NumeroNegativo():
    assert maximo(0, -1) == 0
