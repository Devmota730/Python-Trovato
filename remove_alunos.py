import os
import re
import shutil
import ctypes
import sys

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def delete_numeric_users(user_directory):
    try:
        # Lista todos os diretórios no diretório de usuários
        users = os.listdir(user_directory)
        print(f"Usuários encontrados: {users}")
        
        # Expressão regular para corresponder a diretórios com nomes numéricos
        numeric_pattern = re.compile(r'^\d+$')
        
        for user in users:
            user_path = os.path.join(user_directory, user)
            print(f"Verificando usuário: {user}")
            
            # Verifica se o nome do diretório é numérico e se é um diretório
            if numeric_pattern.match(user):
                print(f"Usuário {user} é numérico.")
                if os.path.isdir(user_path):
                    try:
                        # Deleta o diretório do usuário
                        shutil.rmtree(user_path, ignore_errors=True)
                        print(f"Deleted user directory: {user_path}")
                    except Exception as e:
                        print(f"Failed to delete {user_path}: {e}")
                else:
                    print(f"{user_path} não é um diretório.")
            else:
                print(f"Usuário {user} não é numérico.")
    except Exception as e:
        print(f"Erro ao acessar o diretório de usuários: {e}")

if is_admin():
    # Define o caminho do diretório de usuários
    user_directory = r"C:\Users"

    # Chama a função para deletar diretórios de usuários numéricos
    delete_numeric_users(user_directory)

    # Pausa para manter a janela aberta
    input("Pressione Enter para sair...")
else:
    # Reexecuta o script como administrador
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
