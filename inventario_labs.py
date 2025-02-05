import tkinter as tk
from tkinter import messagebox, filedialog
import requests

import tkinter as tk
from tkinter import messagebox
import socket
import requests
import getpass
import subprocess
import platform
import wmi
import win32com.client
import psutil as ps
import cpuinfo as cpu


# Coletar o username do usuário logado
username = getpass.getuser()

# Coletar o hostname do computador
hostname = socket.gethostname()

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
#print(f"Computer Type: {computer_type}")




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

#office_package = get_office_package()
#print(office_package)

# pega a informação do fabricante
def get_computer_manufacturer():
    c = wmi.WMI()
    for system in c.Win32_ComputerSystem():
        return system.Manufacturer

manufacturer = get_computer_manufacturer()
#print(f"Manufacturer: {manufacturer}")


# pega informação do modelo 
def get_computer_model():
    c = wmi.WMI()
    for system in c.Win32_ComputerSystem():
        return system.Model

model = get_computer_model()
#print(f"Model: {model}")

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
#strComputer = "."
#objWMIService = win32com.client.Dispatch("WbemScripting.SWbemLocator")
#objSWbemServices = objWMIService.ConnectServer(strComputer, "root\\cimv2")
#colItems = objSWbemServices.ExecQuery("SELECT * FROM Win32_OperatingSystem")

#for objItem in colItems:
#   Descrição = {objItem.Description}

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
        'i3-3240': 2012,
        'i5-3470': 2012,
        'i5-4430': 2013,
        'i5-4590': 2014,
        'i5-7400': 2016,
        'i3-2120': 2012,
        'i5-9500': 2019,
        'i5-6500': 2016,
        'i5-4570': 2013,
        'i5-4430': 2014,
        'i3-7100': 2016,
        'i3-3212': 2013,
        'i5-5443': 2015,
        'i5-5740': 2015,
        'i3-540': 2010,

    

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



regional = "Nordeste"
marca = "wyden"
unidade = "UniFanor"
Office = "Office 2019"

def enviar_dados():        
    setor = setor_var.get()
             
    confirmation = messagebox.askyesno(
    "Confirmação",
    f"Você selecionou a regional: {regional}\n"
    f"Marca: {marca}\n"
    f"Unidade: {unidade}\n"
    f"Hostname: {hostname}\n"
    f"Username: {username}\n"
    f"Setor: {setor}\n"
    f"Tipo de Computador: {computer_type}\n"
    f"Dominio: {domain}\n"
    f"Versão do Windows: {versao}\n"
    f"Pacote Office: {Office}\n"
    f"Memória: {RAM}\n"
    f"fabricante: {manufacturer}\n"
    f"Modelo: {model}\n"
    f"SSD: {SSD}\n"
    f"CPU/GPU: {CPUG}\n"
    f"Anos: {Anos}\n"
    "Deseja enviar?"
)

    if confirmation:
        form_url = 'https://docs.google.com/forms/d/e/1FAIpQLSexKYmHwsLTfTGQjLu4c0eA_JZYdMPairLIr1tgzNVmCbaVVg/formResponse'
        form_data = {
            'entry.1962317397': regional,
            'entry.663803946': marca,
            'entry.586116077': unidade,
            'entry.2043695424': hostname,
            'entry.180468983': username,
            'entry.250274945': setor,
            'entry.1689058791': computer_type,
            'entry.305050396': domain,
            'entry.1598784526': versao,
            'entry.1631495942': Office,
            'entry.508585755': RAM,
            'entry.1995549497': manufacturer,
            'entry.809184448': model,
            'entry.9233005': SSD,
            'entry.1650346718': CPUG,
            'entry.186411303': Anos,
        }
        try:
            response = requests.post(form_url, data=form_data)
            response.raise_for_status()
            
            if response.status_code == 200:
                messagebox.showinfo("Sucesso", "Dados enviados com sucesso!")
            else:
                messagebox.showerror("Erro", f"Falha ao enviar os dados. Código de status: {response.status_code}")
        except requests.exceptions.RequestException as e:
            messagebox.showerror("Erro", f"Falha ao enviar os dados. Erro: {e}")
    else:
        messagebox.showinfo("Cancelado", "Envio cancelado.")

# Criação da interface gráfica
root = tk.Tk()
root.title("Formulário de Envio")

# Adicionando a imagem no cabeçalho
image = tk.PhotoImage(file="ydqus-estacio.png")  # Substitua "ydqus-estacio.png" pelo nome do arquivo da sua imagem
image_label = tk.Label(root, image=image)
image_label.grid(row=0, columnspan=3, pady=10)


tk.Label(root, text="Setor:").grid(row=3, column=0)
setor_var = tk.StringVar(root)
setor_var.set("Laboratório-01")  # valor padrão
setor_menu = tk.OptionMenu(root, setor_var, "Laboratório-Informática-01", "Laboratório-Informática-02", "Laboratório-Informática-03", "Laboratório-Informática-04", "Laboratório-Informática-05", "Laboratório-Informática-07")
setor_menu.grid(row=3, column=1)

tk.Button(root, text="Enviar", command=enviar_dados).grid(row=20, columnspan=3)

root.mainloop()
