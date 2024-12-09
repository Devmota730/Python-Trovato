# input - obetr dados pelo promp

import math as M

varNome = input('digite seu nome: ')

verRaio = input('informe o raio da circoferencia: ')
verResultado = M.pi * float(verRaio) ** 2 #formula de pi, PI * Raio eleve
print('Área',verResultado)
print('Compumento', 2 * M.pi * float(verRaio)) # formular do calculo do comprimento


# 2 exemplo
varTemperatura = float(input('digite o valor em celsius para farenheith : '))
valorKelvin = float(input('digite o valor em celsius para kelvin : '))
varTemperatura = (varTemperatura * 1.8) + 32
valorKelvin = valorKelvin + 273.15
print('Farenheith:', varTemperatura)
print('temperatura em', valorKelvin)

# Metodo format ,
nome = 'leo'
varIdade = 29
varProfissao = 'Programador Pleno'
varT = 'Seja Bem-vindo'
varT = '{0}, Seja bem-vido \n idade:{1} \n profissao: {2}'
print(varT.format(nome, varIdade, varProfissao))
print()

# Format 
varTemperatura - M.pi * float(verRaio) ** 2
print('Area:', varTemperatura)
print('Comprimento:', 2 * M.pi * float(verRaio))
print()

Res_final = 'Area:  {0: .1f} Celsius '
print(Res_final.format(varTemperatura))
