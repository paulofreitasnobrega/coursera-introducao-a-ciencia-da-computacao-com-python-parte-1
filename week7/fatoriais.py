# Week 7 - Exercícios em Vídeo
# Exercício 1 - Repetições Encaixadas - Fatorial

# Escreva um programa que leia uma sequência de números digitados pelo usuário,
# e para cada número digitado, informar o seu fatorial.
# A solução deve utilizar Repetições Encaixadas

#Aluno: Paulo Freitas Nobrega

numeroEscolhido = 1

while numeroEscolhido > 0:
    fatorial = 1
    numeroEscolhido = int(input("Forneça um número inteiro: "))
    numeroCorrente = numeroEscolhido

    while numeroCorrente > 0:
        fatorial *= numeroCorrente
        numeroCorrente = numeroCorrente - 1

    print("Fatorial de {} é {}".format(numeroEscolhido, fatorial))
