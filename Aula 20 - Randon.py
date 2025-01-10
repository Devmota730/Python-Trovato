import random as rd

print('gera numero aleatorio', rd.randrange(1,60)) # gera valores na faixa

print('gera valores aleatorio', rd.random)

lista = rd.sample(range(20), 6)
print('gera QTD de numero pedido: ', lista)
print('Sorted,. bota em ordem decrescente: ',sorted(lista) )
print('')
lista.sort() # ordena a llista ,
print('sort: ', lista) 

print('Randit', rd.randint(1, 12)) # gera numero int dentro da faixa

print()
print('esolhe na lista', rd.choice(lista))
print()
print('Choose dois: ', rd.choice(['A', 'B', 'c', 'D']))
print()
rd.shuffle(lista)
print('shuffle, ', lista) #embaralha lista

print('Sample: ', rd.sample(lista, 2))  # escolhe dois valores da lista
print()


