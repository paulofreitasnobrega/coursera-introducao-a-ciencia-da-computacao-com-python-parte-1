# Week 5 - Lista de Exercícios 4
# Exercício 2 - Primos

# Escreva a função maior_primo que recebe um número inteiro maior ou igual a 2
# como parâmetro e devolve o maior número primo menor ou igual ao número
# passado à função

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

# Retorna o maior número primo abaixo ou igual ao número fornecido
def maior_primo(numero):
    if numero < 2:
        return 0

    for numeroCorrente in range(numero, 2, -1):
        if EsteNumeroEPrimo(numeroCorrente):
            return numeroCorrente

# Teste números maiores ou igual a 2
def test_NumerosMaioresQueUm():
    assert maior_primo(100) == 97

# Teste números menores que 2. Por padrão retorna 0
def test_NumerosMenoresQueDois():
    assert maior_primo(1) == 0
