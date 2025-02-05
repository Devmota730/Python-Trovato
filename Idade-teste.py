import subprocess
import re
from datetime import datetime

def get_processor_info():
    # Executa o comando para obter informações do processador
    result = subprocess.run(['wmic', 'cpu', 'get', 'name'], stdout=subprocess.PIPE)
    # Decodifica o resultado para obter o nome do processador
    processor_info = result.stdout.decode().strip().split('\n')[1]
    return processor_info

def extract_processor_model(processor_info):
    # Extrai a parte relevante do nome do processador (ex: i7-7700)
    match = re.search(r'i\d-\d{4}', processor_info)
    if match:
        return match.group()
    return None

def calculate_age(processor_model):
    current_year = datetime.now().year
    # Dicionário com os anos de lançamento dos processadores
    release_years = {
        'i7-7700': 2017,
        'i7-1165': 2022,
        'i5-1165': 2022,
        'i7-6600': 2016,
        'i5-1135': 2021,
        'i7-8550': 2017,
        'i7-8565': 2018,
        'i5-1021': 2019,
        'i7-1021': 2019,
        'i5-7200': 2016,
        'i5-4300': 2013,
        'i7-4600': 2013,
        'i5-4600': 2013,
        'i5-3337': 2012,
        'i5-5300': 2015,
        'i3-2120': 2012,
        'i9-1390': 2023,
        'i5-3320': 2013,
        'i3-4005': 2013,
        
        

        
        
        # Adicione outros modelos e seus anos de lançamento conforme necessário
    }
    
    if processor_model in release_years:
        release_year = release_years[processor_model]
        age = current_year - release_year
        return age
    return None

processor_info = get_processor_info()
processor_model = extract_processor_model(processor_info)

if processor_model:
    age = calculate_age(processor_model)
    if age is not None:
        print(f"A idade do seu computador com base no modelo do processador ({processor_model}) é: {age} anos.")
    else:
        print("Não foi possível determinar a idade do processador.")
else:
    print("Não foi possível extrair o modelo do processador.")
