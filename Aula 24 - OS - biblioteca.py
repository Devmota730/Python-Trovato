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




