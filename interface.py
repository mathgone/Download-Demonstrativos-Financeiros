import customtkinter as ctk
from PIL import Image
import subprocess

def generate_excel():
    user_input_code = entry_code.get()
    user_input_year = combobox.get()
    subprocess.run(['python', 'filtro_demonstrativos_financeiros.py', user_input_code, user_input_year])

def download_data():
    subprocess.run(['python', 'download_dados.py'])

def exec_setup():
    subprocess.run(['python', 'setup.py'])
        
img_excel = Image.open('excel.png')
img_download = Image.open('download.png')
img_packages = Image.open('packages.png')

combobox_values = [str(year) for year in range(2010, 2025)]

width = 300
height = 350

app = ctk.CTk()
app.geometry(f'{width}x{height}')
app.title("Filtro DFP")
app.resizable(width=False, height=False)
app.grid_columnconfigure(0, weight=1)
app.grid_rowconfigure((0,1,2,3,4,5,6), weight=1)


# Input label
label = ctk.CTkLabel(master=app, 
                     text='Digite o código da compania', 
                     font=('Arial', 16))
label.grid(row=0, column=0, pady=(10, 0), padx=10)  # Adjust the pady and padx values as needed

# Input box
entry_code = ctk.CTkEntry(master=app, 
                          border_color='#212F3D', 
                          border_width=2, 
                          placeholder_text='Código da CIA')
entry_code.grid(row=1, column=0, padx=10)

# Dropdown list label
label = ctk.CTkLabel(master=app, 
                     text='Selecione o ano', 
                     font=('Arial', 16))
label.grid(row=2, column=0, pady=(10, 0), padx=10)  # Adjust the pady and padx values as needed

# Dropdown list box
combobox = ctk.CTkComboBox(master=app, 
                           border_color='#212F3D', 
                           border_width=2, 
                           values=combobox_values)
combobox.grid(row=3, column=0, padx=10)

# Generate Excel Button
button_excel = ctk.CTkButton(master=app, 
                       text='Gerar Excel', 
                       corner_radius=32, 
                       fg_color='#1D6F42', 
                       hover_color='#4158D0',
                       image=ctk.CTkImage(img_excel),
                       command=generate_excel
                       )
button_excel.grid(row=4, column=0, pady=(20, 0))

# Download data button
button_download = ctk.CTkButton(master=app, 
                       text='Baixar dados', 
                       corner_radius=32, 
                       fg_color='#1D6F42', 
                       hover_color='#4158D0',
                       image=ctk.CTkImage(img_download),
                       command=download_data
                       )
button_download.grid(row=5, column=0, pady=(20, 0))

# Execute setup.py button
button_setup = ctk.CTkButton(master=app, 
                       text='Verificar bibliotecas', 
                       corner_radius=32, 
                       fg_color='#1D6F42', 
                       hover_color='#4158D0',
                       image=ctk.CTkImage(img_packages),
                       command=exec_setup
                       )
button_setup.grid(row=6, column=0, pady=(20, 10))

app.mainloop()