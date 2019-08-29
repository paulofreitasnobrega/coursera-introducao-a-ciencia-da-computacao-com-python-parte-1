# Week 3 - Exercícios Adicionais (Opcionais)
# Exercício 1 - Distância entre dois pontos

# Receba 4 números na entrada, um de cada vez. Os dois primeiros devem corresponder, 
# respectivamente, às coordenadas x e y de um ponto em um plano cartesiano. 
# Os dois últimos devem corresponder, respectivamente, às coordenadas x e y 
# de um outro ponto no mesmo plano.

# Calcule a distância entre os dois pontos. Se a distância for maior ou igual a 10, 
# imprima (longe) na saída. Caso o contrário, quando a distância for menor que 10, 
# imprima (perto)

# Aluno: Paulo Freitas Nobrega

import math

# Retorna o valor númerico fornecido pelo usuário
def PegarEntrada(planoCartesiano, coordenada):
    return float(input("Forneça a coordenada {} para o Plano Cartesiano {}: ".format(coordenada, planoCartesiano)))

planoCartesianoA = PegarEntrada("A", "X"), PegarEntrada("A", "Y")
planoCartesianoB = PegarEntrada("B", "X"), PegarEntrada("B", "Y")

preCalculo = (planoCartesianoA[0]-planoCartesianoB[0])**2 + (planoCartesianoA[1]-planoCartesianoB[1])**2
distancia = math.sqrt(preCalculo)

print("longe" if distancia >= 10 else "perto")

# Guia de Testes
# [longe]: (1,3), (9,9) - distancia: 10
# [Perto]: (2,4), (5,5) - distancia: 5