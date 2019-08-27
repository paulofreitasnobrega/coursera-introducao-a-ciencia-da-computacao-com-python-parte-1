#Week 2 - Lista de Exercícios 1
#Exercício 2

#Faça um programa em Python que receba quatro notas, calcule e imprima 
# a média aritmética. 
#Saída de Dados: A média aritmética é x

#Aluno: Paulo Freitas Nobrega
#Observação: Nesta variação vou utilizar lista e laços para aprimorar
#o script, bem como a biblioteca python Numpy
import numpy as np

notas = []
qtdNotas = int(input("Quantas notas baseará seu Cálculo? Informe: "))

for x in range(qtdNotas):
    nota = float(input("Forneça a nota {}: ".format(x + 1)))
    notas.append(nota)

print("A média aritmética é {}".format(np.median(notas)))