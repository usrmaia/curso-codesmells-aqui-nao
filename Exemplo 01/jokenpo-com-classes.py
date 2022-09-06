import random
import time

class Jokenpo():
  def __init__(self):
    self.escolha = 0
    self.maquina = 0

  def jokenpo(self):
    jogadas = ['PEDRA', 'PAPEL', 'TESOURA']
    print('''Suas opções:
    [ 1 ] PEDRA
    [ 2 ] PAPEL
    [ 3 ] TESOURA''')

    self.escolha = int(input('DIGITE AQUI: '))
    self.maquina = random.choice(jogadas)
    self.compara_jogadas()

    # jogar novamente  
    estado = " "
    while estado != 'sim' and estado != 's' and estado != 'n' and estado != 'não' and estado != 'nao':
        estado = str(input('Deseja continuar? [S/N]: ')).lower().strip()
        if estado == 'sim' or estado == 's':
            self.jokenpo()
        else:
            break
  
  def compara_jogadas(self):
    if self.escolha == 1:  # JOGADOR ESCOLHEU PEDRA
        self.iniciar_contagem()
        self.compara_escolha_1_maquina()
    elif self.escolha == 2:  # JOGADOR ESCOLHEU PAPEL
        self.iniciar_contagem()
        self.compara_escolha_2_maquina()
    elif self.escolha == 3:  # JOGADOR ESCOLHEU TESOURA
        self.iniciar_contagem()
        self.compara_escolha_3_maquina()
    else:
        print('\033[31m{}ERROR{}\033[m'.format('=-=' * 10, '=-=' * 10))
        print('\033[31m                         OPÇÃO INVÁLIDA\033[m')
        print('\033[31m{}ERROR{}\033[m'.format('=-=' * 10, '=-=' * 10))
  
  def iniciar_contagem(self):
    print('JO...')
    time.sleep(0.6)
    print('KEN...')
    time.sleep(0.6)
    print('PO...!!')
    time.sleep(0.6)
  
  def compara_escolha_1_maquina(self):
    if self.maquina == 'PEDRA':  # COMPUTADOR ESCOLHEU PEDRA
        print('\033[1;33m=-=-=-=-=-=-=-=EMPATE!!!=-=-=-=-=-=-=-=\033[m '
                '\nO computador escolheu {} \ne o jogador PEDRA!!.'.format(self.maquina))
    elif self.maquina == 'PAPEL':  # COMPUTADOR ESCOLHEU PAPEL
        print('\033[1;31m=-=-=-=-=-=-=-=DERROTA!!!=-=-=-=-=-=-=-=\033[m '
                '\nO computador escolheu {} \ne o jogador PEDRA!!.'.format(self.maquina))
    elif self.maquina == 'TESOURA':  # COMPUTADOR ESCOLHEU TESOURA
        print('\033[1;32m=-=-=-=-=-=-=-=VITÓRIA!!!=-=-=-=-=-=-=-=\033[m '
                '\nO computador escolheu {} \ne o jogador PEDRA!!'.format(self.maquina))
  
  def compara_escolha_2_maquina(self):
    if self.maquina == 'PEDRA':  # COMPUTADOR ESCOLHEU PEDRA
        print('\033[1;32m=-=-=-=-=-=-=-=VITÓRIA!!!=-=-=-=-=-=-=-=\033[m '
                '\nO computador escolheu {} \ne o jogador PAPEL!!.'.format(self.maquina))
    elif self.maquina == 'PAPEL':  # COMPUTADOR ESCOLHEU PAPEL
        print('\033[1;33m=-=-=-=-=-=-=-=EMPATE!!!=-=-=-=-=-=-=-=\033[m '
                '\nO computador escolheu {} \ne o jogador PAPEL!!.'.format(self.maquina))
    elif self.maquina == 'TESOURA':  # COMPUTADOR ESCOLHEU TESOURA
        print('\033[1;31m=-=-=-=-=-=-=-=DERROTA!!!=-=-=-=-=-=-=-=\033[m '
                '\nO computador escolheu {} \ne o jogador PAPEL!!'.format(self.maquina))
  
  def compara_escolha_3_maquina(self):
    if self.maquina == 'PEDRA':  # COMPUTADOR ESCOLHEU PEDRA
        print('\033[1;31m=-=-=-=-=-=-=-=DERROTA!!!=-=-=-=-=-=-=-=\033[m '
                '\nO computador escolheu {} \ne o jogador TESOURA!!.'.format(self.maquina))
    elif self.maquina == 'PAPEL':  # COMPUTADOR ESCOLHEU PAPEL
        print('\033[1;32m=-=-=-=-=-=-=-=VITÓRIA!!!=-=-=-=-=-=-=-=\033[m '
                '\nO computador escolheu {} \ne o jogador TESOURA!!.'.format(self.maquina))
    elif self.maquina == 'TESOURA':  # COMPUTADOR ESCOLHEU TESOURA
        print('\033[1;33m=-=-=-=-=-=-=-=EMPATE!!!=-=-=-=-=-=-=-=\033[m '
                '\nO computador escolheu {} \ne o jogador TESOURA!!'.format(self.maquina))
    
if __name__ == '__main__':
    j = Jokenpo()
    j.jokenpo()