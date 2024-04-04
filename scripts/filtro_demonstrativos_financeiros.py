import zipfile
import os
import sys
import pandas as pd
from tkinter import filedialog
from time import sleep

# PARAMETERS AND VARIABLES

# funciton to get the year of the current iteration
def get_year(file):
    file = file.split('_')[3].split('.')[0]
    return file
    
dataframes = {}
dataframe = {}

cia_code = int(sys.argv[1])
year = int(sys.argv[2])

relevant_data = ['BPA', 'BPP', 'DFC_MI', 'DRE']
columns = ['DENOM_CIA', 'CD_CVM', 'ORDEM_EXERC','DT_FIM_EXERC', 'CD_CONTA', 'DS_CONTA', 'VL_CONTA']
columns_cia_codes = ['DENOM_CIA', 'CD_CVM']

path = os.getcwd() + '\\dados_cvm'

# READING THE ZIP FILES AND CREATING THE DATAFRAME
print('\nExtraindo dados...\n')
for filename in os.listdir(path):
    with zipfile.ZipFile(path + f'\\{filename}', 'r') as zipf:
            for relevant in relevant_data:
                with zipf.open(f'dfp_cia_aberta_{relevant}_con_{get_year(filename)}.csv') as csv_file:
                    print(csv_file)
                    df = pd.read_csv(csv_file, sep=';', encoding='ISO-8859-1', dtype={"ORDEM_EXERC": "category"}, usecols=columns)
    
                df_name = f'df_{relevant}_{get_year(filename)}'
                dataframes[df_name] = df

# GETTING THE COMPANY NAME
for filename in os.listdir(path):
    with zipfile.ZipFile(path + f'\\{filename}', 'r') as zipf:
            with zipf.open(f'dfp_cia_aberta_{get_year(filename)}.csv') as csv_file:
                df_cia_codes = pd.read_csv(csv_file, sep=';', encoding='ISO-8859-1', dtype={"ORDEM_EXERC": "category"}, usecols=columns_cia_codes)
                cia_name = df_cia_codes[df_cia_codes['CD_CVM'] == cia_code]['DENOM_CIA'].iloc[0]

# ITERATING THROUGH THE DATAFRAME, GATHERING DATA AND CREATING A .XLSX FILE
for relevant in relevant_data:
    df = dataframes[f'df_{relevant}_{year}']
    
    df_specific_cia = df[df['CD_CVM'] == cia_code]

    df_name = f'df_{relevant}_final'
    
    df_final = df_specific_cia.pivot(index=['DENOM_CIA', 'CD_CVM', 'CD_CONTA', 'DS_CONTA'], columns='ORDEM_EXERC', values='VL_CONTA').reset_index()
    df_final.rename(columns={'ÚLTIMO': f'Último Exercício({year})', 'PENÚLTIMO': f'Penúltimo Exercício ({year - 1})'}, inplace=True)
    # to remove null data, uncomment below
    #df_final = df_final[(df_final[f'Último Exercício({year})'] != 0) | (df_final[f'Penúltimo Exercício ({year - 1})'] != 0)]

    df_name = f'df_{relevant}_{year}'
    dataframe[df_name] = df_final

# creating .XLSX file
print('\nGerando Excel...')
sleep(1.5)
output_path = filedialog.asksaveasfilename(defaultextension='.xlsx', filetypes=[("Excel files", "*.xlsx")], initialfile=f'{cia_name} - {year}')
if output_path:
    with pd.ExcelWriter(output_path) as writer:
        dataframe[f'df_BPA_{year}'].to_excel(writer, sheet_name="Balanço Patrimonial Ativo", index=False)
        dataframe[f'df_BPP_{year}'].to_excel(writer, sheet_name="Balanço Patrimonial Passivo", index=False)
        dataframe[f'df_DFC_MI_{year}'].to_excel(writer, sheet_name="Demonstração do Resultado", index=False)
        dataframe[f'df_DRE_{year}'].to_excel(writer, sheet_name="Demonstração do Fluxo de Caixa", index=False)

    print('\nArquivo salvo!')
else:
    print('\n*****Operação cancelada*****')