# Download Demonstrativos Financeiros
### Faça download dos demonstrativos financeiros de uma empresa listada na B3 

Para realizar o download das DFPs, siga os passos abaixo:

---
###### Bibliotecas do Python necessárias: tkinter, pandas, requests
1. Coloque os arquivos ['download_dados.py'](https://github.com/mathgone/Download-Demonstrativos-Financeiros/blob/main/download_dados.py) e ['filtro_demonstrativos_financeiros.pyw'](https://github.com/mathgone/Download-Demonstrativos-Financeiros/blob/main/filtro_demonstrativos_financeiros.pyw) em uma única pasta

2. Execute o programa ['download_dados.py'](https://github.com/mathgone/Download-Demonstrativos-Financeiros/blob/main/download_dados.py)
    
     * Este script irá fazer o download dos [DFPs (2010 - 2023)](https://dados.cvm.gov.br/dados/CIA_ABERTA/DOC/DFP/DADOS/) de Companias Abertas.
     * Os dados serão salvos em uma pasta denominada **'dados_cvm'**

[<img src="https://i.postimg.cc/MTD9pQp5/cvm-website.png">](https://dados.cvm.gov.br/dados/CIA_ABERTA/DOC/DFP/DADOS/)


3. Em seguida, execute o arquivo ['filtro_demonstrativos_financeiros.pyw'](https://github.com/mathgone/Download-Demonstrativos-Financeiros/blob/main/filtro_demonstrativos_financeiros.pyw)

    * Na tela de prompt, digite o código da compania e especifique o ano do DFP
    
    ![alt text](https://i.postimg.cc/tJ9gG7rF/prompt.png "Janela de Prompt")

    * Os códigos das companias podem ser encontrados [aqui](https://cvmweb.cvm.gov.br/SWB/Sistemas/SCW/CPublica/CiaAb/FormBuscaCiaAbOrdAlf.aspx?LetraInicial=A)

[<img src="https://i.postimg.cc/fL45whQw/cia-code-table.png">](https://cvmweb.cvm.gov.br/SWB/Sistemas/SCW/CPublica/CiaAb/FormBuscaCiaAbOrdAlf.aspx?LetraInicial=A)

4. Clique no botão **_Generate Excel_** e salve o Excel gerado

   * Para ver um exemplo de planilha gerada, baixe o arquivo [exemplo.xslx](https://github.com/mathgone/Download-Demonstrativos-Financeiros/blob/main/exemplo.xlsx) (Alpargatas, código: 10456 | Ano do DFP: 2021)






