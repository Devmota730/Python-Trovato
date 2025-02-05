import socket
import getpass
import requests
import subprocess
import platform
import wmi
import win32com.client
import psutil as ps
import cpuinfo as cpu
from tkinter import messagebox
import re
from datetime import datetime


system_info = platform.uname()

# Coletar o hostname do computador
hostname = socket.gethostname()

# Coletar o username do usuário logado
username = getpass.getuser()

# Coletar o domínio do computador
try:
    domain = subprocess.check_output('wmic computersystem get domain', shell=True).decode().split('\n')[1].strip()
except subprocess.CalledProcessError:
    domain = "N/A"
# versao do windows 

def get_windows_version():
    version = platform.version()
    build_number = int(version.split('.')[2])
    
    if build_number >= 22000:
        return "Windows 11"
    elif build_number >= 10240:
        return "Windows 10"
    else:
        return "Versão do Windows desconhecida"

windows_version = get_windows_version()
versao = (f" {windows_version}")

# verifica se é Desktop ou notebook

def get_computer_type():
    c = wmi.WMI()
    for system in c.Win32_SystemEnclosure():
        for chassis_type in system.ChassisTypes:
            if chassis_type == 3:
                return "Desktop"
            elif chassis_type in [8, 9, 10, 14]:
                return "Laptop"
    return "Unknown"

computer_type = get_computer_type()


# pega versao do office
def get_office_package():
    try:
        # Tentar acessar o Word
        word = win32com.client.Dispatch("Word.Application")
        version = word.Version
        word.Quit()

        # Determinar o pacote do Office com base na versão
        if "16.18" >= version:
            return "Office 365"
        elif "16.0" <=  version:
            return "Office 2019"
        else:
            return f"Versão desconhecida: {version}"
    except Exception as e:
        return f"Erro ao obter a versão do Office: {e}"

office_package = get_office_package()


# pega a informação do fabricante
def get_computer_manufacturer():
    c = wmi.WMI()
    for system in c.Win32_ComputerSystem():
        return system.Manufacturer

manufacturer = get_computer_manufacturer()

# pega informação do modelo 
def get_computer_model():
    c = wmi.WMI()
    for system in c.Win32_ComputerSystem():
        return system.Model

model = get_computer_model()

# Pepga informação da memoria
def get_ram_size():
    c = wmi.WMI()
    total_memory = 0
    for memory in c.Win32_PhysicalMemory():
        total_memory += int(memory.Capacity)
    total_memory_gb = total_memory / (1024 ** 3)  # Converter bytes para gigabytes
    return total_memory_gb

ram_size_gb = get_ram_size()
RAM = (f"{ram_size_gb:.2f} GB RAM")

# Pegar o tamanho do disco rigido
disk_usage = ps.disk_usage('/')
total_size = disk_usage.total // (1024 ** 3) 
SSD = (f" {total_size} GB")

# pega a versão do processador
info = cpu.get_cpu_info()
CPUG = (info['brand_raw'])

# Coleta a Descrição do equipamento
strComputer = "."
objWMIService = win32com.client.Dispatch("WbemScripting.SWbemLocator")
objSWbemServices = objWMIService.ConnectServer(strComputer, "root\\cimv2")
colItems = objSWbemServices.ExecQuery("SELECT * FROM Win32_OperatingSystem")

for objItem in colItems:
    Descrição = {objItem.Description}


#Determina ano do equiapamento


import subprocess
import re
from datetime import datetime

def get_processor_info():
    # Executa o comando para obter informações do processador
    result = subprocess.run(['wmic', 'cpu', 'get', 'name'], stdout=subprocess.PIPE)
    # Decodifica o resultado para obter o nome do processador
    processor_info = result.stdout.decode().strip().split('\n')[1]
    return processor_info

def extract_processor_model(processor_info):
    # Extrai a parte relevante do nome do processador (ex: i7-7700)
    match = re.search(r'i\d-\d{4}', processor_info)
    if match:
        return match.group()
    return None

def get_computer_manufacture_year():
    # Executa o comando para obter o ano de fabricação do computador
    result = subprocess.run(['wmic', 'bios', 'get', 'releasedate'], stdout=subprocess.PIPE)
    # Decodifica o resultado para obter a data de lançamento
    release_date = result.stdout.decode().strip().split('\n')[1]
    # Extrai o ano da data de lançamento
    manufacture_year = int(release_date[:4])
    return manufacture_year

def calculate_age(processor_model):
    current_year = datetime.now().year
    # Dicionário com os anos de lançamento dos processadores
    release_years = {
        'i7-7700': 2017,
        'i7-1165': 2022,
        'i5-1165': 2022,
        'i7-6600': 2016,
        'i5-1135': 2021,
        'i7-8550': 2017,
        'i7-8565': 2018,
        'i5-1021': 2019,
        'i7-1021': 2019,
        'i5-7200': 2016,
        'i5-4300': 2013,
        'i7-4600': 2013,
        'i5-4600': 2013,
        'i5-3337': 2012,
        'i5-5300': 2015,
        'i3-2120': 2012,
        'i9-1390': 2023,
        'i5-3320': 2013,
        'i3-4005': 2013,
        # Adicione outros modelos e seus anos de lançamento conforme necessário
    }
    
    if processor_model in release_years:
        release_year = release_years[processor_model]
        age = current_year - release_year
    else:
        # Se o modelo do processador não estiver no dicionário, obter o ano de fabricação do computador
        manufacture_year = get_computer_manufacture_year()
        age = current_year - manufacture_year
    
    return age

processor_info = get_processor_info()
processor_model = extract_processor_model(processor_info)

if processor_model:
    age = calculate_age(processor_model)
    if age is not None:
        print(f"A idade do seu computador com base no modelo do processador ({processor_model}) é: {age} anos.")
    else:
        print("Não foi possível determinar a idade do processador.")
else:
    print("Não foi possível extrair o modelo do processador.")

Anos = (f"{age} anos")


# Preence os dados dos campus
Regional = "Nordeste"
Marca = "Wydem"
Unidade = "UniFanor"


# URL do formulário e dados a serem enviados
form_url = "https://docs.google.com/forms/d/e/1FAIpQLSexKYmHwsLTfTGQjLu4c0eA_JZYdMPairLIr1tgzNVmCbaVVg/formResponse"
form_data = {
    "entry.586116077": Regional,
    "entry.1962317397": Marca,
    "entry.663803946": Unidade,
    "entry.2043695424": hostname,  # Substitua 'entry.2005620554' pelo nome correto do campo no formulário
    "entry.180468983": username,   # Substitua 'entry.1234567890' pelo nome correto do campo no formulário
    "entry.305050396": domain,      # Substitua 'entry.9876543210' pelo nome correto do campo no formulário
    "entry.1598784526": versao, 
    "entry.1689058791": computer_type,
    "entry.1631495942": office_package,
    "entry.1995549497": manufacturer,
    "entry.809184448": model,
    "entry.508585755": RAM,
    "entry.9233005": SSD,
    "entry.1650346718": CPUG,
    "entry.250274945": Descrição,
    "entry.186411303": Anos
}

# Caixa de confirmação
confirmation = messagebox.askyesno(
    "Confirmação",
    f"Você selecionou a regional: {Regional}\n"
    f"Marca: {Marca}\n"
    f"Unidade: {Unidade}\n"
    f"Hostname: {hostname}\n"
    f"Username: {username}\n"
    f"Domain: {domain}\n"
    f"Versão: {versao}\n"
    f"Tipo de Computador: {computer_type}\n"
    f"Pacote Office: {office_package}\n"
    f"Fabricante: {manufacturer}\n"
    f"Modelo: {model}\n"
    f"RAM: {RAM}\n"
    f"SSD: {SSD}\n"
    f"CPU/GPU: {CPUG}\n"
    f"Descrição: {Descrição}\n"
    f"Anos: {Anos}\n"
    "Deseja enviar?"
)

if confirmation:
    try:
        # Enviar os dados para o formulário
        response = requests.post(form_url, data=form_data)

        # Verificar se a submissão foi bem-sucedida
        if response.status_code == 200 or response.status_code == 302:
            print("Todas as informações foram enviadas ao Forms!")
        else:
            print(f"Falha ao enviar o hostname, username e domínio. Status code: {response.status_code}")
    except Exception as e:
        print(f"Ocorreu um erro ao enviar os dados: {e}")
else:
    print("Envio do formulário cancelado.")


