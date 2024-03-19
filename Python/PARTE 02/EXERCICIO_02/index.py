# Exercícios
# Crie funções que duplicam, triplicam e quadruplicam
# o número recebido como parâmetro

def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return f'{numero} * {multiplicador} = {numero * multiplicador}'
    return multiplicar

duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)

print(duplicar(5))
print(triplicar(3))