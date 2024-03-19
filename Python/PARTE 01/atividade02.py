primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')

condicao1 = primeiro_valor > segundo_valor
condicao2 = segundo_valor > primeiro_valor

if condicao1:
    print(f'{primeiro_valor=} é maior do que {segundo_valor=}')
else:
    print(f'{segundo_valor=} é maior do que {primeiro_valor=}')