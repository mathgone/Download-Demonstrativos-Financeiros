from tkinter import messagebox
import os
import zipfile
import sys

try:
    import requests
except ImportError:
    messagebox.showinfo('Módulos não encontrados', "Clique no botão 'Verificar Bibliotecas para instalar os módulos necessários'", icon='warning')
    sys.exit()

folder = 'dados_cvm_itr'

if os.path.exists(os.getcwd() + f'\\{folder}'):
    messagebox.showinfo("ERRO", f'A pasta {folder} já foi criada')

else:
    # criando a pasta 'dados_cvm_itr'
    os.makedirs(folder)
    os.chdir(os.getcwd() + f'\\{folder}')
    
    anos = range(2011, 2024)
    url = 'https://dados.cvm.gov.br/dados/CIA_ABERTA/DOC/ITR/DADOS/'
        
    # baixando dados
    for ano in anos:
        download = requests.get(url + f'itr_cia_aberta_{ano}.zip')
        open(f'itr_cia_aberta_{ano}.zip', 'wb').write(download.content)
        print(f'Download do arquivo itr_cia_aberta_{ano}.zip finalizado.')
    
    messagebox.showinfo(f'Pasta {folder} criada', "Os dados trimestrais da CVM foram baixados com sucesso")