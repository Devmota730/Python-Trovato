


print('text'.capitalize()) # deixa a primeira letra Mascular

# concatenação de textos
textoA = 'curso'
textoB =   'de algoritmos'
textoC = 'python'

resultado = textoA + ' ' + textoB + ''+ textoC
print(resultado)

# Metodos para textos
CPF = '60543977374'
varTexto = 'leonardo mota'
# adiciona a direito ou a esquerda de um teste
print(varTexto.rjust(len(CPF), '0'))
print(varTexto.ljust(len(CPF), '0'))
print(varTexto.center(20), '/') # centraliza o texto
print('x' * 15) # preenche 15x 

# alteração da caixa de palavras

print('teste do title', varTexto.title()), # deixa em maisculo a iniciais
print(varTexto.upper()) 
print(varTexto.lower())

print('LeOnardO'.swapcase()) # invert maisculos e minisculos

# Len, verifica o tamanho de uma string
print(len(varTexto))
print(len('leonardo amancio da mota'))
 
# Extração de texto
print(varTexto[0:5]) #extrai da posição 0 a posição 4








