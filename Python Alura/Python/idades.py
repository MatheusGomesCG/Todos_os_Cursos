idades = [15, 87, 32, 65, 56, 32, 49, 37]

for indice, idade in enumerate(idades):
    print(f"{indice} - {idade}")

usuarios = [
    ("Guilherme", 37, 1981),
    ("Daniel", 31, 1987),
    ("Paulo", 39, 1979)
]

for nome, _, _ in usuarios:
    print(nome)

print(sorted(idades))
print(list(reversed(idades)))
print(sorted(idades, reverse=True))

idades.sort()

print(idades)

#Para colocar todas as (>, <, >=, <=) dentro do objeto
#from functools import total_ordering
# @total_ordering
# class ContaSalario: 