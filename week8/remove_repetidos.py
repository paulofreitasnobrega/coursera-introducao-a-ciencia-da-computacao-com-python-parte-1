# Week 8 - Lista de Exercícios 6
# Exercício 1 - Removendo elementos repetidos

# Escreva a função remove_repetidos que recebe como parâmetro uma lista com
# números inteiros, verifica se tal lista possui elementos repetidos e os
# remove. A função deve devolver uma lista correspondente à primeira lista,
# sem elementos repetidos. A lista devolvida deve estar ordenada.

#Aluno: Paulo Freitas Nobrega

# Retorna uma nova lista, ordenada, contendo apenas números únicos
# da lista original
def remove_repetidos(lista):
	listaDeNumerosUnicos = []

	for numero in lista:
		if numero not in listaDeNumerosUnicos:
			listaDeNumerosUnicos.append(numero)

	return sorted(listaDeNumerosUnicos)
