try:
    hora_atual = input('Digite a hora atual: ')

    converter_hora = int(hora_atual)

    if converter_hora >= 0 and converter_hora <= 11:
        print('Bom dia')
    
    elif converter_hora > 11 and converter_hora <= 17:
        print('Boa tarde')

    elif converter_hora > 17 and converter_hora <= 23:
        print('Boa noite')
    
    else:
        print('Digite um horário válido')
except:
    print('Você não digitou um número inteiro')