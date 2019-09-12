# Week 7 - Exercícios Adicionais (Opcionais)
# Exercício 1 - Primos

# Escreva a função n_primos que recebe como argumento um número inteiro
# maior ou igual a 2 como parâmetro e devolve a quantidade de números
# primos que existem entre 2 e n (incluindo 2 e, se for o caso, n).

#Aluno: Paulo Freitas Nobrega

# Verifica se um número é primo.
def EsteNumeroEPrimo(numero):
    numeroDeDivisores = 0

    for divisor in range(1, numero + 1):
        if numero % divisor == 0:
            numeroDeDivisores += 1

            if numeroDeDivisores > 2:
                return False

    return True

# Retorna a quntidade de números primos entre o numeroInicial e o numeroFinal
def ContarNumerosPrimos(numeroInicial, numeroFinal):
    quantidadeDeNumerosPrimos = 0

    for numeroCorrente in range(numeroInicial, numeroFinal + 1):
        if EsteNumeroEPrimo(numeroCorrente):
            quantidadeDeNumerosPrimos += 1

    return quantidadeDeNumerosPrimos

# Função exclusiva para a autocorreção. Retorna a quantidade de números primos
# entre 2 e n
def n_primos(numero):
    return ContarNumerosPrimos(2, numero)
