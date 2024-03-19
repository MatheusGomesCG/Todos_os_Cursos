"""
split e join com list e str
split - divide uma string
join - une uma strig
"""

frase = '     Olha só que    , coisa interessante         '
list_frases_cruas = frase.split(',')

list_frases = []
for i, frase in enumerate(list_frases_cruas):
    list_frases.append(list_frases_cruas[i].strip())

print(list_frases)

frases_unidas = ', '.join(list_frases)
print(frases_unidas)