from jogo_da_velha import criarBoard, fazMovimento,  getInputValido, \
                            printBoard, verificaGanhador,  verificaMovimento

from minimax import movimentoIA

def vez_de_jogar(jogador, board):
    i = ""
    j = ""
    
    if(jogador == 0):
        # i,j = movimentoIA(board, jogador)
        i = getInputValido("Digite a linha: ")
        j = getInputValido("Digite a coluna: ")
    else:
        i,j = movimentoIA(board, jogador)
    
    return i, j

def validar_jogada(jogador, board, i, j):
    if(verificaMovimento(board, i, j)):
        fazMovimento(board, i, j, jogador)
        # trocar jogador
        jogador = (jogador + 1)%2
    else:
        print("A posicao informado ja esta ocupada")
    
    return jogador, board
    
jogador = 0 # jogador 1
board = criarBoard()
ganhador = verificaGanhador(board)  
while(not ganhador):
    printBoard(board)
    print("===================")
    i, j = vez_de_jogar(jogador, board)
    jogador, board = validar_jogada(jogador, board, i, j)
    ganhador = verificaGanhador(board)

print("===================")
printBoard(board)
print("Ganhador = ", ganhador)
print("===================")