import subprocess
import importlib

packages = ['pandas', 'customtkinter', 'requests']

def install_package(package):
    try:
        importlib.import_module(package)
        print(f'----- {package} já está instalado -----')
    except ImportError:
        print(f'\n----- Instalando {package} -----')
        subprocess.check_call(['pip', 'install', package])
        print(f'----- Instalação da biblioteca {package} finalizado -----\n')

for package in packages:
    install_package(package)