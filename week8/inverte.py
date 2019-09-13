# Week 8 - Exercícios Adicionais (Opcionais)
# Exercício 2 - Invertendo sequência

# Como pedido na primeira video-aula desta semana, escreva um programa que
# recebe uma sequência de números inteiros e imprima todos os valores
# em ordem inversa. A sequência sempre termina pelo número 0. Note que 0 (ZERO)
# não deve fazer parte da sequência.

#Aluno: Paulo Freitas Nobrega

# Retorna o valor númerico fornecido pelo usuário
def PegarEntrada():
  return int(input("Digite um número: "))

# Recebe uma lista e retorna uma nova lista com seus elementos em ordem inversda
def ListaEmOrdemInversa(lista):
	listaInversa = []

	# Percorra todo o comprimento de uma lista em ordem decrescente
	for numero in range(len(lista), 0, -1):
		# atribua, à nova lista, o número contido em list[n - 1]
		listaInversa.append(lista[numero - 1])

	return listaInversa

# Função de entrada do programa
def Main():
	lista = []
	numero = 1

	# leia os números fornecidos pelo usuário até que o número lido seja 0
	while numero != 0:
		numero = PegarEntrada()

		# se o número lido for diferente de 0, armazene em list
		if numero != 0:
			lista.append(numero)

	# cria uma lista reversa
	listaInversa = ListaEmOrdemInversa(lista)

	# percorre a lista exibindo os números
	for numero in listaInversa:
		print(numero)

Main()
