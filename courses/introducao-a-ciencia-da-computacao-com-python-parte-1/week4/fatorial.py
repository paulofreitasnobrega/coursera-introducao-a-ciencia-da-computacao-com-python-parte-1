# Week 4 - Lista de Exercícios 3
# Exercício 1

# Escreva um programa que receba um número natural nn na entrada e imprima
# n! (fatorial) na saída.

#Aluno: Paulo Freitas Nobrega

# Calcula o fatorial de um número natural
def Fatorial(numero):
    fatorial = 1
    for numeroCorrente in range(numero, 0, -1):
        fatorial *= numeroCorrente

    return fatorial

numero = int(input("Forneça um número natural: "))
print(Fatorial(numero))
