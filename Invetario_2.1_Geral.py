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
print(f"Computer Type: {computer_type}")




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
print(office_package)

# pega a informação do fabricante
def get_computer_manufacturer():
    c = wmi.WMI()
    for system in c.Win32_ComputerSystem():
        return system.Manufacturer

manufacturer = get_computer_manufacturer()
print(f"Manufacturer: {manufacturer}")


# pega informação do modelo 
def get_computer_model():
    c = wmi.WMI()
    for system in c.Win32_ComputerSystem():
        return system.Model

model = get_computer_model()
print(f"Model: {model}")

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
from datetime import datetime
def get_computer_age():
    c = wmi.WMI()
    for system in c.Win32_BIOS():
        manufacture_date = system.ReleaseDate.split('.')[0][:8]  # Garantir que a data esteja no formato correto
        manufacture_date = datetime.strptime(manufacture_date, '%Y%m%d')
        current_date = datetime.now()
        age = current_date.year - manufacture_date.year - ((current_date.month, current_date.day) < (manufacture_date.month, manufacture_date.day))
        return age
computer_age = get_computer_age()
Anos = (f" {computer_age} anos")


#interface 
def submit_form():
    regional_code = regional_var.get()
    marca_code = marca_var.get()
    unidade = combo.get()
    hostname = socket.gethostname()
    
    if regional_code not in ['1', '2', '3', '4']:
        messagebox.showerror("Erro", "Código de regional inválido. Selecione 1 para Nordeste, 2 para Sudeste, 3 para Centro-Oeste ou 4 para Norte.")
        return
    
    if marca_code not in ['1', '2', '3', '4', '5', '6', '7']:
        messagebox.showerror("Erro", "Código de marca inválido. Selecione 1 para Estacio, 2 para Wyden, 3 para Damasio, 4 para Idomed, 5 para Athenas, 6 para Yduqs corporativo ou 7 para Ibmec.")
        return
    
    regional_dict = {
        '1': "Nordeste",
        '2': "Sudeste",
        '3': "Centro-Oeste",
        '4': "Norte"
    }
    
    marca_dict = {
        '1': "Estacio",
        '2': "Wyden",
        '3': "Damasio",
        '4': "Idomed",
        '5': "Athenas",
        '6': "Yduqs corporativo",
        '7': "Ibmec"
    }
    
    regional = regional_dict[regional_code]
    marca = marca_dict[marca_code]
    
    #confirmation = messagebox.askyesno("Confirmação", f"Você selecionou a regional: {regional}\n\nMarca: {marca}\n\nUnidade: {unidade}\nHostname: {hostname}\nDeseja enviar?")


    confirmation = messagebox.askyesno(
    "Confirmação",
    f"Você selecionou a regional: {regional}\n"
    f"Marca: {marca}\n"
    f"Setor: {Setor}\n"
    f"Local: {Local}\n"
    f"Unidade: {unidade}\n"
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
        form_url = 'https://docs.google.com/forms/d/e/1FAIpQLSexKYmHwsLTfTGQjLu4c0eA_JZYdMPairLIr1tgzNVmCbaVVg/formResponse'
        form_data = {
            'entry.1962317397': regional,
            'entry.0987654321': hostname,
            'entry.663803946': marca,
            'entry.0987654321': Setor,
            'entry.663803946': Local,
            'entry.586116077': unidade,
            'entry.2043695424': hostname,
            'entry.180468983': username,
            'entry.305050396': domain,
            'entry.1598784526': versao,
            'entry.1689058791': computer_type,
            'entry.1631495942': office_package,
            'entry.1995549497': manufacturer,
            'entry.809184448': model,
            'entry.508585755': RAM,
            'entry.9233005': SSD,
            'entry.1650346718': CPUG,
            'entry.250274945': Descrição,
            'entry.186411303': Anos

        }
        try:
            response = requests.post(form_url, data=form_data)
            response.raise_for_status()  # Levanta um erro para códigos de status HTTP 4xx/5xx
            
            if response.status_code == 200:
                messagebox.showinfo("Sucesso", "Dados enviados com sucesso!")
            else:
                messagebox.showerror("Erro", f"Falha ao enviar os dados. Código de status: {response.status_code}")
        except requests.exceptions.RequestException as e:
            messagebox.showerror("Erro", f"Falha ao enviar os dados. Erro: {e}")
    else:
        messagebox.showinfo("Cancelado", "Envio cancelado.")

import tkinter as tk
from tkinter import ttk
import requests


# Configuração da interface gráfica
root = tk.Tk()
root.title("Formulário de Regional, Marca e Unidade")

# Carregar a imagem
image = tk.PhotoImage(file="ydqus-estacio.png")  # Substitua "sua_imagem.png" pelo nome do arquivo da sua imagem

# Exibir a imagem
image_label = tk.Label(root, image=image)
image_label.pack(pady=10)

label_regional = tk.Label(root, text="Selecione a sua regional:")
label_regional.pack(pady=10)

regional_var = tk.StringVar(value='0')

radio_nordeste = tk.Radiobutton(root, text="Nordeste", variable=regional_var, value='1')
radio_nordeste.pack(pady=5)

radio_sudeste = tk.Radiobutton(root, text="Sudeste", variable=regional_var, value='2')
radio_sudeste.pack(pady=5)

radio_centro_oeste = tk.Radiobutton(root, text="Centro-Oeste", variable=regional_var, value='3')
radio_centro_oeste.pack(pady=5)

radio_norte = tk.Radiobutton(root, text="Norte", variable=regional_var, value='4')
radio_norte.pack(pady=5)

label_marca = tk.Label(root, text="Selecione a sua marca:")
label_marca.pack(pady=10)

marca_var = tk.StringVar(value='0')

radio_estacio = tk.Radiobutton(root, text="Estacio", variable=marca_var, value='1')
radio_estacio.pack(pady=5)

radio_wyden = tk.Radiobutton(root, text="Wyden", variable=marca_var, value='2')
radio_wyden.pack(pady=5)

radio_damasio = tk.Radiobutton(root, text="Damasio", variable=marca_var, value='3')
radio_damasio.pack(pady=5)

radio_idomed = tk.Radiobutton(root, text="Idomed", variable=marca_var, value='4')
radio_idomed.pack(pady=5)

radio_athenas = tk.Radiobutton(root, text="Athenas", variable=marca_var, value='5')
radio_athenas.pack(pady=5)

radio_yduqs_corporativo = tk.Radiobutton(root, text="Yduqs corporativo", variable=marca_var, value='6')
radio_yduqs_corporativo.pack(pady=5)

radio_ibmec = tk.Radiobutton(root, text="Ibmec", variable=marca_var, value='7')
radio_ibmec.pack(pady=5)

label_unidade = tk.Label(root, text="Selecione a sua unidade:")
label_unidade.pack(pady=10)

# Substitua estas opções pelas suas 20 opções
opcoes = ["UniFanor", "UniFanor-BM", "Via Coprs", "Estacio-parangaba", "Feira-Santana", "Estacio_Venezuela", "Iguatu", "Estacio-Centro", "UniFBV", "Facip"
           ]

combo = ttk.Combobox(root, values=opcoes)
combo.pack(pady=5)

submit_button = tk.Button(root, text="Enviar", command=submit_form)
submit_button.pack(pady=20)

root.mainloop()