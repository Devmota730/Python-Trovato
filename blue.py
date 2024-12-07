import win32com.client

def toggle_bluetooth(state):
    bt_manager = win32com.client.Dispatch("WbemScripting.SWbemLocator")
    bt_service = bt_manager.ConnectServer(".", "root\\cimv2")
    bt_adapter = bt_service.ExecQuery("SELECT * FROM Win32_NetworkAdapter WHERE Name LIKE '%Bluetooth%'")

    for adapter in bt_adapter:
        if state == "on":
            adapter.Enable()
            print("Bluetooth ligado")
        elif state == "off":
            adapter.Disable()
            print("Bluetooth desligado")
        else:
            print("Estado inválido. Use 'on' ou 'off'.")

# Desligar o Bluetooth
toggle_bluetooth("off")

# Ligar o Bluetooth
toggle_bluetooth("on")
