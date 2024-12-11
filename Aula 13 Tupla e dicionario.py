# criação da tupla

tupla1 = 'leo','mota', 2, 3, 5
tupla2 =  ('amancio', 25, False,52, '52')

print(tupla1)
print(type(tupla1))
print(type(tupla2))
# tupla vazia

tupla4 = ()
print(type(tupla4))

# declaração explicita

tupla4 = tuple('amazonas') # armazena cada caractere em um posição
print(tupla4)
print(type(tupla4))
print(len(tupla4))

# Dicionarios

dicionarioA = {1: 'Leonardo', 2: 'mota'} # adiciona intem com ID
print('dicionario ', dicionarioA)
dicionarioA [1] = 'silva' # adiciona na posição informada
dicionarioA [3] = 'corinthians' # adiciona na tupla
print(dicionarioA)

# update em dicionanrios

dicionarioA.update({1: 'leo filho'}) 

print(dicionarioA)

# apaga itens no dicionarios

del(dicionarioA[1])
print(dicionarioA)

print('chaves ', dicionarioA.keys())
print('itens : ', dicionarioA.items())
print('valores :', dicionarioA.values())

