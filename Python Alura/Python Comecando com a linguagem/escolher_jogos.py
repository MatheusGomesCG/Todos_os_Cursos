import adivinhacao
import forca

escolha = \
int(input('''
(1) - ADIVINHACAO
(2) - FORCA
Escolha um dos jogos: '''))

if (escolha == 1):
    adivinhacao.jogar()

elif (escolha == 2):
    forca.jogar()
