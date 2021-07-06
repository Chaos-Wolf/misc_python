import random
import threading

#room object defined here
class Room:
	def __init__(self,name,x,y,z,w,v,p):
		self.name = name
		self.x = x
		self.y = y
		self.z = z
		self.w = w
		self.v = v
		self.p = p
		self.loc = 0
		self.neigh_loc = []
		self.am = 0

#creating a random room object and returning it
def rand_room():
	a = random.choice(range(100))
	if a > 74 :
		return("#")
	return(0)

#creating a empty array for the rooms to be housed
#to create a set with less dimentions set the unwanted ones to 1
def empty_room_array(h,wh,l,t,q,p):
	obj = [[[[[[0 for x in range(h)] for y in range(wh)] for z in range(l)] for w in range(t)] for v in range(q)] for b in range(p)]
	return(obj)

#fills a empty 6th dimenstional array with rooms and assigns them a position that
#can be called later
def room_fill(x):
	one=0
	for a in x:
		two=0
		for b in x[one]:
			three=0
			for c in x[one][two]:
				four=0
				for d in x[one][two][three]:	
					five=0
					for e in x[one][two][three][four]:
						six=0
						for f in x[one][two][three][four][five]:
							x[one][two][three][four][five][six] = Room(str(six)+","+str(five)+","+str(four)+","+str(three)+","+str(two)+","+str(one),six,five,four,three,two,one)
							x[one][two][three][four][five][six].am = rand_room()
							six=six+1
						five=five+1
					four=four+1
				three=three+1
			two=two+1
		one=one+1
	return(x)

#a easy way to create cube in any inputed hieght and in different inputted dimenstions
def cube_room_create(h,d):
	r = []
	if d == 2 and h == 20:
		print("engage classic mode")
		cave_names = ["golgari layer","death wind caverns","kraken layer",
					  "elf ruins","wolfir den","cave of sorrows",
					  "drake perches","cave of exile","jarad's tomb",
					  "guild pass","demons ravine","rainbow caverns",
					  "avenger stronghold","oblivion temple","angels sanctuary",
					  "murderous ruin","vampire roost","zombie grave cave",
					  "bloody caverns","deadly ruins" ] 
		for i in range(20):
			room = Room("none",i,i,i,i,i,i)
			room.name = cave_names[i]
			room.loc = i
			r.append(room)
		return(r)
	elif d == 2:
		r = empty_room_array(h,h,1,1,1,1)
	elif d == 3:
		r = empty_room_array(h,h,h,1,1,1)
	elif d == 4:
		r = empty_room_array(h,h,h,h,1,1)
	elif d == 5:
		r = empty_room_array(h,h,h,h,h,1)
	elif d == 6:
		r = empty_room_array(h,h,h,h,h,h)
	else:
		r = empty_room_array(h,h,h,h,h,h)
	r = room_fill(r)
	return(real(r))
#makes a basic map of the array, mostly for debuggin purposes
def room_map(x):
	for a in x:
		for b in a:
			for c in b:
				for e in range(len(c)):
					for d in range(len(c)):
						for f in range(len(c)):
							print("[", end = "")
							print(c[d][e][f].am, end = "")
							print("]", end = "")
						print(" ", end = "")
					print("")
				print("")

#takes a array of rooms and creates a one dimentional array of rooms that exist		
def real(s):
	real = []
	for a in s:
		for b in a:
			for c in b:
				for d in c:
					for e in d:
						for f in e:
							if f.am == "#":
								real.append(f)
	for x in range(len(real)):
		real[x].loc = x
	print(len(real))
	return(real)

#a list of all rooms that are within one space of the inputted room
def connections(x,r):
	con = []
	for g in r:
		if (g.x == x.x or g.x-1 == x.x or g.x+1 == x.x) and (g.y == x.y or g.y-1 == x.y or g.y+1 == x.y) and (g.z == x.z or g.z-1 == x.z or g.z+1 == x.z) and (g.w == x.w or g.w-1 == x.w or g.w+1 == x.w) and (g.v == x.v or g.v-1 == x.v or g.v+1 == x.v) and (g.p == x.p or g.p-1 == x.p or g.p+1 == x.p):
			con.append(g.loc)
	return(con) 

#same as above but is able to define how many dimensions of travel is allowed
def con(x,c,d,r):
	con = []
	for g in c:
		dif = 0
		if r[g].x != x.x:
			dif+=1
		if r[g].y != x.y:
			dif+=1
		if r[g].z != x.z:
			dif+=1
		if r[g].w != x.w:
			dif+=1
		if r[g].v != x.v:
			dif+=1
		if r[g].p != x.p:
			dif+=1
		if dif <= d and dif > 0:
			con.append(g)
	return(con)
def thread_con(r):
	them = []
	for x in r:
		them.append(connections(x,r))
	return(them)
#returns a list of all connections for each room
def all_con(r):
	div_val = 4
	div = len(r)//div_val
	split_list = []
	them = []*div_val
	for i in range(div_val):
		temp_list = []
		for x in range((div * i),(div+(div*i))):
			temp_list.append(r[x])
		if i == (div_val-1):
			for y in range(div_val*div,len(r)):
				temp_list.append(r[y])
		split_list.append(temp_list)
	thread_list=[]
	for j in range(div_val):
		thread = threading.Thread(target=thread_con, args=(split_list[j]))
		thread.start()
		thread_list.append(thread)
	for k in range(div_val):
		print(thread_list[k].join())
	return(them)

#a print tool for two dimentions
#currently used to print a list of every connection for each room
def print_con(con):
	for x in con:
		print("[",end="")
		for y in x:
			print(y.name,end=",")
		print("]")
		
#a print tool for one dimention
def print_test(c):
	print("[", end="")
	for x in c:
		print(x.name,end=", ")
	print("]")
	
# a function to test the various parts
def test():
	s = empty_room_array(3,3,3,3,3,3)
	s = room_fill(s)
	room_map(s)
	r = real(s)
	c = all_first_con(r)
	pos = 0
	for a in r:
		print(a.name,end=": [")
		for b in c[pos]:
			print(b.name,end=", ")
		print("]")
		pos+=1
	