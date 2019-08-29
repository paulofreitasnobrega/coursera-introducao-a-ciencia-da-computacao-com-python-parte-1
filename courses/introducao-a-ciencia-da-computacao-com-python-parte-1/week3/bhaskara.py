# Week 3 - Exercícios Adicionais (Opcionais)
# Exercício 2 - Desafio da videoaula 
# Cálculo das Raízes com a Fórmula Bhaskara

# Faça um programa em Python que recebe 3 entradas (a, b e c). E usando
# a fórmula de bhaskara deverá imprimir as raízes. Onde (Delta < 0) não
# haverá raízes reais; (Delta == 0) possui uma raiz real; (Delta > 0)
# possui duas raizes reais.

# Aluno: Paulo Freitas Nobrega

import math

# Retorna o valor númerico fornecido pelo usuário
def PegarEntrada(label):
    return int(input("Entrada {}: ".format(label)))

# Calcula o Delta através dos valores númericos a, b, c e por meio deste
# retorna uma resposta com a quantidade de raízes reais
def Bhaskara(a, b, c):
    delta = (b**2) - (4*a*c)

    if delta >= 0:
        raizes = (-b + math.sqrt(delta)) / (2*a), (-b - math.sqrt(delta)) / (2*a)
        raizesEmOrdem = tuple(sorted(raizes))

        if delta > 0:
            return "as raízes da equação são {} e {}".format(raizesEmOrdem[0], raizesEmOrdem[1])
        else:
            return "a raiz desta equação é {}".format(raizes[0])
    else:
        return "esta equação não possui raízes reais"


entradas = PegarEntrada("A"), PegarEntrada("B"), PegarEntrada("C")
print(Bhaskara(entradas[0], entradas[1], entradas[2]))

# Guia de Testes
# [Delta < 0]: A=1, B=-4, C=5 - Sem Raiz Real
# [Delta == 0]: A=4, B=-4, C=1 - Raiz Real: 0.5
# [Delta > 0]: A=1, B=-5, C=6 - Raízes Reais: 3.0 e 2.0
