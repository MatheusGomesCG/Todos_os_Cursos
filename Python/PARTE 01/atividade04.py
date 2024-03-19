try:
    numero_inteiro = input('Digite um número inteiro: ')

    converter_numero_inteiro = int(numero_inteiro)

    numero_par = converter_numero_inteiro % 2

    condicao = numero_par == 0

    if condicao:
        print('Este número é par')
    else:
        print('Este número é ímpar')

except:
    print('Você não digitou um número inteiro')