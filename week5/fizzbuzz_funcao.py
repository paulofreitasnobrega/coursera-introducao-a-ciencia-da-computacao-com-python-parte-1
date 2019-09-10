# Week 5 - Exercícios Adicionais (Opcionais)
# Exercício 1 - FizzBuzz

# Escreva a função fizzbuzz que recebe como parâmetro um número inteiro e devolve
# 'Fizz' se o número for divisível por 3 e não for divisível por 5;
# 'Buzz' se o número for divisível por 5 e não for divisível por 3;
# 'FizzBuzz' se o número for divisível por 3 e por 5;
# Caso o número não seja divisível 3 e também não seja divisível por 5,
# ela deve devolver o número recebido como parâmetro.

# Aluno: Paulo Freitas Nobrega

# Verifica se a divisao possui resto
def DivisorSemResto(numero, divisor = 3):
    return True if numero % divisor == 0 else False

# Função FizzBuzz
def fizzbuzz(numero):
    if DivisorSemResto(numero) and DivisorSemResto(numero, 5):
        return 'FizzBuzz'
    elif DivisorSemResto(numero) and not DivisorSemResto(numero, 5):
        return 'Fizz'
    elif not DivisorSemResto(numero) and DivisorSemResto(numero, 5):
        return 'Buzz'
    else:
        return numero

# Realiza o teste para verificar se o número é divisível por 3 e 5
def test_DivisivelPorTresECinco():
    assert 'FizzBuzz' == fizzbuzz(15)

# Realiza o teste para verificar se o número é divisível por 3, mas não por 5
def test_DivisivelApenasPorTres():
    assert 'Fizz' == fizzbuzz(3)

# Realiza o teste para verificar se o número é divisível por 5, mas não por 3
def test_DivisivelApenasPorCinco():
    assert 'Buzz' == fizzbuzz(5)

# Realiza o teste para verificar se o número não é divisível por 3 e nem por 5
def test_NaoDivisivelPorTresECinco():
    assert 4 == fizzbuzz(4)
