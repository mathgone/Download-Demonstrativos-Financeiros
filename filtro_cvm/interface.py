from pathlib import Path
import os

current_path = os.getcwd()

from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, font

import subprocess

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(current_path + '\\assets')

# -------------------------- FUNÇÕES -------------------------- #

def generate_excel():
    input1 = entry_cia_code.get()
    input2 = entry_year.get()
    subprocess.run(['python', 'filtro.py', input1, input2])

def download_data_itr():
    subprocess.run(['python', 'download_dados_itr.py'])

def download_data_dfp():
    subprocess.run(['python', 'download_dados_dfp.py'])

def verify_packages():
    subprocess.run(['python', 'setup.py'])

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

# -------------------------- INTERFACE -------------------------- #

window = Tk()

window.geometry("899x501")
window.title('Filtro CVM')
icon_path = os.getcwd() + '\\assets' + '\\filtro.png'
window.iconphoto(True, PhotoImage(file=icon_path))
window.configure(bg = "#FFFFFF")

canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 501,
    width = 899,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    317.0,
    -2.0,
    320.0000000000001,
    501.0,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    0.0,
    0.0,
    899.0,
    101.0,
    fill="#1D6F42",
    outline="")

canvas.create_text(
    29.0,
    29.0,
    anchor="nw",
    text="DOWNLOAD DEMONSTRATIVOS FINANCEIROS",
    fill="#FFFFFF",
    font=("Allerta Regular", 34 * -1)
)

# -------------------------- LABEL FILTRO -------------------------- #

canvas.create_text(
    28.0,
    118.0,
    anchor="nw",
    text="FILTRO",
    fill="#1D6F42",
    font=("Allerta Regular", 24 * -1)
)

# -------------------------- LABEL DOWNLOAD DOS DADOS -------------------------- #

canvas.create_text(
    360.0,
    118.0,
    anchor="nw",
    text="DOWNLOAD DOS DADOS",
    fill="#1D6F42",
    font=("Allerta Regular", 24 * -1)
)

# -------------------------- INPUT CÓDIGO DA COMPANIA -------------------------- #

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    153.0,
    220.0,
    image=entry_image_1
)
entry_cia_code = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0,
    font=font.Font(family="Allerta Regular", size=12)
)
entry_cia_code.place(
    x=38.0,
    y=195.0,
    width=230.0,
    height=48.0
)

canvas.create_text(
    37.0,
    177.0,
    anchor="nw",
    text="CÓDIGO CVM",
    fill="#1D6F42",
    font=("Allerta Regular", 14 * -1)
)

# -------------------------- INPUT ANO -------------------------- #

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    153.0,
    322.0,
    image=entry_image_2
)
entry_year = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0,
    font=font.Font(family="Allerta Regular", size=12)
)
entry_year.place(
    x=38.0,
    y=297.0,
    width=230.0,
    height=48.0
)

canvas.create_text(
    37.0,
    279.0,
    anchor="nw",
    text="ANO",
    fill="#1D6F42",
    font=("Allerta Regular", 14 * -1)
)

# -------------------------- BOTÃO GERAR EXCEL -------------------------- #

generate_excel_icon = PhotoImage(
    file=relative_to_assets("generate_excel.png"))
generate_excel_button = Button(
    image=generate_excel_icon,
    borderwidth=0,
    highlightthickness=0,
    command=generate_excel,
    relief="flat"
)
generate_excel_button.place(
    x=53.0,
    y=399.0,
    width=200.0,
    height=50.0
)

# -------------------------- BOTÃO BAIXAR DADOS TRIMESTRAIS -------------------------- #

baixar_dados_trimestrais_icon = PhotoImage(
    file=relative_to_assets("baixar_dados_trimestrais.png"))
baixar_dados_trimestrais_button = Button(
    image=baixar_dados_trimestrais_icon,
    borderwidth=0,
    highlightthickness=0,
    command=download_data_itr,
    relief="flat"
)
baixar_dados_trimestrais_button.place(
    x=421.0,
    y=195.0,
    width=349.0,
    height=50.0
)

# -------------------------- BOTÃO DOWNLOAD DFPs -------------------------- #

baixar_dfps_icon = PhotoImage( 
    file=relative_to_assets("baixar_dfps.png"))
baixar_dfps_button = Button(
    image=baixar_dfps_icon,
    borderwidth=0,
    highlightthickness=0,
    command=download_data_dfp,
    relief="flat"
)
baixar_dfps_button.place(
    x=421.0,
    y=276.0,
    width=349.0,
    height=50.0
)

# -------------------------- BOTÃO VERIFICAR BIBLIOTECAS -------------------------- #

verificar_bibliotecas_icon = PhotoImage(
    file=relative_to_assets("verificar_bibliotecas.png"))
verificar_bibliotecas_button = Button(
    image=verificar_bibliotecas_icon,
    borderwidth=0,
    highlightthickness=0,
    command=verify_packages,
    relief="flat"
)
verificar_bibliotecas_button.place(
    x=421.0,
    y=357.0,
    width=349.0,
    height=50.0
)

# -------------------------- ÍCONE DO EXCEL NO CANTO INFERIOR DIREITO -------------------------- #

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    860.0,
    460.0,
    image=image_image_1
)

window.resizable(False, False)
window.mainloop()