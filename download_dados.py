import os
import requests
import zipfile

folder = 'dados_cvm'

if os.path.exists(os.getcwd() + f'\\{folder}'):
        print(f'\nA pasta {folder} já existe')

else:
        # creating 'dados_cvm' folder
    print(f'\nCriando a pasta {folder}...\n')
    os.makedirs(folder)
    os.chdir(os.getcwd() + f'\\{folder}')
    
    anos = range(2010, 2024)
    url = 'https://dados.cvm.gov.br/dados/CIA_ABERTA/DOC/DFP/DADOS/'
    
    print('Baixando dados...\n')
    
    # downloading data
    for ano in anos:
        download = requests.get(url + f'dfp_cia_aberta_{ano}.zip')
        open(f'dfp_cia_aberta_{ano}.zip', 'wb').write(download.content)
        print(f'Finished downloading dfp_cia_aberta_{ano}.zip')
    
    print('\nDownload finalizado')

