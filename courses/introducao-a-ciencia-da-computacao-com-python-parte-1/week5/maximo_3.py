# Week 5 - Exercícios Adicionais (Opcionais)
# Exercício 2 - Máximo com 3 parâmetros

# Reescreva a função 'maximo' do outro exercício, que devolve o maior valor
# dentre dois inteiros recebidos, para que ela passe a receber 3 valores
# inteiros como parâmetros e devolva o maior dentre eles.

# Aluno: Paulo Freitas Nobrega

# Recebe três números e retorna o número de maior valor
def maximo(numero1, numero2, numero3):
    maiorNumero = 0
    numeros = (numero1, numero2, numero3)

    for chave, numeroCorrente in enumerate(numeros):
        if numeroCorrente > maiorNumero:
            maiorNumero = numeroCorrente

    return maiorNumero

# Recebe uma lista de números e retorna o número de maior valor
def maximoMelhorada(numeros = []):
    numeros.sort()
    return numeros[(len(numeros) - 1):len(numeros)]

# Realiza o teste na função maximo com numeros positivos
def test_MaiorEntreNumerosPositivos():
    assert 101 == maximo(101, 5, 87)

# Realiza o teste na função maximo com numeros negativos
def test_MaiorEntreNumerosNegativos():
    assert 0 == maximo(-5, -325, 0)

# Realiza o teste na função maximo com numeros positivos e negativos
def test_MaiorEntreNumerosPositivosENegativos():
    assert 42 == maximo(-5, 0, 42)
