# Week 4 - Exercícios Complementar
# Exercício - Repetição com while
# Sugerido pelo Prof. Fabio Kon em aula

# Faça um programa em Python que pergunte ao usuário uma quantidade de números
# a ser somado. Após, permita ao mesmo digitar os números até que o limite
# seja alcançado. Ao final, exiba o total da soma.

# Aluno: Paulo Freitas Nobrega

total = 0
numeros = 0
incremento = 0

# Soma a variável total através do valor recebido
# Você pode subtrair adicionando um valor negativo (-) a soma
# Ex: V1:10, V2:10, V3:-10 = 20
def Somar(valor):
    global total
    total += valor

# Retorna o valor númerico fornecido pelo usuário
def PegarEntrada(label):
    return float(input("Forneça o valor do nº{}: ".format(label)))

numeros = int(input("Informe quantos números você deseja somar: "))

while incremento < numeros:
    incremento += 1
    valor = PegarEntrada(incremento)
    Somar(valor)

print("Soma Total: {}".format(total))
