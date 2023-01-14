import d
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import csv
import math
def pre_test():
	ploting(instance(d.coin,1000000,4))
	ploting(instance(d.d4,1000000,4))
	ploting(instance(d.d6,1000000,4))
	ploting(instance(d.d8,1000000,4))	
	ploting(instance(d.d10,1000000,4))
	ploting(instance(d.d12,1000000,4))
	ploting(instance(d.d20,1000000,4))
	ploting(instance(d.d100,1000000,4))
def instance(die,times,die_amount):
	list_of_values = []
	for j in range(die_amount):
		temp_list_of_values = []
		for x in range(die.value*(j+1)):
			temp_list_of_values.append(0)
		for i in range(times):
			temp_list_of_values[die.rs(j+1)-1]+=1
		list_of_values.append(temp_list_of_values)
	return(list_of_values)
def ploting(die_values):
	fig = plt.figure()
	for j in range(len(die_values)):
		plt.plot(die_values[j])
	plt.grid()
	plt.show()
