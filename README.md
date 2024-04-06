# Sumário
- # [Apresentação](#download-demonstrativos-financeiros)
  - ## [Resumo das funcionalidades](#resumo_funcionalidades)
- # [Guia de instalação e de uso](#guia)
  - ## [Pré-requesitos](#pre_requisitos)
    - ### [1. Python](#instalar_python)
    - ### [2. Site de códigos CVM](#codigo_cvm)
  - ## [Passo a passo para baixar e utilizar o programa](#como-baixar-e-utilizar-o-programa)
    - ### [1. Baixe a pasta scripts.zip](#baixar_pasta_script)
    - ### [2. Extraia os arquivos](#extrair_pasta_script)
    - ### [3. Execute o script interface.py](#executar_interface)
    - ### [4. Clique no botão Verificar bibliotecas](#clicar_botao_verificar_bibliotecas)
    - ### [5. Clique no botão Baixar dados trimestrais](#clicar_botao_baixar_dados_trimestrais)
    - ### [6. Clique no botão Baixar DFPs](#clicar_botao_baixar_dfps)
    - ### [7. Digite o código CVM da empresa e o ano da DFP](#inputs)
    - ### [8. Clique no botão Gerar Excel](#clicar_botao_gerar_excel)
   
------------------------

# Download Demonstrativos Financeiros

## Faça download do Demonstrativos Financeiros de uma empresa listada na B3 

Este é um projeto em Python desenvolvido para baixar os demonstrativos financeiros de empresas disponíveis no site da [Comissão de Valores Mobiliários (CVM)](https://dados.cvm.gov.br/) do Brasil. Ele oferece uma maneira rápida e automatizada de obter informações financeiras importantes das companhias listadas na bolsa de valores brasileira.

###### Interface do programa
<img align="center" width='80%' src="https://i.postimg.cc/4xk3sNB8/user-interface.png">

<a name="resumo_funcionalidades"></a>
## Resumo das funcionalidades
- **Download Automatizado**: O programa baixa automaticamente os demonstrativos financeiros da empresa desejada;
- **Dados Abertos e Acessíveis**: Os dados são obtidos a partir do site oficial da CVM;
- **Flexibilidade de Seleção**: O usuário pode fornecer o código CVM da empresa e o ano desejado para baixar os dados específicos.

- No arquivo Excel gerado, são disponibilizados os dados de:

    - Balanço Patrimonial Ativo (BPA) Consolidado
    - Balanço Patrimonial Passivo (BPP) Consolidado
    - Demonstração de Fluxo de Caixa (DFC) Consolidado
    - Demonstração de Resultado (DRE) Consolidado

###### Exemplo de Excel gerado pelo programa
<img align="center" width='100%' src="https://i.postimg.cc/cCXmRbCj/planilha.png">

- Link para acessar a planilha: [https://docs.google.com](https://docs.google.com/spreadsheets/d/18aJ9YykdlPfqjOoxF577g4grvyuqFuht/edit?usp=sharing&ouid=103571908927816967898&rtpof=true&sd=true)
------------------------

<a name="guia"></a>
# Guia de instalação e de uso

<a name="pre_requisitos"></a>
## Pré-requisitos


<a name="instalar_python"></a>
### 1. Instale o Python em seu computador
> [!WARNING]
> É importante que o usuário tenha Python instalado em sua máquina.

- Acesse [python.org](https://www.python.org/downloads/) e baixe Python para seu sistema operacional
- Certifique-se de marcar a opção **add python.exe to PATH**
  
###### Instalador do Python
<img align="center" width='65%' src="https://i.postimg.cc/s2zcPcV8/python-installer.png">

<a name="codigo_cvm"></a>
### 2. Site de códigos CVM
> [!NOTE]
> Acesse o site abaixo para encontrar os códigos CVM das empresas
- Os códigos CVM das empresas podem ser encontrados no site: [https://cvmweb.cvm.gov.br/](https://cvmweb.cvm.gov.br/SWB/Sistemas/SCW/CPublica/CiaAb/FormBuscaCiaAbOrdAlf.aspx?LetraInicial=A)
------------------------

## Como baixar e utilizar o programa

<a name="baixar_pasta_script"></a>
### 1. Baixe a pasta [filtro_cvm.zip](https://github.com/mathgone/Download-Demonstrativos-Financeiros/blob/main/scripts.zip)
------------------------

<a name="extrair_pasta_script"></a>
### 2. Extraia os arquivos

> [!IMPORTANT]
> Para garantir o funcionamento do programa, mantenha todos os arquivos extraídos em um único diretório.

###### Extração de arquivos zip
<img align="center" width='40%' src="https://i.postimg.cc/gj9MyTKz/extract-folder.png">

------------------------

<a name="executar_interface"></a>
### 3. Execute o script [interface.py](https://github.com/mathgone/Download-Demonstrativos-Financeiros-Padronizados/blob/main/filtro_cvm/interface.py)

> [!TIP]
> Segurando a tecla ALT, você pode arrastar o arquivo interface.py para outro diretório para criar um atalho.

###### Interface do programa
![Interface do usuário](https://i.postimg.cc/4xk3sNB8/user-interface.png)

------------------------

<a name="clicar_botao_verificar_bibliotecas"></a>
### 4. Clique no botão <img align="center" width="33%" src="https://i.postimg.cc/YSy0cNVF/verificar-bibliotecas.png"> 

- Este botão irá executar o script [setup.py](https://github.com/mathgone/Download-Demonstrativos-Financeiros-Padronizados/blob/main/filtro_cvm/setup.py)
- Será feito o download de todos os módulos necessários para o funcionamento do programa
------------------------

<a name="clicar_botao_baixar_dados_trimestrais"></a>
### 5. Clique no botão <img align="center" width='33%' src="https://i.postimg.cc/7PJGkcqZ/baixar-dados-trimestrais.png">

- Este botão irá executar o script [donwload_dados_itr.py](https://github.com/mathgone/Download-Demonstrativos-Financeiros-Padronizados/blob/main/filtro_cvm/download_dados_itr.py)
- Será realizado o download das [ITRs (2011 - 2023)](https://dados.cvm.gov.br/dados/CIA_ABERTA/DOC/DFP/DADOS/) de Companias Abertas
- Os dados serão salvos na pasta **dados_cvm_itr**
------------------------

<a name="clicar_botao_baixar_dfps"></a>
### 6. Clique no botão <img align='center' width='33%' src="https://i.postimg.cc/7Z9b9rnm/baixar-dfps.png">

- Este botão irá executar o script [donwload_dados_dfp.py](https://github.com/mathgone/Download-Demonstrativos-Financeiros-Padronizados/blob/main/filtro_cvm/download_dados_dfp.py)
- Será realizado o download das [DFPs (2010 - 2023)](https://dados.cvm.gov.br/dados/CIA_ABERTA/DOC/DFP/DADOS/) de Companias Abertas
- Os dados serão salvos na pasta **dados_cvm_dfp**
------------------------

<a name="inputs"></a>
### 7. Digite o código CVM da empresa e o ano da DFP

- Os códigos CVM das empresas podem ser encontrados [aqui](https://cvmweb.cvm.gov.br/SWB/Sistemas/SCW/CPublica/CiaAb/FormBuscaCiaAbOrdAlf.aspx?LetraInicial=A)

###### Empresa: ALPARGATAS S.A. | Ano: 2023
![Interface do usuário com Inputs](https://i.postimg.cc/j2WhCnFn/user-interface-inputs.png)
------------------------

<a name="clicar_botao_gerar_excel"></a>
### 8. Clique no botão <img align='center' width='20%' src='https://i.postimg.cc/W44zfY9j/generate-excel.png'>
- Este botão irá executar o script [filtro.py](https://github.com/mathgone/Download-Demonstrativos-Financeiros-Padronizados/blob/main/filtro_cvm/filtro.py)
- Um [arquivo Excel]() será gerado com as especificações dadas
