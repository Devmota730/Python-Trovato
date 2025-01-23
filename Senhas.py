import tkinter as tk
from tkinter import simpledialog, messagebox
import json
import os

# Arquivo para armazenar as senhas
PASSWORD_FILE = "passwords.json"

# Carregar senhas do arquivo
def load_passwords():
    if os.path.exists(PASSWORD_FILE):
        with open(PASSWORD_FILE, "r") as file:
            return json.load(file)
    return {}

# Salvar senhas no arquivo
def save_passwords(passwords):
    with open(PASSWORD_FILE, "w") as file:
        json.dump(passwords, file)

# Adicionar uma nova senha
def add_password():
    description = simpledialog.askstring("Input", "Digite a descrição:")
    password = simpledialog.askstring("Input", "Digite a senha:", show='*')
    if description and password:
        passwords[description] = password
        save_passwords(passwords)
        messagebox.showinfo("Sucesso", "Senha salva com sucesso!")

# Recuperar uma senha
def retrieve_password():
    description = simpledialog.askstring("Input", "Digite a descrição:")
    if description in passwords:
        messagebox.showinfo("Senha", f"A senha para '{description}' é: {passwords[description]}")
    else:
        messagebox.showerror("Erro", "Nenhuma senha encontrada para essa descrição.")

# Criar a janela principal da aplicação
root = tk.Tk()
root.title("Gerenciador de Senhas")

# Carregar senhas existentes
passwords = load_passwords()

# Criar botões para adicionar e recuperar senhas
add_button = tk.Button(root, text="Adicionar Senha", command=add_password)
add_button.pack(pady=10)

retrieve_button = tk.Button(root, text="Consultar Senha", command=retrieve_password)
retrieve_button.pack(pady=10)

# Executar a aplicação
root.mainloop()
