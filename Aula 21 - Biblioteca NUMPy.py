import numpy as np


x = np.array([1,2,3,4,5,6,7])

print(x)

# crinado um array bidirecional

xx = np.array([[1,2,3,4], [4,5,6,7], [8,9,10,11], [5,4,3,2]])

print(xx)

# Atributos

print('numero de dimenssões', xx.ndim) 
print(' numero de elementos por dimessão', xx.shape) 
print('Tamanho Size', xx.size) # tamanho do array

# criação de array básicos
print()
print('gerar array com 0', np.zeros(6)) # gera array de 6 posições
print('gera matriz com 1', np.ones(5)) # gerar arrai de 5 com 1 
print('array vazio', np.empty(6)) # gerar x posição com 0
print('Elementos sequenciais', np.arange(10)) # gerar de 0 a 9 sequencia
print('gera elementos em sequencia', np.arange(10, 20, 2)) # gera sequencia na faixa
print('Elementos linear', np.linspace(0,20, num=3)) # conta no espaço de num3

print()

# Adicionar , remover e classificar

Lista = np.array([1,2,3,4,5,6])
ListaB = np.array([7,8,9,10,1,12])
listaC = np.concatenate((Lista, ListaB)) # junta as duas listas
print(listaC)

# Remodela matriz

listaD = listaC.reshape(4, 3) # remodela a matriz
print(listaD)

listaE = np.reshape(listaD, newshape=(2, 6)) # cria uma nova matriz
print(listaE)

print()

print(Lista[Lista < 3])
print(ListaB[ListaB > 5])
print('numeros par', listaD%2 == 0)
print('restorna os numero PAR: ', listaD[listaD%2 == 0]) # retorno numeros pares da lista 
print(' numeros impares:', listaD[listaD%2 == 1]) # impares da lista
print()

print(listaD[(listaD >=3 ) & (listaD <= 5)]) # filtra com base na lista 

print()

ListaG = np.array([[1,2,3], [2,3,4]])
ListaH = np.array([[2,3,4], [2,3,4]])

print('Soma dos valores do arry', listaD.sum())
print('soma da listaG + ListaH', [ListaG + ListaH])
print('subtração das lista',[ListaG - ListaH])
print('Mutlicação das lista', [ListaH * ListaH])
print('comparação das lista', ListaG == ListaH)
print('O maior numero da lista', Lista.max())
print('o minimo da lista', Lista.min())
print('a media dos valores da lista', Lista.mean())
print('produto da matriz', x.prod())
print('valores unicos', np.unique(Lista))




