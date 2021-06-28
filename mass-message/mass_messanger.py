import tkinter as tk
from tkinter import ttk
import excel_tools
import email_tools

def email_list_create(List):
	x = List.splitlines(False)
	return x
		

def importer(column):
	filepath = excel_tools.Get_Filepath_Gui("Excel Files","*.xlsx")
	if not filepath:
		return
	pull = excel_tools.ArrayFromExcel(filepath,column)
	return (pull)
def bcc_importer(c):
	pull = importer(c)
	for i in pull:
		BCC_Email.insert(tk.END, i)
		if i != pull[-1]:
			BCC_Email.insert(tk.END, "\n")
	return True
def cc_importer(c):
	pull = importer(c)
	for i in pull:
		CC_Email.insert(tk.END, i)
		if i != pull[-1]:
			CC_Email.insert(tk.END, "\n")
	return True
def attachment_import():
	filepath = excel_tools.Get_Filepath_Gui("All Files","*.*")
	Attachment_Email.insert(tk.END, filepath)
	Attachment_Email.insert(tk.END, "\n")
	
def text_importer(c):
	pull = importer(c)
	for i in pull:
		Text_List.insert(tk.END, i)
		if i != pull[-1]:
			Text_List.insert(tk.END, "\n")
	return True
	
#main window
window = tk.Tk()
window.title("Mass Messenger v 0.0.1")	

#making tabs
tabControl = ttk.Notebook(window)
email = tk.Frame(tabControl)
ptext = tk.Frame(tabControl)

tabControl.add(email, text = 'Mass Email')
tabControl.add(ptext, text = 'Mass Text')
tabControl.pack(expand = 1)

#email tab contents
email.columnconfigure((0,5), weight=1)
email.rowconfigure((0,5),weight=1)

#filling tabs (email)
#email frame, from, list of to and login
fr_email_ft = tk.Frame(email,relief=tk.RAISED,bd=2)
fr_email_ft.grid(row=0,column=0)

fr_email_body = tk.Frame(email,relief=tk.RAISED,bd=2)
fr_email_body.grid(row=1,column=0)
#from
tk.Label(fr_email_ft, text="From:").grid(row=0,column=0)
From_Email = tk.Entry(fr_email_ft)
From_Email.grid(row=0,column=1)
#	Login = tk.Button(fr_email_ft,text="Login",command=lambda: email_tools.email_login_gui(From_Email.get())).grid(row=0,column=2)
#to
tk.Label(fr_email_ft, text="To:").grid(row=0,column=3)
To_Email = tk.Entry(fr_email_ft)
To_Email.grid(row=0,column=4)
#cc
CC_Email = tk.Text(fr_email_body, width='25')
CC_Email.grid(row=1,column=2)
#bcc
BCC_Email = tk.Text(fr_email_body, width='25')
BCC_Email.grid(row=1,column=3)

tk.Label(fr_email_ft, text="Subject:").grid(row=0,column=5)
Subject_Email = tk.Entry(fr_email_ft)
Subject_Email.grid(row=0,column=6)
#mass loader from a excel doc
BCC_Import = tk.Button(fr_email_body, text="BCC Import",command=lambda: bcc_importer('Email')).grid(row=0,column=3)
CC_Import = tk.Button(fr_email_body, text="CC Import",command=lambda: cc_importer('Email')).grid(row=0,column=2)
email_txt_edit_label = tk.Label(fr_email_body, text="Message body").grid(column=1, row=0,)
#message body
Body_Email= tk.Text(fr_email_body)
Body_Email.grid(row=1,column=1)

Attachment_Import = tk.Button(fr_email_body, text="Attachments", command=lambda: attachment_import())
Attachment_Import.grid(row=0,column=0)

Attachment_Email = tk.Text(fr_email_body, width='30')
Attachment_Email.grid(row=1,column=0)
Send_Button = tk.Button(fr_email_ft, text="Send", command=lambda: email_tools.email_send(To_Email.get(),From_Email.get(), Subject_Email.get(), Body_Email.get("1.0","end-1c"),email_list_create(Attachment_Email.get("1.0","end-1c")),email_list_create(CC_Email.get("1.0","end-1c")),email_list_create(BCC_Email.get("1.0","end-1c")))).grid(row=0,column=7)

#text tab contents
fr_text_ft = tk.Frame(ptext,relief=tk.RAISED,bd=2)
fr_text_ft.grid(row=0,column=0)

#from
From_Number_Label = tk.Label(fr_text_ft,text="From: (").grid(column=0, row=0)
From_Number_Area = tk.Entry(fr_text_ft,width=3)
From_Number_Area.grid(row=0,column=1)
From_Number_Label2 = tk.Label(fr_text_ft,text=") - ").grid(row=0,column=2)
From_Number_First3 = tk.Entry(fr_text_ft,width=3)
From_Number_First3.grid(row=0,column=3)
From_Number_Label3 = tk.Label(fr_text_ft,text=" - ").grid(row=0,column=4)
From_Number_Last4 = tk.Entry(fr_text_ft,width=4)
From_Number_Last4.grid(row=0,column=5)

Text_Import = tk.Button(fr_text_ft, text="Text Import",command=lambda: text_importer('Cell Number')).grid(row=0,column=6)
Text_List = tk.Text(fr_text_ft, width='25')
Text_List.grid(row=0,column=7)
window.mainloop()
