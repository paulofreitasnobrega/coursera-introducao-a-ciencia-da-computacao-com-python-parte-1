# Week 6 - Tarefa de programação: Programa completo - Jogo do NIM

# Você deverá escrever um programa na linguagem Python, versão 3, que permita
# a uma "vítima" jogar o NIM contra o computador. O computador, é claro,
# deverá seguir a estratégia vencedora explicada com detalhes na resenha
# do exercício.

# Permite ao jogador denifir o modo de jogo.
def ModoDeJogo():
    # define uma lista dos modos de jogo permitidos
    modoDeJogoSelecionado = 0
    modosDeJogo = ["Partida Isolada", "Campeonato"]

    # exibe o nome dos modos permitidos para seleção
    print("Bem-vindo ao jogo do NIM! Selecione um modo de jogo:\n")
    for chave, modo in enumerate(modosDeJogo):
        print("{} - {}".format(chave + 1, modo))

    # solicita ao usuário que escolha o modo de jogo desejado
    while modoDeJogoSelecionado > len(modosDeJogo) or modoDeJogoSelecionado < 1:
        modoDeJogoSelecionado = int(input("Qual modo você deseja jogar? "))

    # informa o modo de jogo selecionado
    print("Você selecionou o modo: {}\n".format(modosDeJogo[modoDeJogoSelecionado - 1]))

    return modoDeJogoSelecionado

# Define a jogada do computador.
def computador_escolhe_jogada(n, m):
    # nomeclatura com melhor compreensão para os atributos obrigatórios
    pecasRestantesNoJogo = n
    limitePecasRemovidas = m
    escolhaDoComputador = 0

    # define a estratégia do computador: remover todas as peças restantes
    # ou remover a quantidade máxima de pecas permitidas e multiplas de (m + 1)
    if pecasRestantesNoJogo <= limitePecasRemovidas:
        escolhaDoComputador = pecasRestantesNoJogo
    else:
        for i in range(1, (limitePecasRemovidas + 1)):
            if (pecasRestantesNoJogo - i) % (limitePecasRemovidas + 1) == 0:
                escolhaDoComputador = i

    # quando não for possível a vitória do computador. Retornar o valor limite
    # de peças a serem removidas por turno
    if escolhaDoComputador == 0:
        escolhaDoComputador = limitePecasRemovidas

    return escolhaDoComputador

# Permite ao Jogador fazer uma jogada.
def usuario_escolhe_jogada(n, m):
    # nomeclatura com melhor compreensão para os atributos obrigatórios
    pecasRestantesNoJogo = n
    limitePecasRemovidas = m
    escolhaDoJogador = 0

    # define o limite permitido na jogada
    if pecasRestantesNoJogo >= limitePecasRemovidas:
        limitePecasRemovidasNaJogada = limitePecasRemovidas
    else:
        limitePecasRemovidasNaJogada = pecasRestantesNoJogo

    # solicita ao usuário o número de peças a serem retiradas no turno
    while escolhaDoJogador > limitePecasRemovidasNaJogada or escolhaDoJogador < 1:
        escolhaDoJogador = int(input("Quantas peças você vai tirar? "))

    return escolhaDoJogador

# Gerencia o fluxo de cada partida.
def partida():
    computadorVenceu = True
    turnoDoComputador = False
    limitePecasPorJogada = 0

    # solicita ao usuário o número total de peças no tabuleiro
    totalDePecas = int(input("Quantas peças? "))

    # solicita ao usuário o número de peças limites a serem retiradas por turno
    while limitePecasPorJogada < 1:
        limitePecasPorJogada = int(input("Limite de peças por jogada? "))

    # determina o responsável pelo primeiro turno da rodada
    if totalDePecas % (limitePecasPorJogada + 1) == 0:
        print("Você começa!\n")
        turnoDoComputador = False
    else:
        print("Computador começa!\n")
        turnoDoComputador = True

    # inicia os turnos
    while totalDePecas > 0:
        # invoca a função específica de jogador/computador.
        # recebe a quantidade de peças a serem retiradas do tabuleiro
        # e exibe mensagem da quantidade de peças retiradas do tabuleiro
        if turnoDoComputador:
            pecasRetiradas = computador_escolhe_jogada(totalDePecas, limitePecasPorJogada)
            print("O computador tirou {} peca(s).".format(pecasRetiradas))
        else:
            pecasRetiradas = usuario_escolhe_jogada(totalDePecas, limitePecasPorJogada)
            print("Você tirou {} peca(s).".format(pecasRetiradas))

        # calcula o valor de peças restantes
        totalDePecas = totalDePecas - pecasRetiradas

        # exibe mensagem da quantidade de peças restantes no tabuleiro
        if totalDePecas > 1:
            print("Agora restam {} peças no tabuleiro.\n".format(totalDePecas))
        elif totalDePecas == 1:
            print("Agora resta apenas uma peça no tabuleiro.")

        # atribui o proximo a jogar
        turnoDoComputador = not turnoDoComputador

    # exibe a mensagem do vencedor
    if not turnoDoComputador:
        print("O computador ganhou!")
    else:
        computadorVenceu = False
        print("Você ganhou!")

    return(computadorVenceu)

# Gerencia o fluxo do campeonato.
def campeonato():
    numeroDaRodada = 1
    pontosDoComputador = 0
    pontosDoUsuario = 0

    # loop de rodadas
    while numeroDaRodada < 4:
        print("**** Rodada {} ****\n".format(numeroDaRodada))

        # inicia a partida e atualiza os valores do placar geral
        if partida():
            pontosDoComputador += 1
        else:
            pontosDoUsuario += 1

        # incrementa o número da rodada
        numeroDaRodada += 1

    # exibe o placa final
    print("Placar: Você {} X {} Computador".format(pontosDoUsuario, pontosDoComputador))

# Função de entrada do programa.
def main():
    # solicita ao usuário escolher um modo de jogo (Partida Isolada ou Campeonato)
    modoDeJogo = ModoDeJogo()

    # invoca o modo de jogo escolhido
    partida() if modoDeJogo == 1 else campeonato()

# chama a função de entrada
main()
