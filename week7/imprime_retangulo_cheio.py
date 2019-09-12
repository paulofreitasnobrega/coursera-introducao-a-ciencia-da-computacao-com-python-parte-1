# Week 7 - Lista de Exercícios 5
# Exercício 1

# Escreva um programa que recebe como entradas (utilize a função input) dois
# números inteiros correspondentes à largura e à altura de um retângulo,
# respectivamente. O programa deve imprimir uma cadeia de caracteres que
# represente o retângulo informado com caracteres '#' na saída.

#Aluno: Paulo Freitas Nobrega

# Retorna o valor númerico fornecido pelo usuário
def PegarEntrada():
    return int(input("Forneça o um número inteiro: "))

# Desenha um retangulo de #, baseado na dimensões recebidas
def RetanguloCheio(dimensoes):
    largura, altura = dimensoes
    preencherVertical = 1

    while preencherVertical <= altura:
        preencherHorizontal = 1

        while preencherHorizontal <= largura:
            print("#", end="")
            preencherHorizontal += 1

        print("")
        preencherVertical += 1

# Função de entrada do programa
def Main():
    dimensoes = (PegarEntrada(), PegarEntrada())
    RetanguloCheio(dimensoes)

Main()
