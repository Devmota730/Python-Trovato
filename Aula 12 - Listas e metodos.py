
# cria lista

minhaLista = []

minhaLista = ['Java', 'Python', 'PHP', 'Cobol']

print(type(minhaLista))

# Tamanho da lista

print('tamanho da lista:', len(minhaLista))

# unificar as lista

minhaLista2 = ['java', 'PHP', 'cobo']

minhaListaUnion = minhaLista + minhaLista2

print(minhaListaUnion)

# duplica os elemento de uma lista
listaduplicada = minhaLista * 2
print(listaduplicada)

# verificar elementos na lista

print('Python' in minhaLista) # pesquisa string dentro da lista
print()

# trabalhar com as lista

listNu = [2,4,54,67,12,345,23,12,32,45,21]
print()
print('o minino é: ', min(listNu))
print('valor maximo:', max(listNu))
print('soma da lista: ', sum(listNu))
print()
# metodos append
minhaLista.append('Final') # append adiciona no final da lista
print(len(minhaLista))
print()
# insert
minhaLista3 = minhaLista # inseri na lista e posição
print('minhalista3: ', minhaLista3)
minhaLista3.insert(1, 'JavaScript')
print(minhaLista3)
print()
# pop sem parametro, remoce o ultimo elemento
minhaLista3.pop(2) # elimina o elemento da posição
print(minhaLista3) 
# remove da lista
# minhaLista3.remove('Java')
print()
print(minhaLista3)

# shot  / reverse
minhaLista.sort() # ordena a lista por A,B,C
print('minha lista sort:', minhaLista)

minhaLista.reverse()
print(minhaLista)
minhaLista = minhaLista * 4

print('QTD', minhaLista.count('PHP')) # conta quantidade na lista


