# Exemplo 1

x = 12
while x < 23:
    print(x)
    x = x +1

# adivinhe o numero que estou pensando

numero_secreto = 12
numero_digitado = 0
tentativa = 0
while numero_digitado != numero_secreto:
    numero_digitado = int(input('Adivinhe o numero que estou pensando?'))
    print()
    if numero_secreto == numero_digitado:
        print('Parabeins, você acertou, numero secreto é', numero_secreto)
        print('você conseguiu acerta com :' , tentativa, 'tentativas')

    else:
        print('Não foi dessa vez, tente de novo: ')
        tentativa = tentativa + 1 

