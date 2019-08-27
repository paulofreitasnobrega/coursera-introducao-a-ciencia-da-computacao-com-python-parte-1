#Week 2 - Lista de Exercícios 1
#Exercício 2

#Faça um programa em Python que receba quatro notas, calcule e imprima 
# a média aritmética. 
#Saída de Dados: A média aritmética é x

#Aluno: Paulo Freitas Nobrega

notaUm = float(input("Forneça a nota 1: "))
notaDois = float(input("Forneça a nota 2: "))
notaTres = float(input("Forneça a nota 3: "))
notaQuatro = float(input("Forneça a nota 4: "))

somaNotas = notaUm + notaDois + notaTres + notaQuatro

print("A média aritmética é {}".format(somaNotas / 4))