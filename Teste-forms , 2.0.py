import tkinter as tk
from tkinter import messagebox
import socket
import requests

def submit_form():
    regional_code = regional_var.get()
    marca_code = marca_var.get()
    unidade = unidade_entry.get()
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
    
    confirmation = messagebox.askyesno("Confirmação", f"Você selecionou a regional: {regional}\nMarca: {marca}\nUnidade: {unidade}\nHostname: {hostname}\nDeseja enviar?")
    
    if confirmation:
        form_url = 'https://docs.google.com/forms/d/e/1FAIpQLSevt4DU6rqJJjO-gLOroSGBXh-eBDOoMa453SPle363Rxnneg/formResponse'
        form_data = {
            'entry.1234567890': regional,  # Substitua 'entry.1234567890' pelo ID do campo da pergunta "Regional"
            'entry.0987654321': hostname,  # Substitua 'entry.0987654321' pelo ID do campo do hostname
            'entry.1122334455': marca,     # Substitua 'entry.1122334455' pelo ID do campo da pergunta "Marca"
            'entry.5566778899': unidade    # Substitua 'entry.5566778899' pelo ID do campo da pergunta "Unidade"
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

label_unidade = tk.Label(root, text="Digite a sua unidade:")
label_unidade.pack(pady=10)

unidade_entry = tk.Entry(root)
unidade_entry.pack(pady=5)

submit_button = tk.Button(root, text="Enviar", command=submit_form)
submit_button.pack(pady=20)

root.mainloop()
