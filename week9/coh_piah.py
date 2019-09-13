# Week 9 - Projeto Final
# Programa completo - Similaridades entre textos - Caso COH-PIAH

# Seu programa deverá receber diversos textos e calcular os valores dos
# diferentes traços linguísticos

#Aluno: Paulo Freitas Nobrega

import re

# A funcao le os valores dos tracos linguisticos do modelo e devolve uma
# assinatura a ser comparada com os textos fornecidos
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
    pass

# IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.
def calcula_assinatura(texto):
    pass

# IMPLEMENTAR. Essa funcao recebe uma lista de textos e deve devolver o numero
# (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.
def avalia_textos(textos, ass_cp):
    pass
