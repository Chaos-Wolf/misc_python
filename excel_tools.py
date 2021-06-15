import pandas 
import tkinter
from tkinter.filedialog import askopenfilename, asksaveasfilename
def ArrayFromExcel(filepath,column):
	data = pandas.read_excel(filepath)
	array = []
	for i in range(data.shape[0]):
		array.append(data.at[i,column])
	return array

def Get_Filepath_Gui():
    """Open a file for editing."""
    filepath = askopenfilename(filetypes=[("Excel Files", "*.xlsx"), ("All Files", "*.*")])
    if not filepath:
        return
    return(filepath)

