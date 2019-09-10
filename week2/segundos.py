#Week 2 - Exercícios Adicionais (Opcionais)
#Exercício 2

#Reescreva o programa contaSegundos para imprimir também a quantidade de 
# dias, ou seja, faça um programa em Python que, dada a quantidade de segundos, 
# "quebre" esse valor em dias, horas, minutos e segundos. 

# A saída deve estar no formato: a dias, b horas, c minutos e d segundos.

#Aluno: Paulo Freitas Nobrega

conversao = (86400, 3600, 60) #segundos por: dia, hora, minuto

entradaUsuario = int(input("Por favor, entre com o número de segundos que deseja converter: "))

horasRestantes = (entradaUsuario % conversao[0])
minutosRestantes = (horasRestantes % conversao[1])

dias = entradaUsuario // conversao[0]
horas = horasRestantes // conversao[1]
minutos = minutosRestantes // conversao[2]
segundos = minutosRestantes % conversao[2]

print("{} dias, {} horas, {} minutos e {} segundos.".format(dias, horas, minutos, segundos))