import os
import gdown

def download_file_from_google_drive(file_id, destination):
    URL = f"https://drive.google.com/uc?export=download&id={file_id}"
    gdown.download(URL, destination, quiet=False)

def compare_versions(local_version, remote_version):
    local_version_number = local_version.split('_')[1]
    remote_version_number = remote_version.split('_')[1]
    return float(remote_version_number) > float(local_version_number)

# IDs e caminhos dos arquivos
file_id = '1qw_vl5HbmjUhTV03NoNuS7qsmsWxDNMG'
local_file_path = r'C:\\Users\\leonardo.mota\\Music\\Teste-forms\\Invetario_2.0_Suporte.py'
downloaded_file_path = r'C:\\Inventario_Dunas\\Invetario_2.1_Suporte.py'  # Novo local para baixar o arquivo

# Criar o diretório se não existir
os.makedirs(os.path.dirname(downloaded_file_path), exist_ok=True)

# Baixar o arquivo do Google Drive
download_file_from_google_drive(file_id, downloaded_file_path)

# Verificar se o arquivo baixado é um HTML
with open(downloaded_file_path, 'r') as f:
    first_line = f.readline()
    if '<html' in first_line:
        print("Erro: O arquivo baixado é um HTML. Verifique o link do Google Drive.")
        f.close()
        os.remove(downloaded_file_path)
    else:
        f.close()  # Fechar o arquivo antes de qualquer operação
        # Comparar as versões dos arquivos e substituir se a versão remota for mais recente
        local_file_name = os.path.basename(local_file_path)
        downloaded_file_name = os.path.basename(downloaded_file_path)

        if compare_versions(local_file_name, downloaded_file_name):
            os.replace(downloaded_file_path, local_file_path)
            print(f"O arquivo {local_file_path} foi substituído pela versão atualizada do Google Drive.")
            # Mover o arquivo baixado para o diretório desejado
            new_local_file_path = os.path.join(r'C:\\Inventario_Dunas', downloaded_file_name)
            os.rename(local_file_path, new_local_file_path)
            print(f"O arquivo foi movido para {new_local_file_path}.")
        else:
            os.remove(downloaded_file_path)
            print(f"O arquivo {local_file_path} já está atualizado.")
