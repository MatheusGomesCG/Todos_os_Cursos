import os

lista_de_compras = []

while True:

    choice_menu = input('[i]nserir [a]pagar [l]istar: ')

    if choice_menu == 'i':

        #caso o sistema for mac/linux usar clear
        os.system('cls')

        item_da_loja = input('Digite o item da loja: ')

        lista_de_compras.append(item_da_loja)

        print('Item adicionado com sucesso!')
    
    elif choice_menu == 'a':

        if len(lista_de_compras) > 0:

            deletar_item_da_lista = input('Digite o indice: ')
            
            if deletar_item_da_lista.isnumeric():

                numero_do_item_excluir = int(deletar_item_da_lista)

                if numero_do_item_excluir >= 0 and numero_do_item_excluir < len(lista_de_compras):

                    print(f'O item {lista_de_compras[numero_do_item_excluir]} foi excluído com sucesso!')

                    lista_de_compras.pop(numero_do_item_excluir)

                else:

                    print('Valor incorreto')
            
            else:

                print('Digite apenas números')
        else:

            print('Lista vazia!')

    elif choice_menu == 'l':

        #caso o sistema for mac/linux usar clear
        os.system('cls')

        if len(lista_de_compras) > 0:

            for indice, nome in enumerate(lista_de_compras):

                print(indice, nome)

        else:

            print('Lista vazia!')
    
    else:

        print('Digite uma entrada válida')