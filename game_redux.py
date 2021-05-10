import random
import room_map
rooms = []
structure = []
creatures = []
classic_mode = 0
actions_call = ['i','a','end']
actions_obj = []

#creates object classed for items (weapons and ranged weapons)
#and creatures (includes the character
class actions(object):
	def __init__(self,name,fun):
		self.name = name
		self.fun = fun
	def do(self):
		self.fun()
class weapon(object):
	def __init__(self,name,damage,bonus,des,kill_des):
		self.name = name
		self.damage = damage
		self.bonus = bonus
		self.des = des
		self.kill_des = kill_des
class ranged_weapon( weapon ):
	def __init__(self,name,damage,bonus,des,kill_des,ammo):
		self.ammo = ammo
		weapon.__init__(self,name,damage,bonus,des,kill_des)
class creature(object):
	def __init__(self,name,loc,ac,hp,attack,move_freedom):
		self.name = name
		self.loc = loc
		self.ac = ac
		self.hp = hp
		self.attack = attack
		self.move_freedom = move_freedom
		self.weapons = []
		self.near_des = ''

#check if the inputs are valid
def valid(user_in, valid_min,valid_max):
	for i in range(len(actions_call)):
			if user_in == actions_call[i]:
				actions_obj[i].do()
				return(1)
	try: 
		int(user_in)
	except ValueError:
		print("invalid input")
		return(1)
	if int(user_in) >= valid_min and int(user_in) < valid_max:
		return(0)
	else:
		print("invalid input")
		return(1)
	
#grabs the current location and returns a array of options based off
#the creatures movement
def current_loc_silent(x):
	neighbors = structure[x.loc]
	global classic_mode
	if classic_mode == 1:
		return(neighbors)
	movement = room_map.con(rooms[x.loc],neighbors,x.move_freedom)
	return(movement)

#outputs the neighboring rooms to the display
def current_loc(x):
	print(x.name,"are in ")
	print(rooms[x.loc].name)
	print("from here",x.name,"can see")
	movement = current_loc_silent(x)
	entry = 0
	for a in movement:
		print ("   ", entry, "", a.name)
		entry+=1
	return(len(movement))
def inventory():
	print("inventroy")
def attack():
	print("attack")
	
def end():
	a = input("Do you wish to restart? (y/n): ")
	if a == 'y':
		start()
	if a == 'n':
		print("GG")
		exit()
	else:
		restart()
#function the starts at the beginning of the game
#and sets up the room dimentions 
def intro():
	print("Welcome to the Game Redux!!")
	print("Please choose a game size")
	h = input("Game Height:")
	while valid(h,1,100) == 1:
		h = input("Game Height:")
	d = input("Dimention Number:")
	while valid(d,1,100) == 1:
		d = input("Dimention Number:")
	h = int(h)
	d = int(d)
	if h == 20 and d == 2:
		global classic_mode
		classic_mode = 1
	print("One moment as the playfield is made")
	global rooms 
	rooms = room_map.cube_room_create(abs(h),abs(d))
	print("Rooms created, now mapping connections")
	global structure
	if classic_mode == 1:
		structure = [[rooms[18],rooms[1],rooms[5]],[rooms[0],rooms[10],rooms[8]],[rooms[10],rooms[7],rooms[4]],
					[rooms[5],rooms[4],rooms[6]],[rooms[2],rooms[14],rooms[3]],[rooms[0],rooms[3],rooms[17]],
					[rooms[11],rooms[3],rooms[12]],[rooms[2],rooms[10],rooms[16]],[rooms[1],rooms[13],rooms[9]],
					[rooms[11],rooms[8],rooms[13]],[rooms[7],rooms[2],rooms[1]],[rooms[9],rooms[6],rooms[13]],
					[rooms[6],rooms[15],rooms[19]],[rooms[8],rooms[9],rooms[11]],[rooms[4],rooms[18],rooms[17]],
					[rooms[12],rooms[16],rooms[17]],[rooms[7],rooms[15],rooms[19]],[rooms[5],rooms[15],rooms[14]],
					[rooms[14],rooms[19],rooms[0]],[rooms[16],rooms[18],rooms[12]]]
	else:
		structure = room_map.all_con(rooms)
		
#creates the local object classes
#starts after intro()
def setup():
	dragon = creature("dragon",1,20,10,6,6)
	player = creature("you",0,10,1,3,3)
	player.weapons.append(weapon('sword',2,0,'sliced','disenbowled'))
	player.weapons.append(ranged_weapon('bow',1,1,'shot','impaled',10))
	dragon.weapons.append(weapon('claws',2,0,'gouged','disenbowled'))
	dragon.weapons.append(weapon('fire',4,-2,'burned','incinerated'))
	dragon.weapons.append(weapon('tail',3,-1,'hit','crushed'))
	dragon.near_des = 'It becomes swelteringly hot as deafing breaths vibrate the chamber'
	creatures.append(player)
	creatures.append(dragon)
	actions_obj.append(actions('i',inventory))
	actions_obj.append(actions('a',attack))
	actions_obj.append(actions('end',end))

#takes the next room the player wants to go to and changes
#its .loc trait
def move(x, v):
	pos = current_loc_silent(x)
	new = input("next location: ")
	while valid(new,0,v) == 1:
		new = input("next location: ")
	new = int(new)
	x.loc = pos[int(new)].loc
	
#the fight logic
#takes the player (x) and the monster (y)
def fight(x, y):
	print("you have encountered a",y.name)
	while y.hp > 0 and x.hp > 0:
		print("your weapons are:")
		num = 0
		for i in x.weapons:
			print(num,":", i.name)
			num+=1
		print(num,": flee")
		a = input(">")
		while valid(a,0,num) == 1:
			a = input(">")
		a = int(a)
		if a == num:
			  neigh = current_loc_silent(x)
			  ran_dir = random.choice(range(len(neigh)))
			  x.loc = neigh[ran_dir].loc
			  main()
		attack = random.choice(range(1,21))+x.weapons[a].bonus+x.attack
		if attack >= y.ac:
			print("you have",x.weapons[a].des,"the", y.name)
			y.hp = y.hp - x.weapons[a].damage
		else:
			print("your",x.weapons[a].name,"has missed the",y.name)
		if y.hp >0:
			attack_choice = random.choice(range(len(y.weapons)))
			attack_mon = random.choice(range(1,21))+y.weapons[attack_choice].bonus+y.attack
			if attack_mon >= x.ac:
				print("the",y.name,y.weapons[attack_choice].des,"you with",y.weapons[attack_choice].name)
				x.hp = x.hp - y.weapons[attack_choice].damage
			else:
				print("you barley dodged the",y.name,"'s",y.weapons[attack_choice].name)
	if y.hp <= 0:
		print("you have",x.weapons[a].kill_des,"the",y.name)
	if x.hp <= 0:
		print("you have been",y.weapons[attack_choice].kill_des,"by the",y.name)

def mon_move():
	for i in creatures:
		if i.name == 'you':
			continue
		else:
			next = current_loc_silent(i)
			direction = random.choice(range(len(next)))
			i.loc = next[direction].loc
def check_neigh(x):
	for i in x:
		for j in creatures:
			if j.name == 'you':
				continue
			else:
				if j.loc == i.loc:
					print(j.near_des)
# the main loop
def main():
	char_move = 0
	while creatures[0].loc != creatures[1].loc:
		valid = current_loc(creatures[0])
		if char_move == 2:
			mon_move()
		else:
			char_move += 1
		neigh = current_loc_silent(creatures[0])
		check_neigh(neigh)
		move(creatures[0], valid)
		
	fight(creatures[0],creatures[1])
	end()
def start():
	global rooms
	rooms = []
	global structure 
	structure = []
	global creatures 
	creatures = []
	global classic_mode 
	classic_mode = 0
	intro()
	setup()
	main()
start()