import os
import requests
import zipfile
import datetime

# creating 'dados' folder
folder = 'dados_cvm'
os.makedirs(folder)
os.chdir(os.getcwd() + f'\\{folder}')

ano_atual = datetime.datetime.now().year
anos = range(2010, ano_atual)
url = 'https://dados.cvm.gov.br/dados/CIA_ABERTA/DOC/DFP/DADOS/'

# downloading data
for ano in anos:
    download = requests.get(url + f'dfp_cia_aberta_{ano}.zip')
    open(f'dfp_cia_aberta_{ano}.zip', 'wb').write(download.content)
