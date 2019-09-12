# Week 7 - Lista de Exercícios 5
# Exercício 2

# Refaça o exercício 1 imprimindo os retângulos sem preenchimento, de forma
# que os caracteres que não estiverem na borda do retângulo sejam espaços.

#Aluno: Paulo Freitas Nobrega

# Retorna o valor númerico fornecido pelo usuário
def PegarEntrada():
    return int(input("Forneça o um número inteiro: "))

# Desenha um retangulo de #, baseado na dimensões recebidas
def RetanguloVazado(dimensoes):
    largura, altura = dimensoes
    preencherVertical = 1

    while preencherVertical <= altura:
        preencherHorizontal = 1

        while preencherHorizontal <= largura:
            # define um ponto cartesiano a ser analisado
            pontoCartesiano = (preencherHorizontal, preencherVertical)

            # desenhe se o ponto estiver na primeira ou última linha
            if pontoCartesiano[1] == 1 or pontoCartesiano[1] == altura:
                print("#", end="")
            # desenhe se o ponto estiver no primeiro ou último caracter da linha
            elif pontoCartesiano[0] == 1 or pontoCartesiano[0] == largura:
                print("#", end="")
            # caso contrário deixe-o em branco
            else:
                print(" ", end="")

            preencherHorizontal += 1

        print("")
        preencherVertical += 1

# Função de entrada do programa
def Main():
    dimensoes = (PegarEntrada(), PegarEntrada())
    RetanguloVazado(dimensoes)

Main()
