import tkinter as tk
from tkinter import ttk, messagebox
import requests
import socket

# Função para enviar o formulário
def submit_form():
    regional_name = regional_var.get()
    marca_name = marca_var.get()
    unidade = unidade_var.get()
    hostname = socket.gethostname()
    
    regional_dict = {
        "Nordeste": '1',
        "Sudeste": '2',
        "Centro-Oeste": '3',
        "Norte": '4'
    }
    
    marca_dict = {
        "Estacio": '1',
        "Wyden": '2',
        "Damasio": '3',
        "Idomed": '4',
        "Athenas": '5',
        "Yduqs corporativo": '6',
        "Ibmec": '7'
    }
    
    regional_code = regional_dict.get(regional_name)
    marca_code = marca_dict.get(marca_name)
    
    if regional_code not in ['1', '2', '3', '4']:
        messagebox.showerror("Erro", "Código de regional inválido. Selecione uma opção válida.")
        return
    
    if marca_code not in ['1', '2', '3', '4', '5', '6', '7']:
        messagebox.showerror("Erro", "Código de marca inválido. Selecione uma opção válida.")
        return
    
    regional = regional_name
    marca = marca_name
    
    # Verifique se todas as variáveis estão definidas
    try:
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
    except NameError as e:
        messagebox.showerror("Erro", f"Variável não definida: {e}")
        return
    
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

regional_var = tk.StringVar(root)
regional_var.set("Nordeste")  # valor padrão
regional_menu = tk.OptionMenu(root, regional_var, "Nordeste", "Sudeste", "Centro-Oeste", "Norte")
regional_menu.pack(pady=5)

label_marca = tk.Label(root, text="Selecione a sua marca:")
label_marca.pack(pady=10)

marca_var = tk.StringVar(root)
marca_var.set("Estacio")  # valor padrão
marca_menu = tk.OptionMenu(root, marca_var, "Estacio", "Wyden", "Damasio", "Idomed", "Athenas", "Yduqs corporativo", "Ibmec")
marca_menu.pack(pady=5)

label_unidade = tk.Label(root, text="Digite a sua unidade:")
label_unidade.pack(pady=10)

unidade_var = tk.StringVar()
unidade_entry = tk.Entry(root, textvariable=unidade_var)
unidade_entry.pack(pady=5)

submit_button = tk.Button(root, text="Enviar", command=submit_form)
submit_button.pack(pady=20)

root.mainloop()
