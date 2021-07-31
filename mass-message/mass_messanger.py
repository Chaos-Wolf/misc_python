import tkinter as tk
from tkinter import ttk
import excel_tools
import email_tools
import text_tools

#returns a array of objects that the send function can read
#from the inputs in the email windows, CC, BCC and Text_List
def email_list_create(List):
	x = List.splitlines(False)
	return x

#a overly complicated function that takes the list of recipient objects
#and pulls the unique locations from them and then uses excel_tools.SheetChoice()
#to select which ones to keep on the list
#this is super ineficient and it iterates through the list like 3 times :/
def location_pull(pull):
	choices = []
	for i in pull:
		if len(choices) == 0:
			choices.append(i.location)
		flag = 0
		for x in choices:
			if i.location == x:
				flag = 1
		if flag == 0:
			choices.append(i.location)
	if len(choices) == 1:
		return(pull)
	choice = excel_tools.SheetChoice(choices)
	temp = list(choice)
	final_choice = []
	z = 0
	for j in choices:
		if temp[z] == "x":
			final_choice.append(j)
		z=z+1
	final_pull = []
	for k in pull:
		for l in final_choice:
			if k.location == l:
				final_pull.append(k)
	return(final_pull)

#prompts the user to locate the excel doc they want to import from
#pulls a list of recipient objects from the file using excel_tools.ArrayofObjFromExcel()
#see excel_tools.py documentation for more
#then sends that list through location_pull and returns the final array of objects
def importer():
	filepath = excel_tools.Get_Filepath_Gui("Excel Files","*.xlsx")
	if not filepath:
		return
	first_pull = excel_tools.ArrayofObjFromExcel(filepath)
	pull = location_pull(first_pull)
	return (pull)

#these two functions are identical except for where the final values end up
#they call the above importer function and sort through the list of objects
#they skip each object that doesnt have a email adress and insert the ones that
#do into their respective text boxes
def bcc_importer():
	try:
		pull = importer()
		if not pull:
			return False
		for i in pull:
			if i.email == "NaN":
				continue
			BCC_Email.insert(tk.END, i.email)
			if i != pull[-1]:
				BCC_Email.insert(tk.END, "\n")
		return True
	except Exception as e:
		return False
def cc_importer():
	try:
		pull = importer()
		if not pull:
			return False
		for i in pull:
			if i.email == "NaN":
				continue
			CC_Email.insert(tk.END, i.email)
			if i != pull[-1]:
				CC_Email.insert(tk.END, "\n")
		return True
	except Exception as e:
		return False

#this lets the user select a file using the excel_tools.Get_Filepath_Gui() gui
#then insterts the filepath into the attachments text box
def attachment_import():
	try:
		filepath = excel_tools.Get_Filepath_Gui("All Files","*.*")
		Attachment_Email.insert(tk.END, filepath)
		Attachment_Email.insert(tk.END, "\n")
	except Exception as e:
		return False

#does the same thing as the cc_importer except it parses through the final data and 
#adds carrier suffixes where it can
#if the carrier is not in the dictionary then it will output to the terminal that it is 
#incomplete
#after insuring that each number is correctly formatted it sends it to text_tools.getCarrier()
#to recieve the carrier name and then compares it to the Num_Suf dictionary
#if its in the dictionary it adds the corisponed suffix and adds it to the Text_List textbox
def text_importer():
	Num_Suf = {
		'BELL ATLANTIC NYNEX MOBILE' : '@vtext.com',
		'OMNIPOINT MIAMI E LICENSE, LLC' : '@tmomail.net',
		'NEW CINGULAR WIRELESS PCS, LLC' : '@txt.att.net',
		'UNITED STATES CELLULAR CORP. -' : '@email.uscc.net',
		'SPRINT SPECTRUM L.P.' : '@messaging.sprintpcs.com',
		'CELLCO PARTNERSHIP DBA VERIZON' : '@vtext.com',
		'D&E/OMNIPOINT WIREL JOINT VENT' : '@tmomail.net',
		'METRO PCS, INC.' : '@mymetropcs.com',
		'COMCAST IP PHONE, LLC' : '@vtext.com',
		'POWERTEL NASHVILLE LICENSES, I' : 'tmomail.net'
	}
	try:
		pull = importer()
		if not pull:
			return False
		complete = []
		incomplete = []
		for i in pull:
			if i.number == "NaN":
				continue
			j = str(i.number)
			if j[-2] == ".":
				j = j[:-1]
				j = j[:-1]
			try:
				name = text_tools.getCarrier(j)
				suf = Num_Suf[name]
				j = j + suf
				#print("complete: ",j)
			except:
				incomplete.append(j)
				print(name)
				#print("incomplete: ", j)
				continue
			complete.append(j)
		for k in complete:
			Text_List.insert(tk.END, k)
			if k != pull[-1]:
				Text_List.insert(tk.END, "\n")
		return True
	except Exception as e:
		return False
	
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
CC_Email = tk.Text(fr_email_body, width='30')
CC_Email.grid(row=1,column=2)
#bcc
BCC_Email = tk.Text(fr_email_body, width='30')
BCC_Email.grid(row=1,column=3)

tk.Label(fr_email_ft, text="Subject:").grid(row=0,column=5)
Subject_Email = tk.Entry(fr_email_ft)
Subject_Email.grid(row=0,column=6)
#mass loader from a excel doc
BCC_Import = tk.Button(fr_email_body, text="BCC Import",command=lambda: bcc_importer()).grid(row=0,column=3)
CC_Import = tk.Button(fr_email_body, text="CC Import",command=lambda: cc_importer()).grid(row=0,column=2)
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
fr_text_body = tk.Frame(ptext,relief=tk.RAISED,bd=2)
fr_text_body.grid(row=1,column=0)
#from
tk.Label(fr_text_ft, text="From:").grid(row=0,column=0)
From_Text = tk.Entry(fr_text_ft)
From_Text.grid(row=0,column=1)
#subject
tk.Label(fr_text_ft, text="Subject:").grid(row=0,column=2)
Subject_Text = tk.Entry(fr_text_ft)
Subject_Text.grid(row=0,column=3)
#body
tk.Label(fr_text_body,text="Message body").grid(row=0,column=0)
Text_Body = tk.Text(fr_text_body)
Text_Body.grid(row=1,column=0)
#import recipients
Text_Import = tk.Button(fr_text_body, text="Text Import",command=lambda: text_importer()).grid(row=0,column=1)
#recipients list
Text_List = tk.Text(fr_text_body, width='35')
Text_List.grid(row=1,column=1)
#send text
Send_Text = tk.Button(fr_text_ft, text="Send", command=lambda: email_tools.email_send([],From_Text.get(),Subject_Text.get(),Text_Body.get("1.0","end-1c"),[],[],email_list_create(Text_List.get("1.0","end-1c")))).grid(row=0,column=4)

window.mainloop()
