import d
import numpy as np
import matplotlib.pyplot as plt
def tracy_test(n):
	td6 = 0
	td6l = 0
	total_list=[[0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0]]
	num_times = n
	fd6 = 0
	fd6l = 0
	for i in range(num_times):
		temp =[]
		for x in range(3):
			temp.append(d.d6.r())
	#	print(temp)
		temp = sorted(temp)
	#	print(temp[2])
		total_list[0][temp[1] + temp[2]] = total_list[0][temp[1] + temp[2]] + 1
		total_list[1][temp[0] + temp[1]] = total_list[1][temp[0] + temp[1]] + 1
		td6 = td6 + temp[1] + temp[2]
		td6l = td6l + temp[0] + temp[1]
	av3d6 = td6/num_times
	av3d6l = td6l/num_times
	print(av3d6)
	print(av3d6l)
	for i in range(num_times):
		temp1=[]
		for x in range(2):
			temp1.append(d.d6.rs(2))
	#	print(temp1)
		temp1 = sorted(temp1)
	#	print(temp1[1])
		total_list[2][temp1[1]] = total_list[2][temp1[1]] + 1
		total_list[3][temp1[0]] = total_list[3][temp1[0]] + 1
		fd6 = fd6 + temp1[1]
		fd6l = fd6l + temp1[0]
	av4d6 = fd6/num_times
	av4d6l = fd6l/num_times
	print(av4d6)
	print(av4d6l)
	print(total_list)
	x = [0,1,2,3,4,5,6,7,8,9,10,11,12]
	plt.plot(x,total_list[0],label = 'high 3d6')
	plt.plot(x,total_list[1],label = 'low 3d6')
	plt.plot(x,total_list[2],label = 'high 4d6')
	plt.plot(x,total_list[3],label = 'low 4d6')
	plt.legend(loc=2)
	plt.show()