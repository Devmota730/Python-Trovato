# tratamento de erro.

Valorx = 10
try:
    print(Valorx)

except:
    print('valor não encontrado')


try:
    print(x)
except NameError:
    print('variavel x não foi declarada')
print()
valorB = input('informe um valor para valida')
try:
    print(valorB)
except:
    print('valor não conhecido')
else:
    print('valor validado')

print()

# Abertura de arquivo

try:
    arquivo = open('open.txt')
    try:
        arquivo.write('adicionado ao arquivo')
    except:
        print('não foi possivel adiciona ao arquivos')
    finally:
        arquivo.close()
except:
    print('há problemas em abrir o seu arquivo')



