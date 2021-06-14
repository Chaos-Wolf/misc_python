from tkinter import *
from tkinter import ttk
window = Tk()
window.title("Database")	
window.geometry("750x750")
tabControl = ttk.Notebook(window)
bio1 = ttk.Frame(tabControl)
notes = ttk.Frame(tabControl)
tabControl.add(bio1, text = 'Bio1')
tabControl.add(notes, text = 'Notes')
tabControl.pack(expand = 1, fill="both")
ttk.Label(bio1, text ="Bio Stuff").grid(column = 0, row = 0, padx = 30, pady = 30)
txt_edit = Text(notes).grid(column=0, row=0, sticky="nsew")
window.mainloop()