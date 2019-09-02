# Week 4 - Exercícios Adicionais (Opcionais)
# Exercício 1

# Escreva um programa que receba um número inteiro positivo na entrada e
# verifique se é primo. Se o número for primo, imprima "primo". Caso contrário,
# imprima "não primo".

# Aluno: Paulo Freitas Nobrega

# Verifica se um número é primo.
# OBS: Um número primo possui apenas dois divisores: 1 e ele mesmo. Esta função
# cria um laço de repetição baseada no número recebido. A cada ciclo do loop
# uma divisão sem resto é realizada. Em caso de sucesso, a variável
# numeroDeDivisores é incrementada. Quando esta variável se torna maior que 2,
# detectamos que o número não é primo
def EsteNumeroEPrimo(numero):
    numeroDeDivisores = 0

    for divisor in range(1, numero + 1):
        if numero % divisor == 0:
            numeroDeDivisores += 1

            if numeroDeDivisores > 2:
                return False

    return True

numero = int(input("Forneça um número inteiro positivo: "))
print("primo" if EsteNumeroEPrimo(numero) else "não primo")
