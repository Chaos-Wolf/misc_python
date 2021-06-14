import pandas 
def ArrayFromExcel(filepath,column):
	data = pandas.read_excel(filepath)
	array = []
	for i in range(data.shape[0]):
		array.append(data.at[i,column])
	return array