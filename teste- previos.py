import socket
import getpass
import requests
import subprocess
import platform
import wmi
import win32com.client
import psutil as ps
import cpuinfo as cpu

system_info = platform.uname()


hostname = socket.gethostname()


username = getpass.getuser()


try:
    domain = subprocess.check_output('wmic computersystem get domain', shell=True).decode().split('\n')[1].strip()
except subprocess.CalledProcessError:
    domain = "N/A"
 


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


def get_office_package():
    try:
      
        word = win32com.client.Dispatch("Word.Application")
        version = word.Version
        word.Quit()

     
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


def get_computer_manufacturer():
    c = wmi.WMI()
    for system in c.Win32_ComputerSystem():
        return system.Manufacturer

manufacturer = get_computer_manufacturer()

def get_computer_model():
    c = wmi.WMI()
    for system in c.Win32_ComputerSystem():
        return system.Model

model = get_computer_model()

def get_ram_size():
    c = wmi.WMI()
    total_memory = 0
    for memory in c.Win32_PhysicalMemory():
        total_memory += int(memory.Capacity)
    total_memory_gb = total_memory / (1024 ** 3)  
    return total_memory_gb

ram_size_gb = get_ram_size()
RAM = (f"{ram_size_gb:.2f} GB RAM")

disk_usage = ps.disk_usage('/')
total_size = disk_usage.total // (1024 ** 3) 
SSD = (f" {total_size} GB")


info = cpu.get_cpu_info()
CPUG = (info['brand_raw'])

strComputer = "."
objWMIService = win32com.client.Dispatch("WbemScripting.SWbemLocator")
objSWbemServices = objWMIService.ConnectServer(strComputer, "root\\cimv2")
colItems = objSWbemServices.ExecQuery("SELECT * FROM Win32_OperatingSystem")

for objItem in colItems:
    Descrição = {objItem.Description}



from datetime import datetime

def get_computer_age():
    c = wmi.WMI()
    for system in c.Win32_BIOS():
        manufacture_date = system.ReleaseDate.split('.')[0][:8]  
        manufacture_date = datetime.strptime(manufacture_date, '%Y%m%d')
        current_date = datetime.now()
        age = current_date.year - manufacture_date.year - ((current_date.month, current_date.day) < (manufacture_date.month, manufacture_date.day))
        return age

computer_age = get_computer_age()
Anos = (f" {computer_age} anos")

Regional = "Nordeste"
Marca = "Wydem"
Unidade = "UniFanor"



# URL do formulário e dados a serem enviados
form_url = "https://docs.google.com/forms/d/e/1FAIpQLSexKYmHwsLTfTGQjLu4c0eA_JZYdMPairLIr1tgzNVmCbaVVg/formResponse"
form_data = {
    "entry.586116077": Regional,
    "entry.1962317397": Marca,
    "entry.663803946": Unidade,
    "entry.2043695424": hostname,  
    "entry.180468983": username,   
    "entry.305050396": domain,  
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

try:
    # Enviar os dados para o formulário
    response = requests.post(form_url, data=form_data)

    # Verificar se a submissão foi bem-sucedida
    if response.status_code == 200 or response.status_code == 302:
        print("Forms enviados com sucesso!")
    else:
        print(f"Falha ao enviar o hostname, username e domínio. Status code: {response.status_code}")
except Exception as e:
    print(f"Ocorreu um erro ao enviar os dados: {e}")





input('Inventario realizado, com sucesso!')


