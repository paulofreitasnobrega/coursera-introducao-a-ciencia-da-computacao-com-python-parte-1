# Week 8 - Lista de Exercícios 6
# Exercício 2 - Soma dos elementos de uma lista

# Escreva a função soma_elementos que recebe como parâmetro uma lista com
# números inteiros e devolve um número inteiro correspondente à soma dos
# elementos da lista recebida.

#Aluno: Paulo Freitas Nobrega

# Você consegue resolver essa questão utilizando sum(list). Para fim didático
# e fixação vou utilizar estruturas de repetição e condicionais

# Recebe um lista de números e retorna a soma destes
def soma_elementos(numeros):
	soma = 0

	for numeroCorrente in numeros:
		soma += numeroCorrente

	return soma
