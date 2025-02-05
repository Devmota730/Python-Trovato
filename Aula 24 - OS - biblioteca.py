import os

print('usuario logado', os.environ.get('username'))
## print('lista a pasta do path', os.environ.get('path'))
print('Nomde do computador', os.environ.get('computername'))


# Mostra os paramento da invorin

for param in os.environ:
    print('param:', f"`{param}: os.environ.get(param)")

print()

unidade = 'c:\\'
caminhoA = 'temp'
caminhoB = 'podeApagar'

print(os.path.join(unidade, caminhoA,caminhoB)) # junta os caminho
print()
print(os.getcwd()) # caminho da pasta
print()

caminhoCompleto = os.path.join(os.getcwd(), 'Teste.py')
print('Caminho + arquivo', caminhoCompleto)
print('Caminho sem arquivo', os.path.dirname(caminhoCompleto))
print('Diretorio atual: ', os.curdir)
print()

# testa se o diretorio existe

caminhoCompleto = os.path.join(os.getcwd(), 'LS')

if os.path.exists(caminhoCompleto):
    print('A pasta ja existe')
    os.rmdir('LS')
else:
    print('A pasta não existe')
    os.mkdir('LS')
    print('A pasta foi criada: ☻')

# verifica se o caminho existe

print(os.path.isdir(caminhoCompleto)) # verifica se o caminho existe
print(os.path.isdir(caminhoA))








