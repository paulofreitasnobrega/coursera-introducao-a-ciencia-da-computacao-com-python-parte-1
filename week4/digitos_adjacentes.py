# Week 4 - Exercícios Adicionais (Opcionais)
# Exercício 2 - Desafio do vídeo "Repetição com while"
# Desafio sugerido pelo Prof. Fabio Kon em aula

# Escreva um programa que receba um número inteiro na entrada e verifique se o
# número recebido possui ao menos um dígito com um dígito adjacente igual a ele.
# Caso exista, imprima "sim"; se não existir, imprima "não".
# Ex: 1223456 = Onde 1(22)3456

# Aluno: Paulo Freitas Nobrega

numeroAnterior = 0
numerosAdjacentesIguais = False

# Retorna uma tupla contendo o dígitos iniciais do número atribuído, bem como
# seu último dígito.
# Ex: 1234 - (123, 4)
def SeperarNumeros(numero):
    digitosIniciais = numero // 10
    digitoFinal = numero % 10
    return digitosIniciais, digitoFinal

numeroUsuario = int(input("Forneça um número inteiro: "))
separacao = SeperarNumeros(numeroUsuario)

while separacao[0] > 0 and not numerosAdjacentesIguais:
    numeroAnterior = separacao[1]
    separacao = SeperarNumeros(separacao[0])
    if separacao[1] == numeroAnterior:
        numerosAdjacentesIguais = True

if numerosAdjacentesIguais:
    print("sim");
else:
    print("não");
