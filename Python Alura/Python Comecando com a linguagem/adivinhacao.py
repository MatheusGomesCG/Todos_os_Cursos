def jogar():

    import random

    print("*******************************************")
    print("*****Bem-vindo ao jogo de adivinhação******")
    print("*******************************************")
    print("Você tem que adivinhar um número de 1 a 100")

    numero_adivinhacao = round(random.randrange(1, 101))

    while(True):
        
        escolha_dificuldade = \
        (input('''
    Escolha uma das opções abaixo:
        (1) - Fácil
        (2) - Médio
        (3) - Difícil
        Digite uma das opções: '''))

        verificar_escolha = escolha_dificuldade.isdigit()

        if (verificar_escolha):

            escolha_dificuldade = int(escolha_dificuldade)

            if (escolha_dificuldade == 1):
                quantidade_de_tentativas = 10
                break
            
            elif (escolha_dificuldade == 2):
                quantidade_de_tentativas = 5
                break
            
            elif (escolha_dificuldade == 3):
                quantidade_de_tentativas = 3
                break
            
            else:
                print("Digite uma opção válida")
        else:
            print("Digite apenas números")
        
    while(True):
        
        if (quantidade_de_tentativas > 0):

            print(f'O número de tentativas é {quantidade_de_tentativas}')
            input_do_usuario = input("Digite sua tentativa: ")

            validacao_usuario = input_do_usuario.isdigit()

            if (validacao_usuario):

                input_do_usuario = int(input_do_usuario)

                condicao_do_jogo = input_do_usuario > 0 and input_do_usuario < 101

                if condicao_do_jogo:

                    if (input_do_usuario == numero_adivinhacao):
                        print(f'Parabéns você acertou o número {numero_adivinhacao}')
                        break
                    
                    elif (input_do_usuario != numero_adivinhacao):
                        quantidade_de_tentativas -= 1
                        print(f'Você errou!')

                else:
                    print("Digite um número entre 1 e 100")

            else:
                print("Digite apenas números")

        else:
            print()
            print("Você perdeu")
            break

if(__name__ == "__main__"):
    jogar()