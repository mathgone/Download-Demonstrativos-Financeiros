from tkinter import messagebox, filedialog
import zipfile
import os
import sys

try:
    import pandas as pd
except ImportError:
    messagebox.showinfo('Módulos não encontrados', "Clique no botão 'Verificar Bibliotecas' para instalar os módulos necessários", icon='warning')
    sys.exit()

# -------------------------------------------- PARÂMETROS -------------------------------------------- #

try:
    # INPUTS DO USUÁRIO DA INTERFACE
    cia_code = int(sys.argv[1])
    
    anos = [ano for ano in range(2011, 2024)]
    year = int(sys.argv[2])
    if year not in anos:
        messagebox.showinfo('Entrada inválida', 'Digite um ano válido (2011 a 2023)', icon='warning')
        sys.exit()
    
    columns_1t = ['DENOM_CIA', 'CD_CVM', 'DT_FIM_EXERC', 'CD_CONTA', 'DS_CONTA', 'VL_CONTA']
    colunas_geral = ['DT_FIM_EXERC', 'CD_CONTA', 'DS_CONTA', 'VL_CONTA']
    
    new_columns_1t = {'DENOM_CIA': 'Empresa', 
                      'CD_CVM': 'Código CVM', 
                      'DT_FIM_EXERC': '1T',
                      'CD_CONTA': 'Conta', 
                      'DS_CONTA': 'Descrição', 
                      'VL_CONTA': 'Valor'}
    
    new_columns_2t = { 'DT_FIM_EXERC': '2T', 
                      'CD_CONTA': 'Conta', 
                      'DS_CONTA': 'Descrição', 
                      'VL_CONTA': 'Valor'}
    
    new_columns_3t = { 'DT_FIM_EXERC': '3T', 
                      'CD_CONTA': 'Conta', 
                      'DS_CONTA': 'Descrição', 
                      'VL_CONTA': 'Valor'}
    
    new_columns_dfp = { 'DT_FIM_EXERC': 'DFP', 
                      'CD_CONTA': 'Conta', 
                      'DS_CONTA': 'Descrição', 
                      'VL_CONTA': 'Valor'}
    
    relevant_data = ['BPA', 'BPP', 'DFC_MI', 'DRE'] # AJUSTE DE ACORDO COM OS DADOS DA CVM A SEREM LIDOS (CONSOLIDADOS)
    columns = ['DENOM_CIA', 'CD_CVM', 'ORDEM_EXERC', 'DT_FIM_EXERC', 'CD_CONTA', 'DS_CONTA', 'VL_CONTA'] # COLUNAS RELEVANTES
    periods = ['1T', '2T', '3T', 'DFP'] # 1º TRIMESTRE, 2º TRIMESTRE, 3º TRIMESTRE, DEMONSTATIVO FINANCEIRO PADRONIZADO
    dt_fim_exerc = [f'{year}-03-31', f'{year}-06-30', f'{year}-09-30', f'{year}-12-31']
    
    # -------------------------------------------- FUNÇÕES -------------------------------------------- #
    
    def process_dataframe(category):
        new_df_1t = data[category]['1T'].reset_index(drop=True)[columns_1t]
        new_df_1t = new_df_1t.rename(columns=new_columns_1t)
        
        new_df_2t = data[category]['2T'].reset_index(drop=True)[colunas_geral]
        new_df_2t = new_df_2t.rename(columns=new_columns_2t)
        
        new_df_3t = data[category]['3T'].reset_index(drop=True)[colunas_geral]
        new_df_3t = new_df_3t.rename(columns=new_columns_3t)
        
        new_df_dfp = data[category]['DFP'].reset_index(drop=True)[colunas_geral]
        new_df_dfp = new_df_dfp.rename(columns=new_columns_dfp)
        
        result_df = pd.concat([new_df_1t, new_df_2t, new_df_3t, new_df_dfp], axis=1)
        
        return result_df
    
    # -------------------------------------------- SCRIPT -------------------------------------------- #
    
    # DICIONÁRIOS PARA SALVAR OS DADOS
    dataframes_itr = {}
    dataframes_dfp = {}
    
    # ITERANDO PELOS DADOS TRIMESTRAIS
    path = os.getcwd() + '\\dados_cvm_itr'
    if not os.path.exists(path):
        messagebox.showinfo('Dados trimestrais não encontrados', "Clique no botão 'Baixar dados trimestrais'", icon='warning')
        sys.exit()
    
    with zipfile.ZipFile(path + f'\\itr_cia_aberta_{year}.zip', 'r') as zipf:
        for relevant in relevant_data:
            with zipf.open(f'itr_cia_aberta_{relevant}_con_{year}.csv', 'r') as csv_file:
                print(csv_file)
                df_itr = pd.read_csv(csv_file, 
                                 sep=';', 
                                 encoding='ISO-8859-1',
                                 usecols=columns
                                )
                df_itr = df_itr[df_itr['CD_CVM'] == cia_code]
                df_itr = df_itr[df_itr['ORDEM_EXERC'] != 'PENÚLTIMO']
                dataframes_itr[relevant] = df_itr
    
    # ITERANDO PELOS DADOS DO DEMONSTRATIVO FINANCEIRO PADRONIZADO
    path = os.getcwd() + '\\dados_cvm_dfp'
    if not os.path.exists(path):
        messagebox.showinfo('Dados do DFP não encontrados', "Clique no botão 'Baixar DFPs'", icon='warning')
        sys.exit()
    
    with zipfile.ZipFile(path + f'\\dfp_cia_aberta_{year}.zip', 'r') as zipf:
        for relevant in relevant_data:
            with zipf.open(f'dfp_cia_aberta_{relevant}_con_{year}.csv', 'r') as csv_file:
                print(csv_file)
                df_dfp = pd.read_csv(csv_file, 
                                 sep=';', 
                                 encoding='ISO-8859-1',
                                 usecols=columns
                                )
                df_dfp = df_dfp[df_dfp['CD_CVM'] == cia_code]
                df_dfp = df_dfp[df_dfp['ORDEM_EXERC'] != 'PENÚLTIMO']
                dataframes_dfp[relevant] = df_dfp
    
    # JUNTANDO OS DICIONÁRIOS DE DADOS TRIMESTRAIS E DE DEMONSTRATIVO FINANCEIRO PADRONIZADO
    combined_dict = {} 
    for key in dataframes_itr.keys():
        combined_dict[key] = pd.concat([dataframes_itr[key], dataframes_dfp[key]], ignore_index=True)
    
    # DICIONÁRIO DE DADOS GERAL
    data = {'BPA': {}, 'BPP': {}, 'DFC_MI': {}, 'DRE': {}}
    
    for period, dt in zip(periods, dt_fim_exerc):
        for category in data:
            data[category][period] = eval(f"combined_dict['{category}'][combined_dict['{category}']['DT_FIM_EXERC'] == '{dt}']")
    
    # CRIANDO O ARQUIVO EXCEL
    result_df_bpa = process_dataframe('BPA')
    result_df_bpp = process_dataframe('BPP')
    result_df_dfc = process_dataframe('DFC_MI')
    result_df_dre = process_dataframe('DRE')
    
    cia_name = df_itr['DENOM_CIA'].iloc[0] # NOME DA EMPRESA
    print(cia_name)
        
    print('Salvando arquivo...')

    output_path = filedialog.asksaveasfilename(defaultextension='.xlsx', filetypes=[("Excel files", "*.xlsx")], initialfile=f'{cia_name}_{year}')
    
    if output_path:
        with pd.ExcelWriter(output_path) as writer:
            result_df_bpa.to_excel(writer, sheet_name='Balanço Patrimonial Ativo', index=False)
            result_df_bpp.to_excel(writer, sheet_name='Balanço Patrimonial Passivo', index=False)
            result_df_dfc.to_excel(writer, sheet_name='Demonstração de Fluxo de Caixa', index=False)
            result_df_dre.to_excel(writer, sheet_name='Demonstraçõa de Resultado', index=False)
        
        messagebox.showinfo('Arquivo salvo', 'Arquivo salvo com sucesso')
    
    else:
        messagebox.showinfo('Operação cancelada', 'Operação cancelada', icon='error')

except Exception as e:
    messagebox.showinfo('ERRO', 'Operação inválida\n\n- Verifique o código CVM\n\n- Verifique o ano\n\n- A empresa pode não ter dados disponíveis para o ano selecionado', icon='error')