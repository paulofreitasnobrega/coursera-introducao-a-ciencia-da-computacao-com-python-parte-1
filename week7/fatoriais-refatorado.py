# Week 7 - Exercícios em Vídeo
# Exercício 2 - Repetições Encaixadas - Fatorial Refatoração

# Refatorar o programa que lê uma sequência de números digitados pelo usuário,
# e para cada número digitado, informar o seu fatorial. Nessa refatoração o
# while mais profundo deve-se tornar uma função chamada fatorial

#Aluno: Paulo Freitas Nobrega

# Calcula o fatorial de um número utilizando while
def Fatorial(numero):
    fatorial = 1

    while numero > 0:
        fatorial *= numero
        numero = numero - 1

    return fatorial

# Função de entrada do programa
# 0 finaliza a execução
def main():
    numero = 1

    while numero > 0:
        numero = int(input("Forneça um número inteiro: "))
        fatorial = Fatorial(numero)
        print("Fatorial de {} é {}".format(numero, fatorial))

main()
