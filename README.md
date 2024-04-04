# Download Demonstrativos Financeiros Padronizados
## Faça download do Demonstrativo Financeiro Padronizado (DFP) de uma empresa listada na B3 

Para realizar o download das DFPs, siga os passos abaixo:

# 1. Instale o Python em seu computador

- Acesse [python.org](https://www.python.org/downloads/) e baixe Python para seu sistema operacional
- Certifique-se de marcar a opção **add python.exe to PATH**
  
![](https://i.postimg.cc/s2zcPcV8/python-installer.png)

# 2. Baixe a pasta [scripts.zip](https://github.com/mathgone/Download-Demonstrativos-Financeiros/blob/main/scripts.zip)

# 3. Extraia os arquivos

![](https://i.postimg.cc/Jz4sJ6vt/image.png)

# 4. Execute o script [setup.py](https://github.com/mathgone/Download-Demonstrativos-Financeiros/blob/main/scripts/setup.py)

###### Para garantir o funcionamento do programa, todos os scripts devem estar em um único diretório
- Este script irá instalar as bibliotecas do Python necessárias

# 5. Execute o script [interface.py](https://github.com/mathgone/Download-Demonstrativos-Financeiros/blob/main/scripts/interface.py)

![](https://i.postimg.cc/HxcmC5Kp/interface.png)

- Para verificar se os módulos foram instalados corretamente, clique no botão  ![](https://i.postimg.cc/K8HnJk6P/interface-verificar-biblioteca.png)

# 6. Clique no botão  ![](https://i.postimg.cc/qvL7vs70/interface-baixar-dados.png)

- Este botão irá executar o script [donwload_dados.py](https://github.com/mathgone/Download-Demonstrativos-Financeiros/blob/main/scripts/download_dados.py)
- Será realizado o download das [DFPs (2010 - 2023)](https://dados.cvm.gov.br/dados/CIA_ABERTA/DOC/DFP/DADOS/) de Companias Abertas
- Os dados serão salvos na pasta **dados_cvm**

# 7. Digite o código CVM da empresa e o ano da DFP

- Os códigos das empresas podem ser encontrados [aqui](https://cvmweb.cvm.gov.br/SWB/Sistemas/SCW/CPublica/CiaAb/FormBuscaCiaAbOrdAlf.aspx?LetraInicial=A)

![](https://i.postimg.cc/SxvvCKV5/image.png)

# 8. Clique no botão  ![](https://i.postimg.cc/nV3M4bb7/image.png)

- Um [arquivo Excel](https://github.com/mathgone/Download-Demonstrativos-Financeiros/blob/main/ALPARGATAS%20S.A.%20-%202021%20(exemplo).xlsx) será gerado com as especificações dadas
- Você pode analisar o arquivo gerado no exemplo clicando [aqui](https://docs.google.com/spreadsheets/d/1xZ_fXTsaw5FEhF6XI1VJJExQuG1A7i8K6ko_rh2QZ40/edit?usp=sharing)
