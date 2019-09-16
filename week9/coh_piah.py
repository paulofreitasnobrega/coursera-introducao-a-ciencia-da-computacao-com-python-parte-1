# Week 9 - Projeto Final
# Programa completo - Similaridades entre textos - Caso COH-PIAH

# Seu programa deverá receber diversos textos e calcular os valores dos
# diferentes traços linguísticos, afim de realizar uma comparação e verficar,
# de acordo com a assinatura definida como padrão, qual texto esta "infectado"

# Mais detalhes na resenha do exercício

#Aluno: Paulo Freitas Nobrega

import re
import math

# Retorna a quantidade de caracteres de um conjunto de palavras,
# frases ou sentença
def quantidadeTotalDeCaracteres(conjuntos):
    quantidadeCaracteres = 0

    for conjunto in conjuntos:
        quantidadeCaracteres += len(conjunto)

    return quantidadeCaracteres

# Retorna o tamanho médio das palavras em uma lista de palavras
def TamanhoMedioDasPalavras(palavras):

    return (quantidadeTotalDeCaracteres(palavras) / len(palavras))

# A funcao le os valores dos tracos linguisticos do modelo e devolve uma
# assinatura a ser comparada com os textos fornecidos
# padrão: [4.79, 0.72, 0.56, 80.5, 2.5, 31.6]
def le_assinatura():
    print("Bem-vindo ao detector automático de COH-PIAH.")

    wal = float(input("Entre o tamanho medio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

# A funcao recebe um texto e devolve uma lista das sentencas dentro do texto
def separa_sentencas(texto):
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

# A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca
def separa_frases(sentenca):
    return re.split(r'[,:;]+', sentenca)

# A funcao recebe uma frase e devolve uma lista das palavras dentro da frase
def separa_palavras(frase):
    return frase.split()

# Essa funcao recebe uma lista de palavras e devolve o numero de palavras
# que aparecem uma unica vez
def n_palavras_unicas(lista_palavras):
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

# Essa funcao recebe uma lista de palavras e devolve o numero de palavras
# diferentes utilizadas
def n_palavras_diferentes(lista_palavras):
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

# IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o
# grau de similaridade nas assinaturas.
def compara_assinatura(as_a, as_b):
    somatorio = 0

    for i in range(0, 6):
        somatorio += math.fabs(as_a[i] - as_b[i])

    somatorio = (somatorio / 6)
    return round(somatorio, 2)

# IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.
def calcula_assinatura(texto):
    frases = []
    palavras = []

    # separa as sentencas do texto
    sentencas = separa_sentencas(texto)

    # separa as frases do texto
    for sentenca in sentencas:
        frases += separa_frases(sentenca)

    #separa as palavras do texto
    for frase in frases:
        palavras += separa_palavras(frase)

    # define os traços linguisticos
    wal = TamanhoMedioDasPalavras(palavras)
    ttr = (n_palavras_diferentes(palavras) / len(palavras))
    hlr = (n_palavras_unicas(palavras) / len(palavras))
    sal = (quantidadeTotalDeCaracteres(sentencas) / len(sentencas))
    sac = (len(frases) / len(sentencas))
    pal = (quantidadeTotalDeCaracteres(frases) / len(frases))

    return [wal, ttr, hlr, sal, sac, pal]

# IMPLEMENTAR. Essa funcao recebe uma lista de textos e deve devolver o numero
# (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.
def avalia_textos(textos, ass_cp):
    comparacoes = []

    for texto in textos:
        assinatura = calcula_assinatura(texto)
        comparacao = compara_assinatura(assinatura, ass_cp)
        comparacoes.append(comparacao)

    menorComparacao = min(comparacoes)
    indiceMenorComparacao = (comparacoes.index(menorComparacao) + 1)
    print("O autor do texto {} está infectado com COH-PIAH".format(indiceMenorComparacao))

    return indiceMenorComparacao

# Função de entrada do programa
def main():
    # solicita ao usuário a assinatura padrao
    ass_cp = le_assinatura()
    # solicita ao usuário os textos a serem comparados
    textos = le_textos()
    # realiza a avaliação
    avalia_textos(textos, le_assinatura())

main()
