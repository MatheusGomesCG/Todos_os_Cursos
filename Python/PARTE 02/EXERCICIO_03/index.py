perguntas = [
    {
        'Pergunta': 'Quanto é 2+2',
        'Opções': ['1', '2', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*2',
        'Opções': ['5', '10', '15', '20', '25'],
        'Resposta': '10',
    }
]

acertos = 0

for pergunta in perguntas:
    
    for questao in pergunta.items():
        if questao[0] == 'Pergunta':
            print(f'{questao[1]} ?')
            print()
        if questao[0] == 'Opções':
            print('Opções:')
            print(f'a) {questao[1][0]}')
            print(f'b) {questao[1][1]}')
            print(f'c) {questao[1][2]}')
            print(f'd) {questao[1][3]}')
            print(f'e) {questao[1][4]}')
    
    while True:
        
        alternativa = input('Escolha uma opção: ').lower()

        if alternativa in ['a', 'b', 'c', 'd', 'e']:
            if pergunta['Opções'][ord(alternativa) - ord('a')] == pergunta['Resposta']:
                print('Acertou')
                acertos += 1
                break
            else:
                print('Errou')
                break
        else:
            print('Digite uma alternativa válida')
    

print(f'Você acertou {acertos} de {len(perguntas)}!')
