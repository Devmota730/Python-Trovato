import tkinter as tk
from tkinter import messagebox
import socket
import requests

def submit_form():
    regional_code = regional_var.get()
    hostname = socket.gethostname()
    
    if regional_code not in ['1', '2', '3', '4']:
        messagebox.showerror("Erro", "Código inválido. Selecione 1 para Nordeste, 2 para Sudeste, 3 para Centro-Oeste ou 4 para Norte.")
        return
    
    regional_dict = {
        '1': "Nordeste",
        '2': "Sudeste",
        '3': "Centro-Oeste",
        '4': "Norte"
    }
    
    regional = regional_dict[regional_code]
    
    confirmation = messagebox.askyesno("Confirmação", f"Você selecionou a regional: {regional}\nHostname: {hostname}\nDeseja enviar?")
    
    if confirmation:
        form_url = 'https://docs.google.com/forms/d/e/1FAIpQLSevt4DU6rqJJjO-gLOroSGBXh-eBDOoMa453SPle363Rxnneg/formResponse'
        form_data = {
            'entry.1754849344': regional,  # Substitua 'entry.1234567890' pelo ID do campo da pergunta "Regional"
            'entry.1411100373': hostname   # Substitua 'entry.0987654321' pelo ID do campo do hostname
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
root.title("Formulário de Regional")

label = tk.Label(root, text="Selecione a sua regional:")
label.pack(pady=10)

regional_var = tk.StringVar(value='0')

radio_nordeste = tk.Radiobutton(root, text="Nordeste", variable=regional_var, value='1')
radio_nordeste.pack(pady=5)

radio_sudeste = tk.Radiobutton(root, text="Sudeste", variable=regional_var, value='2')
radio_sudeste.pack(pady=5)

radio_centro_oeste = tk.Radiobutton(root, text="Centro-Oeste", variable=regional_var, value='3')
radio_centro_oeste.pack(pady=5)

radio_norte = tk.Radiobutton(root, text="Norte", variable=regional_var, value='4')
radio_norte.pack(pady=5)

submit_button = tk.Button(root, text="Enviar", command=submit_form)
submit_button.pack(pady=20)

root.mainloop()
