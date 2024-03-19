import os

palavra_secreta = 'controle remoto'
letra_acertadas = ''
numero_tentativa = 0
total_vidas = 10
dica = 'Tem em casa'

print('*' *80)
print('Bem-vindo ao jogo da forca você tem 10 tentativas para acertar a palavra')
print(f'A dica do jogo é "{dica}"')
print('*' *80)

while True:
    print(f'Você tem {total_vidas - numero_tentativa} vidas')
    letra_do_usuario = input('Digite apenas uma letra da palavra secreta: ').lower()
        
    if letra_do_usuario.isalpha():
        
        if numero_tentativa <= 10:

            if len(letra_do_usuario) == 1:
                    
                if letra_do_usuario in palavra_secreta:
                    letra_acertadas += letra_do_usuario
                
                else:
                    numero_tentativa += 1

                palavra_formada = ''
                for letra_secreta in palavra_secreta:

                    if letra_secreta in letra_acertadas:
                        palavra_formada += letra_secreta

                    elif letra_secreta == " ":
                        palavra_formada += " "

                    else:
                        palavra_formada += '_'

                print(palavra_formada)

                if palavra_formada == palavra_secreta:
                    #caso o sistema for mac/linux usar clear
                    os.system('cls')
                    print(f'Você conseguiu a palavra era "{palavra_formada.upper()}", você tentou {numero_tentativa} até acertar')
                    letra_acertadas = ''
                    numero_tentativa = 0
                    break

                print()
            else:
                print('Digite apenas uma letra')
                continue
        else:
            print('GAME-OVER')
            break
    else:
        print('Digite apenas letras')
        continue