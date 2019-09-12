# Week 7 - Exercícios em Vídeo
# Exercício 3 - Decomposição em Fatores Primos

# Desenvolver um programa que dado número inteiro n, sendo que n é maior que 1,
# imprimir a sua decomposição fatores primos indicando também a multiplicidade
# de cada fator

#Aluno: Paulo Freitas Nobrega

# Calcula a multiplicidade de um número.
# A cada divisão inteira encontrada, entre número e fator, incrementa a
# multiplicidade. A primeira divisão a possuir resto, encerra a operação de laço
# e retorna a quantidade de total de multiplicidade
def Multiplicidade(numero, fator):
	multiplicidade = 0

	while numero % fator == 0:
		multiplicidade += 1
		numero = numero / fator

	# O número na tupla retornada, representa o resto não divisível pelo fator
	return (numero, multiplicidade)

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

# Função de entrada do programa
def Main():
	fator = 2
	numero = int(input("Digite um número inteiro, maior do que 1: "))

	while numero > 1:
		# numero é atribuido com o resto da operação de decomposição realizada na
		# função de multiplicidade
		numero, multiplicidade = Multiplicidade(numero, fator)

		if multiplicidade > 0 and EsteNumeroEPrimo(fator):
			print("Fator Primo: {}, Multiplicidade: {}".format(fator, multiplicidade))

		fator += 1

Main()
