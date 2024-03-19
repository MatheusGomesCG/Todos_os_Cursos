def multiplica (*args):
    total = 1
    for numero in args:
        total *= numero
    return total

numeros = 1, 2, 3, 4, 5, 6, 7, 8, 9, 78, 89
valor_final = multiplica(*numeros)
print(valor_final)

def par_ou_impar (x):
    if (x % 2) == 0:
        return f'O número [{x}]: é par'
    else:
        return f'O número [{x}]: é ímpar'

pares_e_impares = par_ou_impar(8)
print(pares_e_impares)
