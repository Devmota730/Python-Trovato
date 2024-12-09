


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
print(varTexto[5]) # estra o 5 caracteres da palavra
print(varTexto[6:]) #traz todos os caracteres da depois da 6 posição

# Eliminar espaços indesejados
Nome = 'leonardo amancio da mota'
print(Nome.strip())
print('tamanho A com strip: ',len(Nome.strip())) # o strip faz um copia das letras, o len conta o tamanho
print(len(Nome.strip()))

# concatenação com strings

print('-'.join(Nome)) # adiciona o - em cada lestra da string
print('.'.join(CPF))







