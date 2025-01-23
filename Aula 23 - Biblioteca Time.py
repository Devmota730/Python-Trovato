import time

relogio = time.localtime()

print()

Ano = relogio.tm_year
Mes = relogio.tm_mon
Dia = relogio.tm_mday

hora = relogio.tm_hour
minuto = relogio.tm_min
segundo = relogio.tm_sec
DiadoAno = relogio.tm_yday
DiadaSemana = relogio.tm_wday

print(Dia, Mes, Ano)

print(hora, minuto,segundo, DiadoAno)

print()

relogio_inicio = time.localtime()
relogio_em_segundos = time.mktime(relogio_inicio) # transforma hora em segundos
relogio_em_segundos =+ 10
relogio_fim = time.localtime(relogio_em_segundos)

print()

while True:
    localTime = time.localtime()
    result = time.strftime('%H:%M:%S %p', localTime)
    print(result)
    time.sleep(1)
    print(relogio_fim)

    if localTime == relogio_fim:
        exit()




