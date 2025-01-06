# estrutura do IF

# exemplo 1
# exemplo 2
# exemplo 3 - clacula a idade com base na data idade
# 

from datetime import date

# calculo da idade
data_nascimento = date(1995,4,3)
idade = int((date.today() - data_nascimento).days/365.25)
print(idade) 

# calculo do dia do nascimento

data = date(1998,2,4)
dia_semana = data.isoweekday()

if dia_semana >= 1 and dia_semana <= 5:
    print('Na semana', data.strftime("%A"))
else:
    print(' no final de semana', data.strftime("%A"))

# 
dia_da_semana = ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo']
dia_hoje = data.isoweekday()

if dia_hoje >= 1 and dia_hoje <= 5:
    print('Dia da semana', dia_da_semana[dia_hoje -1])

else:
    print('No final de semana', dia_da_semana[dia_hoje -1])

