import sys

strCPF = '60543977374'
numDV1 = 0
numDV2 = 0
numcheck1 = 0
nuncheck2 = 0 

i =1 

# verifica o numero de caracteres do CPF, e adiciona 0 para manter o tamanho iguala a 11
if len(strCPF) < 11:
    difCPF = 11 -len(strCPF)
    strCPF = '0' * difCPF + strCPF

# captura digito verificador

numcheck1 = int(strCPF[9:10])
numcheck2 = int(strCPF[10:11])


# calculo do primeiro digito verificador

for i in range(1,10):
    numDV1 = numDV1 + int(strCPF[i-1:i]) * i
    


for i in range(2, 11):
    numDV2 = numDV2 + int(strCPF[i-1: i]) * (i -1)
    print(numDV2)

# extrair o resto da divisao

numDV1 = numDV1 % 11
print(numDV1)

numDV2 = numDV2 % 11
print(numDV2)

# transforma numero maior que 10 em 0

if (numDV1 == 10):
    numDV1 = 0


if (numDV2 == 10):
    numDV2 = 0

if numDV1 != numcheck1:
    sys.exit('digito verificado 1 invalido')

if numDV2 != numcheck2:
    sys.exit('digito verificado 2 invalido')

if (numDV1 == numcheck1 and numDV2 == numcheck2 ):
    print('CPF valido')
