import tkinter as tk
from tkinter import ttk
import excel_tools
import email_tools

def importer(column):
	filepath = excel_tools.Get_Filepath_Gui()
	if not filepath:
		return
	pull = excel_tools.ArrayFromExcel(filepath,column)
	for i in pull:
		print(i)
	return (pull)

def bcc_importer():
	return importer('email')

def cc_importer():
	return importer('email')
#main window
window = tk.Tk()
window.title("Mass Messenger")	

#making tabs
tabControl = ttk.Notebook(window)
email = ttk.Frame(tabControl)
ptext = ttk.Frame(tabControl)

tabControl.add(email, text = 'Mass Email')
tabControl.add(ptext, text = 'Mass Text')
tabControl.pack(expand = 1, fill="both")

email.columnconfigure((0,4), weight=1)
email.rowconfigure((0,4),weight=1)

#filling tabs (email)
#email frame, from, list of to and login
fr_email_ft = tk.Frame(email,relief=tk.RAISED,bd=2)
fr_email_ft.grid(row=0,column=0)
#from
tk.Label(fr_email_ft, text="From").grid(row=0,column=0)
From_Email = ttk.Entry(fr_email_ft)
From_Email.grid(row=0,column=1)
Login = tk.Button(fr_email_ft,text="Login",command=lambda: email_tools.email_login(From_Email.get())).grid(row=0,column=2)
#to
tk.Label(fr_email_ft, text="To").grid(row=0,column=3)
To_Email = ttk.Entry(fr_email_ft)
To_Email.grid(row=0,column=4)
#cc
tk.Label(fr_email_ft, text="CC").grid(row=0,column=5)
CC_Email = ttk.Entry(fr_email_ft)
CC_Email.grid(row=0,column=6)
#bcc
tk.Label(fr_email_ft, text="BCC").grid(row=0,column=7)
BCC_Email = ttk.Entry(fr_email_ft)
BCC_Email.grid(row=0,column=8)

#mass loader from a excel doc
Import = tk.Button(fr_email_ft, text="Import",command=lambda: importer('email')).grid(row=0,column=9)

txt_edit = tk.Text(ptext).grid(column=0, row=0, sticky="nsew")
window.mainloop()