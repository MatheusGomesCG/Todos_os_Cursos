usuarios_data_science = [15, 23, 43, 56]
usuarios_machine_learning = [13, 23, 56, 42]

assistiram = usuarios_data_science.copy()
assistiram.extend(usuarios_machine_learning)
print(assistiram)

usuarios_data_science = {15, 23, 43, 56}
usuarios_machine_learning = {13, 23, 56, 42}

'''
Utilizar o | para juntar conjuntos;
Utilizar o & para juntar apenas números que estão no mesmo conjunto;
Utilizar o - para remover números repetidos que estão nos dois conjuntos;
O que é ou (^) exclusivo.
'''

union = usuarios_data_science | usuarios_machine_learning #union
print(union)
interscicion = usuarios_data_science & usuarios_machine_learning #interseção
print(interscicion)
dif = usuarios_data_science - usuarios_machine_learning
print(dif)
exc = usuarios_data_science ^ usuarios_machine_learning
print(exc)

#Adiciona dentro do conjunto
usuarios_data_science.add(25)

#Congela o set e não deixar adicionar
usuarios = {1, 3, 5, 10, 20, 13}
usuarios = frozenset(usuarios)
print(type(usuarios))

apresentacao = "Bem vindo meu nome é Matheus eu gosto muito de programar"
print(apresentacao.split())
apresentacao_set = set(apresentacao.split())
print(apresentacao_set)

aparicoes = {
    "Guilherme" : 1,
    "Cachorro" : 2,
    "Nome" : 1,
    "vindo" : 1
}

print(type(aparicoes))

print(aparicoes["Guilherme"])

#Adicionando em dicionário
aparicoes["Matheus"] = 10
print(aparicoes)

#Excluindo
del aparicoes["vindo"]
print(aparicoes)

print("Matheus" in aparicoes)

for elemento in aparicoes:
    print(elemento)

for elemento in aparicoes.values():
    print(elemento)

print(1 in aparicoes.values())

for elemento in aparicoes.items():
    print(elemento)

for elemento, chave  in aparicoes.items():
    print(f"{elemento} : {chave}")

d = {'coding': 'good', 'thinking': 'better'}
print(d.get('coding'))

