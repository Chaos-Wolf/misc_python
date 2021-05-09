import random
import fd
room_names = ["red", "green", "blue", "yellow", "purple", "pink"]
class Room:
	name = "none"
	x = 0
	y = 0
	z = 0
	w = 0
	v = 0
	p = 0
	am = 0
def rand_room():
	room = Room()
	room.name = random.choice(range(10000))#room_names[random.choice(range(len(room_names)))]
	a = random.choice(range(100))
	if a > 74 :
		room.am = "#"
	return(room)
def six_room_fill(x):
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
def six_dim_rooms(h):
	rooms = fd.sdcube(h)
	rooms = six_room_fill(rooms)
	return(rooms)
def print_rooms(x):
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
							print("room",one,two,three,four,five,six,":")
							print("name: ",x[one][two][three][four][five][six].name)
							print("am: ",x[one][two][three][four][five][six].am)
							six=six+1
						five=five+1
					four=four+1
				three=three+1
			two=two+1
		one=one+1
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
def possible(s):
	possible = []
	for a in s:
		for b in a:
			for c in b:
				for d in c:
					for e in d:
						for f in e:
							if f.am == "#":
								possible.append(f)
	return(possible)
def connections(x,poss):
	con = []
	for g in poss:
		if (g.x == x.x or g.x-1 == x.x or g.x+1 == x.x) and (g.y == x.y or g.y-1 == x.y or g.y+1 == x.y) and (g.z == x.z or g.z-1 == x.z or g.z+1 == x.z) and (g.w == x.w or g.w-1 == x.w or g.w+1 == x.w) and (g.v == x.v or g.v-1 == x.v or g.v+1 == x.v) and (g.p == x.p or g.p-1 == x.p or g.p+1 == x.p):
			con.append(g)
	return(con)
def all_con(s):
	them = []
	poss = possible(s)
	for x in poss:
		them.append(connections(x,poss))
	return(them)
def print_con(con):
	for x in con:
		print("[",end="")
		for y in x:
			print(y.name,end=",")
		print("]")
def over_all(h):
	s = six_dim_rooms(h)
	room_map(s)
	final = all_con(s)
	#print_con(final)
	return(final)
def current_loc():
	locs = over_all(3)
	neigh = locs[0]
	n = 0
	for room in neigh:
		print("room",n,":",room.name)
		n=n+1