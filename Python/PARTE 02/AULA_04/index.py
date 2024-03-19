x, y, *resto = 1, 2, 3, 4

print (x, y, resto)

# def soma(x, y):
#     return x + y

def soma(*args):
    total = 0
    for numero in args:
        total += numero
    return total

soma123 = soma(1, 2, 3, 4, 5, 6)
numeros = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10

outra_soma = soma(*numeros)
print(numeros, type(numeros))
print(soma123)
print(outra_soma)