# Week 4 - Desafio
# Exercício - Soma dos Dígitos
# Sugerido pelo Prof. Fabio Kon em aula

# Faça um programa em Python que receba um número inteiro do usuário e após
# some cada um dos dígitos deste mesmo número.
# Ex: 1234 = 10. Onde (1 + 2 + 3 + 4)

# Aluno: Paulo Freitas Nobrega

soma = 0

# Retorna uma tupla contendo o dígitos iniciais do número atribuído, bem como
# seu último dígito.
# Ex: 1234 - (123, 4)
def SeperarNumeros(numero):
    digitosIniciais = numero // 10
    digitoFinal = numero % 10
    return digitosIniciais, digitoFinal

numeroUsuario = int(input("Digite um número: "))
separacao = SeperarNumeros(numeroUsuario)

# IMPORTANETE: sum() diferente de max() ou min() permite apenas dois atributos
# como entrada de dados. Dessa forma, tuplas com mais de 2 elementos, geram o
# erro: TypeError: divmod expected 2 arguments, got 1   >>> Fique atento!

# Um inteiro 0 equivale a false em Python. Assim sum(0, 0) é a condição de
# encerramento do while. Ou seja, enquanto a tupla separacao possuir valores
# o while continuará a execução.
while sum(separacao):
    soma += separacao[1]
    separacao = SeperarNumeros(separacao[0])

print("Soma Total: {}".format(soma))

# Uma alternativa com um código menor seria aceitar uma entrada em string
# converte-la em list (Ex: list("1234") = ['1','2','3','4']) e passá-la para
# um map reponsável pela conversao do caracter em inteiro e soma. Exemplo:
# a = "1234"
# map(minhafuncao, list(a))
# Você também poderá utilizar lambda para diminuir ainda mais o código.
