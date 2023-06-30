import tkinter as tk
from tkinter import ttk
import socket
import time

IP = "192.168.1.116"
PORT = 5000
ADDR= (IP,PORT)
FORMAT= "utf-8"
SIZE=2048

# Functie apelata atunci cand se apasa 'Run'
def run_button_clicked():
    # Curatarea tab-ului din dreapta
	output_text.config(state='normal')
	output_text.delete('1.0', tk.END)  # sterge tot textul din obiectul Text
	output_text.config(state='disabled')
	output_text.config(state='normal')
    
    # Implementare conexiune server
	client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	client.connect(ADDR)
	data=editor1.get("1.0", tk.END)
	client.send(data.encode(FORMAT))
	
	err = client.recv(SIZE).decode(FORMAT)
	msg1 = client.recv(SIZE).decode(FORMAT)
	client.close()
        	
	# create custom tags with desired colors
	output_text.tag_config("red", foreground="#eb0505")
	output_text.tag_config("green", foreground="#258a42")

    # apply appropriate tag to msg1 based on the value of err
	if err == "1":
		output_text.insert('end', msg1, "green")
	else:
		output_text.insert('end', msg1, "red")
	output_text.config(state='disabled')

# Functie apelata la apasarea butonului "Clear"
def cler_button_clicked():
    editor1.delete("1.0", tk.END)

# Crearea ferestrei principale
root = tk.Tk()
root.title('Aplicatie cod C/C++')

icon_path = "D:/ATM/practica/python/python2.ico"
root.wm_iconbitmap(icon_path)

# Maximizarea ferestrei principale
root.wm_state('zoomed')

# Crearea unui control Notebook
notebook = ttk.Notebook(root)
notebook.pack(fill='both', expand=True)

# Adaugarea tab-ului din stanga
tab1 = ttk.Frame(notebook)
notebook.add(tab1, text='Stânga')

# Adaugarea tab-ului din dreapta
tab2 = ttk.Frame(notebook)
notebook.add(tab2, text='Dreapta')

# Scrollbar pentru tab-ul din stanga
scrollbar = tk.Scrollbar(tab1)

# Crearea unui editor text pentru tab-ul din stanga
editor1 = tk.Text(tab1, yscrollcommand=scrollbar.set, height=30, width=70)
scrollbar.config(command=editor1.yview)
scrollbar.pack(side='right', fill='y')
editor1.pack(fill='both', expand=True)

# Preluarea dimensiunilor paginii
screen_width = root.winfo_screenwidth()
screen_height= root.winfo_screenheight()

# Crearea butonului "Run"
run_button = tk.Button(tab1, text='Run', command=run_button_clicked)
run_button.place(x= screen_width/2 -130, y= screen_height -105,width=100,height=30)

# Creare butonului pentru "Clear"
clear_button= tk.Button(tab1, text='Clear', command=cler_button_clicked)
clear_button.place(x= screen_width/2 -250, y= screen_height -105,width=100,height=30)

# Crearea unui scrollbar pentru tab-ul din dreapta
output_scrollbar = tk.Scrollbar(tab2)

# Crearea obiectului Text în tab-ul din dreapta
output_text = tk.Text(tab2, yscrollcommand=output_scrollbar.set, height=30, width=70, state='disabled')
output_scrollbar.config(command=output_text.yview)
output_scrollbar.pack(side='right', fill='y')
output_text.pack(fill='both', expand=True)

# Setarea dimensiunii tab-ului din stânga
tab1_width = int(screen_width / 2)
tab1.place(x=0, y=0, width=tab1_width, height=screen_height-60)

# Setarea dimensiunii tab-ului din dreapta
tab2.place(x=tab1_width, y=0, width=tab1_width, height=screen_height)

# Rularea buclei evenimentului principal
root.mainloop()