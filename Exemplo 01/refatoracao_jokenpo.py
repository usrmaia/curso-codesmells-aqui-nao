import random
import time

def iniciar_contagem():
    print('JO...')
    time.sleep(0.6)
    print('KEN...')
    time.sleep(0.6)
    print('PO...!!')
    time.sleep(0.6)

def compara_escolha_1_maquina(maquina):
    if maquina == 'PEDRA':  # COMPUTADOR ESCOLHEU PEDRA
        print('\033[1;33m=-=-=-=-=-=-=-=EMPATE!!!=-=-=-=-=-=-=-=\033[m '
                '\nO computador escolheu {} \ne o jogador PEDRA!!.'.format(maquina))
    elif maquina == 'PAPEL':  # COMPUTADOR ESCOLHEU PAPEL
        print('\033[1;31m=-=-=-=-=-=-=-=DERROTA!!!=-=-=-=-=-=-=-=\033[m '
                '\nO computador escolheu {} \ne o jogador PEDRA!!.'.format(maquina))
    elif maquina == 'TESOURA':  # COMPUTADOR ESCOLHEU TESOURA
        print('\033[1;32m=-=-=-=-=-=-=-=VITÓRIA!!!=-=-=-=-=-=-=-=\033[m '
                '\nO computador escolheu {} \ne o jogador PEDRA!!'.format(maquina))

def compara_escolha_2_maquina(maquina):
    if maquina == 'PEDRA':  # COMPUTADOR ESCOLHEU PEDRA
        print('\033[1;32m=-=-=-=-=-=-=-=VITÓRIA!!!=-=-=-=-=-=-=-=\033[m '
                '\nO computador escolheu {} \ne o jogador PAPEL!!.'.format(maquina))
    elif maquina == 'PAPEL':  # COMPUTADOR ESCOLHEU PAPEL
        print('\033[1;33m=-=-=-=-=-=-=-=EMPATE!!!=-=-=-=-=-=-=-=\033[m '
                '\nO computador escolheu {} \ne o jogador PAPEL!!.'.format(maquina))
    elif maquina == 'TESOURA':  # COMPUTADOR ESCOLHEU TESOURA
        print('\033[1;31m=-=-=-=-=-=-=-=DERROTA!!!=-=-=-=-=-=-=-=\033[m '
                '\nO computador escolheu {} \ne o jogador PAPEL!!'.format(maquina))

def compara_escolha_3_maquina(maquina):
    if maquina == 'PEDRA':  # COMPUTADOR ESCOLHEU PEDRA
        print('\033[1;31m=-=-=-=-=-=-=-=DERROTA!!!=-=-=-=-=-=-=-=\033[m '
                '\nO computador escolheu {} \ne o jogador TESOURA!!.'.format(maquina))
    elif maquina == 'PAPEL':  # COMPUTADOR ESCOLHEU PAPEL
        print('\033[1;32m=-=-=-=-=-=-=-=VITÓRIA!!!=-=-=-=-=-=-=-=\033[m '
                '\nO computador escolheu {} \ne o jogador TESOURA!!.'.format(maquina))
    elif maquina == 'TESOURA':  # COMPUTADOR ESCOLHEU TESOURA
        print('\033[1;33m=-=-=-=-=-=-=-=EMPATE!!!=-=-=-=-=-=-=-=\033[m '
                '\nO computador escolheu {} \ne o jogador TESOURA!!'.format(maquina))

def compara_jogadas(escolha, maquina):
    if escolha == 1:  # JOGADOR ESCOLHEU PEDRA
        iniciar_contagem()
        compara_escolha_1_maquina(maquina)
    elif escolha == 2:  # JOGADOR ESCOLHEU PAPEL
        iniciar_contagem()
        compara_escolha_2_maquina(maquina)
    elif escolha == 3:  # JOGADOR ESCOLHEU TESOURA
        iniciar_contagem()
        compara_escolha_3_maquina(maquina)
    else:
        print('\033[31m{}ERROR{}\033[m'.format('=-=' * 10, '=-=' * 10))
        print('\033[31m                         OPÇÃO INVÁLIDA\033[m')
        print('\033[31m{}ERROR{}\033[m'.format('=-=' * 10, '=-=' * 10))

# TODO
# aaaaaaaaaaaa

def jokenpo():
    jogadas = ['PEDRA', 'PAPEL', 'TESOURA']
    print('''Suas opções:
    [ 1 ] PEDRA
    [ 2 ] PAPEL
    [ 3 ] TESOURA''')

    escolha = ""
    escolha = int(input('DIGITE AQUI: '))
    maquina = random.choice(jogadas)
    compara_jogadas(escolha, maquina)

    # jogar novamente    
    continuar = ' '
    estado = continuar != 'sim' and continuar != 's' and continuar != 'n' and continuar != 'não' and continuar != 'nao'
    while estado:
        continuar = str(input('Deseja continuar? [S/N]: ')).lower().strip()
        if continuar == 'sim' or continuar == 's':
            jokenpo()
        else:
            break


if __name__ == '__main__':
    jokenpo()
