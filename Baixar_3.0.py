
import os 
import gdown 

caminhoCompleto = os.path.join(os.getcwd())

print(caminhoCompleto)

caminhoCompleto = os.mkdir('Inventario_Dunas')

caminhoCompleto = os.chdir('Inventario_Dunas')

#caminhoCompleto = os.getcwd()

def download_file_from_google_drive(file_id, destination):
    URL = f"https://drive.google.com/uc?export=download&id={file_id}"
    gdown.download(URL, destination, quiet=False)

# IDs dos arquivos e nomes de destino
files = {
    '10vyxu49E_ktRowbxVNom4MKU7Zo_6xIw': 'Inventario_sala.py',
    '1qw_vl5HbmjUhTV03NoNuS7qsmsWxDNMG': 'Inventario_Lab.py',
    '1oPbznsaSwKQzLe6pPtshD82Hyi2cOBAP': 'ydqus-estacio.png',
    '1Jl6RleFENQLnefObcESp9PhRMhSuF74g': 'Biblioteca.bat',
    '1K7j129DB0UOqMXgvF9rr22NG0d13cI3P': 'Inventario_Suporte_2.4.py',
    '1Dgu7gP9gkTH8U-GNQuI1egGNA9A_aoGb': 'python-3.13.1-amd64.exe'
}

destination_dir = r''

#destination_dir = r'C:\\Inventario_Dunas'

# Criar o diretório se não existir
os.makedirs(destination_dir, exist_ok=True)

# Baixar cada arquivo do Google Drive
for file_id, file_name in files.items():
    destination_path = os.path.join(destination_dir, file_name)
    download_file_from_google_drive(file_id, destination_path)

print("Todos os arquivos foram baixados com sucesso para o diretório C:\\Inventario_Dunas.")


