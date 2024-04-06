## Sumário
- ### [Apresentação](#download-demonstrativos-financeiros)
  - ### [Resumo das funcionalidades](#resumo-das-funcionalidades)
- ### [Guia de uso](#para-realizar-o-download-das-dfps-siga-os-passos-abaixo)
  - ### [Pré-requesitos](#instale-o-python-em-seu-computador)
  - ### [Passo a passo para baixar e utlizar o programa](#como-baixar-e-utilizar-o-programa)
    - [1. Baixe a pasta scripts.zip]()
    - [2. Extraia os arquivos]()
    - [3. Execute o script interface.py]()
    - [4. Clique no botão Verificar bibliotecas]()
    - [5. Clique no botão Baixar dados trimestrais]()
    - [6. Clique no botão Baixar DFPs]()
    - [7. Digite o código CVM da empresa e o ano da DFP]()
    - [8. Clique no botão Gerar Excel]()
   
[click here to jump to my anchor](#custom_anchor_name)
------------------------

<a name="custom_anchor_name"></a>
# some header

# Download Demonstrativos Financeiros

## Faça download do Demonstrativos Financeiros de uma empresa listada na B3 

- Exemplo de Excel gerado

![](https://i.postimg.cc/cCXmRbCj/planilha.png)
- Link para acessar a planilha: [https://docs.google.com](https://docs.google.com/spreadsheets/d/1U45nzbGmEVZjq0cGmKAqq7J9ZpSKAg2d/edit?usp=drive_link&ouid=103571908927816967898&rtpof=true&sd=true)

## Resumo das funcionalidades
- Este programa faz o download automático da Demonstração de Resultado de uma compania a partir de seu código CVM e do ano de análise dados pelo usuário

- São disponibilizados os dados de:

    - Balanço Patrimonial Ativo (BPA) Consolidado
    - Balanço Patrimonial Passivo (BPP) Consolidado
    - Demonstração de Fluxo de Caixa (DFC) Consolidado
    - Demonstração de Resultado (DRE) Consolidado

##### Interface do programa
![](https://i.postimg.cc/4xk3sNB8/user-interface.png)

# Para realizar o download das DFPs, siga os passos abaixo

> [!WARNING]
> É importante que o usuário tenha Python instalado em sua máquina.
# Instale o Python em seu computador

- Acesse [python.org](https://www.python.org/downloads/) e baixe Python para seu sistema operacional
- Certifique-se de marcar a opção **add python.exe to PATH**
  
![Instalador do Python](https://i.postimg.cc/s2zcPcV8/python-installer.png)

# Como baixar e utilizar o programa

# 1. Baixe a pasta [scripts.zip](https://github.com/mathgone/Download-Demonstrativos-Financeiros/blob/main/scripts.zip)

# 2. Extraia os arquivos

> [!IMPORTANT]
> Para garantir o funcionamento do programa, mantenha todos os arquivos extraídos em um único diretório.

![Tutorial como extrair arquivos](https://i.postimg.cc/gj9MyTKz/extract-folder.png)

# 3. Execute o script [interface.py](https://github.com/mathgone/Download-Demonstrativos-Financeiros/blob/main/scripts/interface.py)

> [!TIP]
> Segurando a tecla ALT, você pode arrastar o arquivo interface.py para outro diretório para criar um atalho.

![Interface do usuário](https://i.postimg.cc/4xk3sNB8/user-interface.png)

# 5. Clique no botão ![Botão Verificar bibliotecas](https://i.postimg.cc/YSy0cNVF/verificar-bibliotecas.png)

- Este botão irá executar o script [setup.py]()
- Será feito o download de todos os módulos necessários para o funcionamento do programa

# 5. Clique no botão ![Baixar dados trimestrais](https://i.postimg.cc/7PJGkcqZ/baixar-dados-trimestrais.png)

- Este botão irá executar o script [donwload_dados_itr.py]()
- Será realizado o download das [ITRs (2011 - 2023)](https://dados.cvm.gov.br/dados/CIA_ABERTA/DOC/DFP/DADOS/) de Companias Abertas
- Os dados serão salvos na pasta **dados_cvm_itr**

# 6. Clique no botão ![Baixar DFPs](https://i.postimg.cc/7Z9b9rnm/baixar-dfps.png)

- Este botão irá executar o script [donwload_dados_dfp.py]()
- Será realizado o download das [DFPs (2010 - 2023)](https://dados.cvm.gov.br/dados/CIA_ABERTA/DOC/DFP/DADOS/) de Companias Abertas
- Os dados serão salvos na pasta **dados_cvm_dfp**

# 6. Digite o código CVM da empresa e o ano da DFP

- Os códigos CVM das empresas podem ser encontrados [aqui](https://cvmweb.cvm.gov.br/SWB/Sistemas/SCW/CPublica/CiaAb/FormBuscaCiaAbOrdAlf.aspx?LetraInicial=A)

![Interface do usuário com Inputs](https://i.postimg.cc/j2WhCnFn/user-interface-inputs.png)

# 7. Clique no botão  ![Botão Gerar Excel](https://i.postimg.cc/W44zfY9j/generate-excel.png)

- Um [arquivo Excel]() será gerado com as especificações dadas
