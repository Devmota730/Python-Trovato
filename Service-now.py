from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time

def download_video(video_url, output_path):
    # Configurar o driver do navegador
    driver = webdriver.Chrome(ChromeDriverManager().install())
    
    try:
        # Abrir a página do vídeo
        driver.get(video_url)
        
        # Aguarde o carregamento da página e encontre o botão de download
        time.sleep(5)  # Ajuste o tempo conforme necessário
        download_button = driver.find_element(By.XPATH, '//*[@id="download-button-xpath"]')  # Substitua pelo XPath correto
        
        # Clique no botão de download
        download_button.click()
        
        # Aguarde o download ser concluído
        time.sleep(10)  # Ajuste o tempo conforme necessário
        
        print(f"Vídeo baixado com sucesso e salvo em {output_path}")
    except Exception as e:
        print(f"Erro ao baixar o vídeo: {e}")
    finally:
        driver.quit()

# URL do vídeo a ser baixado
video_url = 'https://ead1.cursobeta.com.br/aula/assistir/13507'

# Caminho onde o vídeo será salvo
output_path = 'C:\\Users\\leonardo.mota\\Music\\Videos\\video_baixado.mp4'

# Baixar o vídeo
download_video(video_url, output_path)
