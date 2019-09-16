# Week 9 - Exercícios em Vídeo
# Exercício - Temperatura mínima e máxima

# Escreva uma função que recebe um lista de temperaturas e informa as variações
# mínima e máxima. Deve-se criar testes.

#Aluno: Paulo Freitas Nobrega

# Exibe as variações de temperatura mínima e máxima de acordo com a lista de
# temperaturas recebida
def minimaMaxima(temperaturas):
    variacoes = (temperaturaMinima(temperaturas), temperaturaMaxima(temperaturas))

    print("Temperatura mínima do mês: ", variacoes[0])
    print("Temperatura máxima do mês: ", variacoes[1])

# Encontra a menor temperatura em uma lista de temperaturas
def temperaturaMinima(temperaturas):
    temperaturaMinima = temperaturas[0]

    for temperatura in temperaturas:
        if temperatura < temperaturaMinima:
            temperaturaMinima = temperatura

    return temperaturaMinima

# Encontra a maior temperatura em uma lista de temperaturas
def temperaturaMaxima(temperaturas):
    temperaturaMaxima = temperaturas[0]

    for temperatura in temperaturas:
        if temperatura > temperaturaMaxima:
            temperaturaMaxima = temperatura

    return temperaturaMaxima

# Realiza a validação entre a temperatura esperada e a temperatura calculada
def teste_pontual(temperaturas, temperaturaEsperada, variacao = "min"):
    if variacao == "min":
        temperaturaCalculada = temperaturaMinima(temperaturas)
    else:
        temperaturaCalculada = temperaturaMaxima(temperaturas)

    if temperaturaCalculada != temperaturaEsperada:
        print("Erro para lista: ", temperaturas)
        print("Temperatura esperada: {} - Temperatura Calculada: {}". format(temperaturaEsperada, temperaturaCalculada))

# Realiza os testes de validação para a temperatura mínima
def teste_temperaturaMinina():
    testes = [
        ([10, -5, 2, 0, 32], -5),
        ([10, 2, 0, 32, 40], 0),
        ([0, 0, 0, 0], 0),
        ([0], 0),
        ([5, 8, 32, 40], 5)
    ]

    print("Iniciando os testes de temperatura mínima")

    for teste in testes:
        teste_pontual(teste[0], teste[1])

    print("Finalizando os testes de temperatura mínima")

# Realiza os testes de validação para a temperatura máxima
def teste_temperaturaMaxima():
    testes = [
        ([10, -5, 2, 0, 32], 32),
        ([10, 2, 0, 32, 40], 40),
        ([0, 0, 0, 0], 0),
        ([0], 0),
        ([5, 8, 32, 40], 40)
    ]

    print("Iniciando os testes de temperatura máxima")

    for teste in testes:
        teste_pontual(teste[0], teste[1], "max")

    print("Finalizando os testes de temperatura máxima")

minimaMaxima([10,-5,2,0,32])
