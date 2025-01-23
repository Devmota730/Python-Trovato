import os
import cpuinfo as cpu
import platform as p
import psutil as ps
import wmi as w
import pywin32_system32 
import win32com
import win32com.client




print()

print()


disk_usage = ps.disk_usage('/')
total_size = disk_usage.total / (1024 ** 3) 

print()


import platform
import win32com

system_info = platform.uname()
print('Hostname',os.environ.get('computername'))
print('usuario', os.environ.get('username'))
print(f"System: {system_info.system}")
print(f"Node Name: {system_info.node}")
print(f"Version: {system_info.version}")
print(f"Machine: {system_info.machine}")

memory_info = ps.virtual_memory()
print(f"Total RAM: {memory_info.total / (1024 ** 3):.2f} GB")

print('SSD',total_size)

info = cpu.get_cpu_info()
print('Versão do processador',info['brand_raw'])


strComputer = "."
objWMIService = win32com.client.Dispatch("WbemScripting.SWbemLocator")
objSWbemServices = objWMIService.ConnectServer(strComputer, "root\\cimv2")
colItems = objSWbemServices.ExecQuery("SELECT * FROM Win32_OperatingSystem")

for objItem in colItems:
    print(f"Description: {objItem.Description}")


import wmi

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


import win32com.client

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


def get_computer_manufacturer():
    c = wmi.WMI()
    for system in c.Win32_ComputerSystem():
        return system.Manufacturer

manufacturer = get_computer_manufacturer()
print(f"Manufacturer: {manufacturer}")



def get_computer_model():
    c = wmi.WMI()
    for system in c.Win32_ComputerSystem():
        return system.Model

model = get_computer_model()
print(f"Model: {model}")

print('teste CPU')

info = cpu.get_cpu_info()
print('Versão do processador',info['brand_raw'])


print('teste ano ')

import wmi
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
print(f"Idade do equipamento: {computer_age} anos")

print('teste HD ')
import wmi

def get_hd_size():
    c = wmi.WMI()
    total_size = 0
    for disk in c.Win32_DiskDrive():
        total_size += int(disk.Size)
    total_size_gb = total_size // (1024 ** 3)  # Converter bytes para gigabytes e arredondar para baixo
    return total_size_gb

hd_size_gb = get_hd_size()
print(f"Tamanho do HD: {hd_size_gb} GB")








