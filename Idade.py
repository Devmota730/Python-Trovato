import platform
import subprocess
from datetime import datetime

def get_computer_age_and_manufacture_date():
    # Obter informações do sistema
    system_info = platform.uname()
    
    # Obter informações do BIOS usando o comando 'wmic' (apenas para Windows)
    try:
        bios_info = subprocess.check_output("wmic bios get releasedate", shell=True).decode().strip().split('\n')
        if len(bios_info) > 1:
            bios_date = bios_info[1].strip()
            # Remover qualquer parte extra da data
            bios_date = bios_date[:8]  # Pegar apenas os primeiros 8 caracteres
            manufacture_date = datetime.strptime(bios_date, '%Y%m%d').strftime('%d/%m/%Y')
            
            # Calcular a idade do computador
            manufacture_datetime = datetime.strptime(bios_date, '%Y%m%d')
            current_datetime = datetime.now()
            age_days = (current_datetime - manufacture_datetime).days
            age_years = age_days // 365
            age_months = (age_days % 365) // 30
            age_days = (age_days % 365) % 30
            
            return manufacture_date, age_years, age_months, age_days
        else:
            return "Não foi possível obter a data de fabricação do BIOS."
    except Exception as e:
        return str(e)

result = get_computer_age_and_manufacture_date()

if isinstance(result, tuple):
    manufacture_date, age_years, age_months, age_days = result
    print(f"Data de fabricação: {manufacture_date}")
    print(f"Idade do computador: {age_years} anos, {age_months} meses e {age_days} dias")
else:
    print(f"Erro: {result}")
