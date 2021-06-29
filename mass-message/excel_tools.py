import pandas 
import tkinter
from tkinter.filedialog import askopenfilename, asksaveasfilename
def ArrayFromExcel(filepath,column):
	data = pandas.read_excel(filepath)
	data[column] = data[column].fillna("NaN")
	array = []
	for i in range(data.shape[0]):
		if data.at[i,column] == "NaN":
			continue			
		array.append(data.at[i,column])
	return array

def Get_Filepath_Gui(file,ex):
    """Open a file for editing."""
    filepath = askopenfilename(filetypes=[(file, ex)])
    if not filepath:
        return
    return(filepath)

