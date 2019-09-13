# Week 8 - Lista de Exercícios 6
# Exercício 1 - Removendo elementos repetidos

# Escreva a função remove_repetidos que recebe como parâmetro uma lista com
# números inteiros, verifica se tal lista possui elementos repetidos e os
# remove. A função deve devolver uma lista correspondente à primeira lista,
# sem elementos repetidos. A lista devolvida deve estar ordenada.

#Aluno: Paulo Freitas Nobrega

# Você consegue resolver essa questão utilizando sorted(set(list)). Para fim
# didático e fixação do conteúdo vou utilizar estruturas de repetição
# e condicionais

# Retorna uma nova lista, ordenada, contendo apenas números únicos
# da lista original
def remove_repetidos(lista):
	listaOrdenada = []
	listaDeNumerosUnicos = []

	# gera uma lista de números únicos
	for numeroCorrente in lista:
		# se a listaDeNumerosUnicos não possuir o número corrente, adiciona-o
		if numeroCorrente not in listaDeNumerosUnicos:
			listaDeNumerosUnicos.append(numeroCorrente)

	# ordenando os números únicos
	while len(listaDeNumerosUnicos) > 0:
		# reconhe o menor número e adiciona-o na lista ordenada
		numeroMinimo = min(listaDeNumerosUnicos)
		listaOrdenada.append(numeroMinimo)

		# remove o número adicionado
		index = listaDeNumerosUnicos.index(numeroMinimo)
		del listaDeNumerosUnicos[index]

	return listaOrdenada
