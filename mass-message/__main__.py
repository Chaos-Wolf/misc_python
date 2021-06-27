import tkinter as tk
from tkinter import ttk
import excel_tools
import email_tools

def email_list_create(List):
	x = List.splitlines(False)
	return x
		

def importer(column):
	filepath = excel_tools.Get_Filepath_Gui()
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
		print(i)
	return True

def cc_importer(c):
	pull = importer(c)
	for i in pull:
		CC_Email.insert(tk.END, i)
		if i != pull[-1]:
			CC_Email.insert(tk.END, "\n")
		print(i)
	return True

def main():
	#main window
	window = tk.Tk()
	window.title("Mass Messenger")	

	#making tabs
	tabControl = ttk.Notebook(window)
	email = tk.Frame(tabControl)
	ptext = tk.Frame(tabControl)

	tabControl.add(email, text = 'Mass Email')
	tabControl.add(ptext, text = 'Mass Text')
	tabControl.pack(expand = 1)

	email.columnconfigure((0,5), weight=1)
	email.rowconfigure((0,5),weight=1)

	#filling tabs (email)
	#email frame, from, list of to and login
	fr_email_ft = tk.Frame(email,relief=tk.RAISED,bd=2)
	fr_email_ft.grid(row=0,column=0)

	fr_email_body = tk.Frame(email,relief=tk.RAISED,bd=2)
	fr_email_body.grid(row=1,column=0)
	#from
	tk.Label(fr_email_ft, text="From").grid(row=0,column=0)
	From_Email = tk.Entry(fr_email_ft)
	From_Email.grid(row=0,column=1)
	Login = tk.Button(fr_email_ft,text="Login",command=lambda: email_tools.email_login_gui(From_Email.get())).grid(row=0,column=2)
	#to
	tk.Label(fr_email_ft, text="To").grid(row=0,column=3)
	To_Email = tk.Entry(fr_email_ft)
	To_Email.grid(row=0,column=4)
	#cc
	CC_Email = tk.Text(fr_email_body, width='25')
	CC_Email.grid(row=1,column=1)
	#bcc
	BCC_Email = tk.Text(fr_email_body, width='25')
	BCC_Email.grid(row=1,column=2)

	tk.Label(fr_email_ft, text="Subject").grid(row=0,column=5)
	Subject_Email = tk.Entry(fr_email_ft)
	Subject_Email.grid(row=0,column=6)
	#mass loader from a excel doc
	BCC_Import = tk.Button(fr_email_body, text="BCC Import",command=lambda: bcc_importer('Email')).grid(row=0,column=2)
	CC_Import = tk.Button(fr_email_body, text="CC Import",command=lambda: cc_importer('Email')).grid(row=0,column=1)
	email_txt_edit_label = tk.Label(fr_email_body, text="Message body").grid(column=0, row=0,)
	#message body
	Body_Email= tk.Text(fr_email_body)
	Body_Email.grid(row=1,column=0)

	Send_Button = tk.Button(fr_email_ft, text="Send", command=lambda: email_tools.email_send(To_Email.get(),From_Email.get(), Subject_Email.get(), Body_Email.get("1.0","end-1c"),email_list_create(CC_Email.get("1.0","end-1c")),email_list_create(BCC_Email.get("1.0","end-1c")))).grid(row=0,column=7)



	txt_edit = tk.Text(ptext).grid(column=0, row=0, sticky="nsew")
	window.mainloop()
if __name__ == "__main__":
	main()