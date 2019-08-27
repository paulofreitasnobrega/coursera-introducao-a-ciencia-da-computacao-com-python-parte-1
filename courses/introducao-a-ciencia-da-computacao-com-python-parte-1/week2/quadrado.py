#Week 2 - Lista de Exercícios 1
#Exercício 1

#Faça um programa em Python que receba o valor correspondente ao lado de um
#quadrado, calcule e imprima seu perímetro e sua área.
#Observação: a saída deve estar no formato: "perímetro: x - área: y"

#Aluno: Paulo Freitas Nobrega

ladoQuadrado = float(input("Informe o valor correspondente ao lado de um quadrado: "))
areaQuadrado = ladoQuadrado * ladoQuadrado
perimetroQuadrado = ladoQuadrado * 4

print("perímetro: {} - área: {}".format(perimetroQuadrado, areaQuadrado))
