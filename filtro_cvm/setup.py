import subprocess
from tkinter import messagebox
import sys

packages = ['pandas', 'requests', 'openpyxl']

for package in packages:
    try:
        __import__(package)
        messagebox.showinfo('Módulos instalados', 'Os módulos necessários já estão instalados')
        sys.exit()
    except ImportError:
        print(f'Instalando {package}...')
        subprocess.check_call(['pip', 'install', package])
        messagebox.showinfo('Download completo', f'Módulo {package} instalado')
