import pandas 
import tkinter
from tkinter.filedialog	import askopenfilename,	asksaveasfilename
class Recipient:
	def __init__(self,first,last,employer,location,number,email):
		self.first = first
		self.last	= last
		self.employer	= employer
		self.location	= location
		self.number =	number
		self.email = email
	def __str__(self):
		return(self.first	+ "	" +	self.last +	"\nEmployer: " + self.employer + "\nLocation: "	+ self.location	+ "\nCell Number: "	+ str(self.number) + "\nEmail: " +self.email + "\n")
def	Toggle(but):
	if but.config('text')[-1] == "True":
		but.config(text="False")
	else:
		but.config(text="True")

def Select_All(buttons):
	for i in buttons:
		if i.config('text')[-1] == "False":
			i.config(text="True")
def pull_buttons(buttons):
	i = 0
	final = ""
	for x in buttons:
		if x.config('text')[-1] == "True":
			final = final + "x"
		else:
			final = final + "o"
		i=i+1
	return(final)

def	SheetChoice(sheets):
	sheet_window= tkinter.Tk()
	#button_frame =	tkinter.Frame(sheet_window)
	#button_frame.grid(row=0,column=0)
	i = 0
	but_list = []
	var = { 'value': "" }
	def inner_work_around():
		var['value'] = pull_buttons(but_list)
		sheet_window.destroy()
	for x in sheets:
		but_list.append(tkinter.Button(sheet_window,width=12))
		but_list[i].config(text="True", command=lambda j=i: Toggle(but_list[j]))
		but_list[i].grid(row=1,column=i)
		tkinter.Label(sheet_window,text=x).grid(row=0,column=i)
		i = i	+ 1
	all_but = tkinter.Button(sheet_window,width=12,text="All",command=lambda:Select_All(but_list))
	all_but.grid(row=2,column=i//2)
	import_sheets = tkinter.Button(sheet_window,width=12,text="Import",command=lambda:inner_work_around())
	import_sheets.grid(row=3,column=i//2)
	sheet_window.wait_window()
	return(var['value'])

def	ArrayofObjFromExcel(filepath):
	whole_data	= pandas.read_excel(filepath, None)
	raw_sheets	= whole_data.keys()
	sheet_cheat	= SheetChoice(raw_sheets)
	temp = list(sheet_cheat)
	sheets = []
	z = 0
	for y in raw_sheets:
		if temp[z] == "x":
			sheets.append(y)
		z=z+1
	array = []
	for x in sheets:
		raw_data = pandas.read_excel(filepath, x)
		raw_data = raw_data.fillna("NaN")
		for i in range(raw_data.shape[0]):
			recip = Recipient(raw_data.at[i,"First Name"], raw_data.at[i,"Last Name"], raw_data.at[i,"Employer"], raw_data.at[i,"City/Town of Employment"], raw_data.at[i,"Cell Number"],raw_data.at[i,"Email"])
			array.append(recip)
	return(array)

def	ArrayFromExcel(filepath,column):
	data =	pandas.read_excel(filepath)
	data[column] =	data[column].fillna("NaN")
	array = []
	for i in range(data.shape[0]):
		if data.at[i,column] == "NaN":
			continue			
		array.append(data.at[i,column])
	return	array

def	Get_Filepath_Gui(file,ex):
	"""Open a file	for	editing."""
	filepath =	askopenfilename(filetypes=[(file, ex)])
	if	not	filepath:
		return
	return(filepath)

