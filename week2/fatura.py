#Week 2 - Exercícios Adicionais (Opcionais)
#Exercício 1

#Escreva um programa que receba o nome do cliente, o dia de vencimento, 
# o mês de vencimento e o valor da fatura e imprima (saída de dados) 
# a mensagem com os dados recebidos, no mesmo formato da mensagem abaixo.

#Olá, Fulano de Tal
#A sua fatura com vencimento em 9 de Janeiro no valor de R$ 350,00 está fechada.

#Aluno: Paulo Freitas Nobrega

fatura = {}

fatura["nomeCliente"] = input("Digite o nome do cliente: ")
fatura["diaVenc"] = input("Digite o dia de vencimento: ")
fatura["mesVenc"] = input("Digite o mês de vencimento: ")
fatura["valor"] = input("Digite o valor da fatura: ")

msg = "Olá, {}\nA sua fatura com vencimento em {} de {} no valor de R$ {} está fechada."

print(msg.format(fatura["nomeCliente"], fatura["diaVenc"], fatura["mesVenc"], fatura["valor"]))