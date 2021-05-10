import random

#room object defined here
class Room:
	name = "none"
	x = 0
	y = 0
	z = 0
	w = 0
	v = 0
	p = 0
	loc = 0
	am = 0

#creating a random room object and returning it
def rand_room():
	room = Room()
	a = random.choice(range(100))
	if a > 74 :
		room.am = "#"
	return(room)

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
							x[one][two][three][four][five][six] = rand_room()
							x[one][two][three][four][five][six].name = str(six)+str(five)+str(four)+str(three)+str(two)+str(one)
							x[one][two][three][four][five][six].x = six
							x[one][two][three][four][five][six].y = five
							x[one][two][three][four][five][six].z = four
							x[one][two][three][four][five][six].w = three
							x[one][two][three][four][five][six].v = two
							x[one][two][three][four][five][six].p = one
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
	if d == 2:
		print("engage classic mode")
		cave_names = ["golgari layer","death wind caverns","kraken layer",
					  "elf ruins","wolfir den","cave of sorrows",
					  "drake perches","cave of exile","jarad's tomb",
					  "guild pass","demons ravine","rainbow caverns",
					  "avenger stronghold","oblivion temple","angels sanctuary",
					  "murderous ruin","vampire roost","zombie grave cave",
					  "bloody caverns","deadly ruins" ] 
		for i in range(20):
			room = Room()
			room.name = cave_names[i]
			room.loc = i
			r.append(room)
		return(r)
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
	return(real)

#a list of all rooms that are within one space of the inputted room
def connections(x,r):
	con = []
	for g in r:
		if (g.x == x.x or g.x-1 == x.x or g.x+1 == x.x) and (g.y == x.y or g.y-1 == x.y or g.y+1 == x.y) and (g.z == x.z or g.z-1 == x.z or g.z+1 == x.z) and (g.w == x.w or g.w-1 == x.w or g.w+1 == x.w) and (g.v == x.v or g.v-1 == x.v or g.v+1 == x.v) and (g.p == x.p or g.p-1 == x.p or g.p+1 == x.p):
			con.append(g)
	return(con) 

#same as above but is able to define how many dimensions of travel is allowed
def con(x,c,d):
	con = []
	for g in c:
		dif = 0
		if g.x != x.x:
			dif+=1
		if g.y != x.y:
			dif+=1
		if g.z != x.z:
			dif+=1
		if g.w != x.w:
			dif+=1
		if g.v != x.v:
			dif+=1
		if g.p != x.p:
			dif+=1
		if dif <= d and dif > 0:
			con.append(g)
	return(con)

#returns a list of all connections for each room
def all_con(r):
	them = []
	for x in r:
		them.append(connections(x,r))
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
	