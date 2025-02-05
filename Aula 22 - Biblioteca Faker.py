import numpy as np
from faker import Faker
import pandas as panda

fake = Faker(locale='pt-BR')
fakeV = Faker(locale=['pt-br','es-ES', 'en-US'])
print()


#como usar o Faler

print('enderço',fake.address())
print('Email',fake.ascii_email())
print('MAC PC', fake.address())
print(fake.ascii_company_email())
print(fake.administrative_unit())

a = np.array([5])
for i in range(2):
    a = fake.name_male()
    print('Array',a)

print(fake.random_digit_not_null())
print(fake.year())
print(fake.day_of_week())
print(fake.date_time())
print(fake.image_url())
print(fake.cellphone_number())
print(fake.city())
print(fake.neighborhood())


# aplicação da biblioteca

nome = []
empresa = []
pais = []
funcao = []
data_nascimento = []

for i in range(3):
    nome.append(fake.name())
    empresa.append(fake.company())
    pais.append(fake.country())
    funcao.append(fake.job())
    data_nascimento.append(fake.date_of_birth())

print(nome)  

# Gerar um data frame

df = panda.DataFrame({

    'nome': nome,
    'empresa': empresa,
    'pais': pais,
    'funcão': funcao,
    'data_nascimento': data_nascimento

})

print(df)

df.to_csv('./dados_fake.csv', index=False)

#Diversos 
print('teste', fake.random_letter()) # uma letra
print('teste random', fake.random_letters(8)) # 8 letras aleatorias
print('Ano',fake.year())
print('Data ',fake.date())
print(fake.date_time()) # data com horas
print(fake.time()) # hora qualquer
print(fake.url())
print(fake.cpf())




print()




