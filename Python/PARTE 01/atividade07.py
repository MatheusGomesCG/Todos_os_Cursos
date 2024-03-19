nome_usuario = input('Digite seu nome: ')
nova_string = ""
i = 0

while i < len(nome_usuario):

    nova_string += (f'*{nome_usuario[i]}')
    i += 1

print(nova_string)