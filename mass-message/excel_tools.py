import pandas 
import tkinter
from tkinter.filedialog	import askopenfilename,	asksaveasfilename

#a object for each recipient that holds their name, location, employer, cell number, and email
#also has a nice premade output if it is printed
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

######################################################
#block of Functions for importing from a excel doc   #
#go to ArrayofObjFromExcel first and work your way up#
######################################################

#the function behind the each of the choice buttons
#it takes itself as a varible and changes the text
#to the oppisite of what it was
def	Toggle(but):
	if but.config('text')[-1] == "True":
		but.config(text="False")
	else:
		but.config(text="True")

#the function for the all button
#if anything is false it is flipped to true
#if everything is true they are all flipped to false
#takes a list of buttons
def Select_All(buttons):
	trues = 0
	for i in buttons:
		if i.config('text')[-1] == "True":
			trues = trues + 1
	if trues == len(buttons):
		for i in buttons:
			i.config(text="False")
		return(False)
	for i in buttons:
		if i.config('text')[-1] == "False":
			i.config(text="True")

#the import function for SheetChoice
#takes a list of buttons and reads their text
#returns x for true and o for false
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

#this takes a list of sheets (or locations) and presents them as a list of options
#each button is a toggle and once the user hits Import a code is send back where 
#o means that sheet will not be imported and x means it will
def	SheetChoice(sheets):
	sheet_window= tkinter.Tk()
	i = 0
	but_list = []
	var = { 'value': "" }
	def inner_work_around():
		var['value'] = pull_buttons(but_list)
		sheet_window.destroy()
	for x in sheets:
		but_list.append(tkinter.Button(sheet_window,width=12))
		but_list[i].config(text="False", command=lambda j=i: Toggle(but_list[j]))
		but_list[i].grid(row=1,column=i)
		tkinter.Label(sheet_window,text=x).grid(row=0,column=i)
		i = i	+ 1
	all_but = tkinter.Button(sheet_window,width=12,text="All",command=lambda:Select_All(but_list))
	all_but.grid(row=2,column=i//2)
	import_sheets = tkinter.Button(sheet_window,width=12,text="Import",command=lambda:inner_work_around())
	import_sheets.grid(row=3,column=i//2)
	sheet_window.wait_window()
	return(var['value'])

#collects the filepath of the excel doc
#imports the data then parses it for a list of sheets
#this list is then sent to Sheet choice and a code is given back
#it is parsed into its own array and compared to the list of sheets
#the final list of sheets is gone through and imports each row as a recipient object
#this list of objects is returned to user
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

############################################################
#a outdated function that takes both the filepath and the column name
#and returns a array of each item in that column
def	ArrayFromExcel(filepath,column):
	data =	pandas.read_excel(filepath)
	data[column] =	data[column].fillna("NaN")
	array = []
	for i in range(data.shape[0]):
		if data.at[i,column] == "NaN":
			continue			
		array.append(data.at[i,column])
	return	array
############################################################

#a user friendly way to locate and return the filepath of a excel doc
def	Get_Filepath_Gui(file,ex):
	"""Open a file	for	editing."""
	filepath =	askopenfilename(filetypes=[(file, ex)])
	if	not	filepath:
		return
	return(filepath)

