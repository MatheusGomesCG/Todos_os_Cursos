cpf_usuario = input('Digite seu CPF Ex: 999.999.999-99: ')

nove_digitos = cpf_usuario[:9]
contador_regressivo_1 = 10
resultado_digito_1 = 0

for digito in nove_digitos:
    resultado_digito_1 += int(digito) * contador_regressivo_1
    contador_regressivo_1 -= 1

digito = (resultado_digito_1 * 10) % 11
digito = digito if digito <= 9 else 0

cpf_2 = nove_digitos + str(digito)
contador_regressivo_2 = 11
resultado_digito_2 = 0
for digito in cpf_2:
    resultado_digito_2 += int(digito) * contador_regressivo_2
    contador_regressivo_2 -= 1

digito = (resultado_digito_2 * 10) % 11
digito = digito if digito <= 0 else 0

