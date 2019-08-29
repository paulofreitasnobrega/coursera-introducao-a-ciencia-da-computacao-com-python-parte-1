# Week 3 - Lista de Exercícios 2
# Exercício 5

# Receba 3 números inteiros na entrada e imprima (crescente) se eles forem dados 
# em ordem crescente. Caso contrário, imprima (não está em  ordem crescente)

#Aluno: Paulo Freitas Nobrega

# Retorna o valor númerico fornecido pelo usuário
def PegarEntrada(label):
    return int(input("{} Informe um número inteiro: ".format(label)))

numeros = PegarEntrada("A"), PegarEntrada("B"), PegarEntrada("C")
numerosOrdenados = tuple(sorted(numeros))

print("crescente" if numeros == numerosOrdenados else "não está em ordem crescente")