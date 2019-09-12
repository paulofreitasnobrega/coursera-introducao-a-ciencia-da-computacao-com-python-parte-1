# Week 7 - Exercícios Adicionais (Opcionais)
# Exercício 2 - (Difícil) Soma das hipotenusas

# Escreva uma função soma_hipotenusas que receba como parâmetro um número
# inteiro positivo nn e devolva a soma de todos os inteiros entre 1 e nn que são
# comprimento da hipotenusa de algum triângulo retângulo com catetos inteiros.

# Dicas adicionais na resenha do exercício

#Aluno: Paulo Freitas Nobrega

import math

# Faz uma varredura de 1 a n (hipotenusa) buscando por catetos inteiros. Ao
# encontrar a primeira ocorrencia, retorna True. Se não houverem catetos inteiros
# retorna False
def CatetosInteiros(hipotenusa):
    incremento = 1

    while incremento < hipotenusa:
        # formula de Pitágoras h² = a² + b². Uma vez de posse da hipotenusa,
        # varia-se a operação para encontrar o cateto faltante.
        # Ex: b² = h² - a²
        cateto = (hipotenusa ** 2) - (incremento ** 2)

        # garante apenas números positivos evitando problemas de raízes
        # quadradas negativas
        if cateto > 0:
            cateto = math.sqrt(cateto)

            # se o resto de uma divisão por 1 for 0, então trata-se de um
            # número inteiro
            if cateto % 1 == 0:
                return True

        incremento += 1

    return False

# Realiza a soma de todos os inteiros entre 1 e n que são o comprimento da
# hipotenusa de algum triângulo retângulo com catetos inteiros
def soma_hipotenusas(numero):
    hipotenusas = []
    hipotenusa = 1

    while hipotenusa <= numero:
        # se o triângulo possí catetos inteiros, adiciona-se o comprimento da
        # hipotenusa a lista
        if CatetosInteiros(hipotenusa):
            hipotenusas.append(hipotenusa)

        hipotenusa += 1

    # soma-se todos os comprimentos e retorna o total
    return sum(hipotenusas)
