nome_usuario = input('Digite seu primeiro nome: ')

condicao = nome_usuario.isalpha()

contar_nome = len(nome_usuario)

if condicao:

    if contar_nome <= 4:
            print('Seu nome é curto')

    elif contar_nome > 4 and contar_nome <= 6:
            print('Seu nome é normal')

    else:
            print('Seu nome é muito grande')

else:

    print('Digite apenas letras e seu primeiro nome')
    