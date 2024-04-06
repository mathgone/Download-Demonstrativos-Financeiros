import subprocess
from tkinter import messagebox
import sys

packages = ['pandas', 'requests', 'openpyxl']

for package in packages:
    try:
        __import__(package)
        messagebox.showinfo('Módulo instalado', f'O módulo {package} já foi instalado')
    except ImportError:
        print(f'Instalando {package}...')
        subprocess.check_call(['pip', 'install', package])
        messagebox.showinfo('Download completo', f'Módulo {package} instalado')
