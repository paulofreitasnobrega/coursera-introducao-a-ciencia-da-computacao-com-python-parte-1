# Week 6 - Tarefa de programação: Programa completo - Jogo do NIM

# Você deverá escrever um programa na linguagem Python, versão 3, que permita
# a uma "vítima" jogar o NIM contra o computador. O computador, é claro,
# deverá seguir a estratégia vencedora explicada com detalhes na resenha
# do exercício.

# Minhas Funções

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

# Seleciona o próximo jogador
def SelecionarProximoJogador(proximoJogador = 0):
    # define uma lista contendo ID, Rótulo e método callback de cada jogador
    competidores = [
        [0, "Jogador", "usuario_escolhe_jogada"],
        [1, "Comutador", "computador_escolhe_jogada"]
    ]

    # reseta o jogador se o número for maior que a quantidade de jogadores - 1
    if proximoJogador > 1:
        proximoJogador = 0;

    return competidores[proximoJogador]

# Funcões obrigatórias pelo sistema automático de correção

# Define a estratégia de jogada do computador.
def computador_escolhe_jogada(n, m):
    # inclui uma nomeclatura com melhor compreensão para os atributos obrigatórios
    pecasRestantesNoJogo = n
    limitePecasRemovidas = m

    # define a estratégia do computador, entre remover todas as peças restantes,
    # remover a quantidade máxima de peças permitidas ou remover uma quantidade
    # estratégica de peças para garantir a vitória
    if pecasRestantesNoJogo <= limitePecasRemovidas:
        return pecasRestantesNoJogo
    elif (pecasRestantesNoJogo - limitePecasRemovidas) >= (limitePecasRemovidas + 1):
        return limitePecasRemovidas
    else:
        for i in range(limitePecasRemovidas, 0, -1):
            if (pecasRestantesNoJogo - i) >= (limitePecasRemovidas + 1):
                return i

# Permite ao Jogador fazer uma jogada.
def usuario_escolhe_jogada(n, m):
    # Eu não compreendi a obrigatoriedade do uso do parametro n.
    limitePecasRemovidas = m
    escolhaDoJogador = 0

    # solicita ao usuário o número de peças a serem retiradas no turno
    while escolhaDoJogador > limitePecasRemovidas or escolhaDoJogador < 1:
        escolhaDoJogador = int(input("Quantas peças você vai tirar? "))

    return escolhaDoJogador

# Gerencia o fluxo de cada partida.
def partida():
    jogadorAtual = []
    ultimoJogador = []
    limitePecasPorJogada = 0

    # solicita ao usuário o número total de peças no tabuleiro
    totalDePecas = int(input("Quantas peças? "))

    # solicita ao usuário o número de peças limites a serem retiradas por turno
    while limitePecasPorJogada < 1 or limitePecasPorJogada > totalDePecas:
        limitePecasPorJogada = int(input("Limite de peças por jogada? "))

    # determina o jogador responsável pelo primeiro turno da rodada
    if totalDePecas % (limitePecasPorJogada + 1) == 0:
        jogadorAtual = SelecionarProximoJogador()
    else:
        jogadorAtual = SelecionarProximoJogador(1)

    print("{} começa!\n".format(jogadorAtual[1]))

    # inicia os turnos
    while totalDePecas > 0:
        # invoca o metodo específico de cada jogador.
        # armazenando sua jogada e calcula o valor total de peças restantes
        pecasRetiradas = eval(jogadorAtual[2])(totalDePecas, limitePecasPorJogada)
        totalDePecas = totalDePecas - pecasRetiradas

        # exibe as mensagem do turno
        print("O {} tirou {} peca(s)\n".format(jogadorAtual[1], pecasRetiradas))
        print("Agora resta(m) {} peça(s) no tabuleiro\n".format(totalDePecas))

        # atribui os jogadores dos turnos (anterior/proximo)
        ultimoJogador = jogadorAtual
        jogadorAtual = SelecionarProximoJogador(jogadorAtual[0] + 1)

    # exibe a mensagem do vencedor e retorna uma lista contendo, ID, Rótulo
    # e método callback
    print("Fim do jogo! O {} ganhou!".format(ultimoJogador[1]))
    return(ultimoJogador)

# Gerencia o fluxo do campeonato.
def campeonato():
    numeroDaRodada = 1
    placarGeral = {}

    # inicia as partidas
    while numeroDaRodada < 4:
        print("***** Rodada {} *****\n".format(rodada))

        # inicia uma partida e recebe como resposta uma list com dados do vencedor
        vencedor = partida()

        # atualiza os valores do placar geral
        if vencedor[1] in placarGeral:
            placarGeral[vencedor[1]] += 1
        else:
            placarGeral[vencedor[1]] = 1

        numeroDaRodada += 1

    print("fim")

# Função de entrada do programa.
def main():
    # solicita ao usuário escolher um modo de jogo (Partida Isolada ou Campeonato)
    modoDeJogo = ModoDeJogo()

    # invoca o modo de jogo escolhido
    partida() if modoDeJogo == 1 else campeonato()

# chama a função de entrada
main()
