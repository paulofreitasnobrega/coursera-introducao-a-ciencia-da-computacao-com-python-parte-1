#Week 2 - Exercícios Adicionais (Opcionais)
#Exercício 3

# Faça um programa em Python que recebe um número inteiro e imprime seu dígito das dezenas.
# Digite um número inteiro: 78615
# A saída: O dígito das dezenas é 1

#Aluno: Paulo Freitas Nobrega

numero = int(input("Digite um número inteiro: "))
digito = (numero // 10) % 10

print("O dígito das dezenas é {}".format(digito))