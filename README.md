# Download Demonstrativos Financeiros
### Faça download dos demonstrativos financeiros de uma empresa listada na B3 

Para realizar o download das DFPs, siga os passos abaixo:

---
###### Bibliotecas do Python necessárias: pandas, requests
1. Acesse [esta pasta no Google Drive](https://drive.google.com/drive/folders/1_XXCsOvaYVDjrRyFr1-M9eABil2dT7z_?usp=sharing) e faça download dos arquivos **download_dados.exe** e **filtro_demonstrativos_financeiros.exe**

2. Coloque os arquivos [download_dados](https://github.com/mathgone/Download-Demonstrativos-Financeiros/blob/main/download_dados.py) e [filtro_demonstrativos_financeiros](https://github.com/mathgone/Download-Demonstrativos-Financeiros/blob/main/filtro_demonstrativos_financeiros.pyw) em uma única pasta

3. Execute o programa [download_dados](https://github.com/mathgone/Download-Demonstrativos-Financeiros/blob/main/download_dados.py)
    
     * Este script irá fazer o download dos [DFPs (2010 - 2023)](https://dados.cvm.gov.br/dados/CIA_ABERTA/DOC/DFP/DADOS/) de Companias Abertas.
     * Os dados serão salvos em uma pasta denominada **'dados_cvm'**

[<img src="https://i.postimg.cc/MTD9pQp5/cvm-website.png">](https://dados.cvm.gov.br/dados/CIA_ABERTA/DOC/DFP/DADOS/)


4. Em seguida, execute o arquivo [filtro_demonstrativos_financeiros](https://github.com/mathgone/Download-Demonstrativos-Financeiros/blob/main/filtro_demonstrativos_financeiros.pyw)

    * Na tela de prompt, digite o código da compania e especifique o ano do DFP
    
    ![alt text](https://i.postimg.cc/tJ9gG7rF/prompt.png "Janela de Prompt")

    * Os códigos das companias podem ser encontrados [aqui](https://cvmweb.cvm.gov.br/SWB/Sistemas/SCW/CPublica/CiaAb/FormBuscaCiaAbOrdAlf.aspx?LetraInicial=A)

[<img src="https://i.postimg.cc/fL45whQw/cia-code-table.png">](https://cvmweb.cvm.gov.br/SWB/Sistemas/SCW/CPublica/CiaAb/FormBuscaCiaAbOrdAlf.aspx?LetraInicial=A)

5. Clique no botão **_Generate Excel_** e salve o Excel gerado

   * Para ver um exemplo de planilha gerada, baixe o arquivo [ALPARGATAS S.A. - 2021 (exemplo).xslx](https://github.com/mathgone/Download-Demonstrativos-Financeiros/blob/main/ALPARGATAS%20S.A.%20-%202021%20(exemplo).xlsx) ou [clique aqui](https://docs.google.com/spreadsheets/d/1xZ_fXTsaw5FEhF6XI1VJJExQuG1A7i8K6ko_rh2QZ40/edit?usp=sharing) (Alpargatas, código: 10456 | Ano do DFP: 2021)






