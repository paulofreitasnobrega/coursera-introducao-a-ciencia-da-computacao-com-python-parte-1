# Week 3 - Lista de Exercícios 2
# Exercício 4

# Receba um número inteiro na entrada e imprima (FizzBuzz) na saída se o número for divisível 
# por 3 e por 5. Caso contrário, imprima o mesmo número que foi dado na entrada.

#Aluno: Paulo Freitas Nobrega

numero = int(input("Informe um número inteiro: "))

print("FizzBuzz" if (numero % 3 == 0 and numero % 5 == 0) else numero)
