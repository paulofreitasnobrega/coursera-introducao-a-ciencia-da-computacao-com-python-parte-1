# Week 4 - Lista de Exercícios 3
# Exercício 2

# Receba um número inteiro positivo na entrada e imprima os n primeiros números
# ímpares naturais.

#Aluno: Paulo Freitas Nobrega

incremento = 1
primeirosNumeros = []

quantidadeDeNumeros = int(input("Forneça um número inteiro positivo: "))

while len(primeirosNumeros) < quantidadeDeNumeros:
    if incremento % 2 > 0:
        primeirosNumeros.append(incremento)
        print(incremento)
    incremento += 1
