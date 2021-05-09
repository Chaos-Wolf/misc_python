import random
from random import choice
game_intro = 1
game_start_run = 1
items = []
player_helth = 30
intro = 1
pllo = 0
area = 1
e = 0
doga = range(50)
questlog = ["you have no quests"]
cquest = []
quest1 = "investigate the creepy shack"
subquest1 = "find the key to the creepy shack"
weapons = ['shovel',
           'dead squirel',
           'spoon',
           'knife',
           'rusted sword',
           'candy necklace']
bartender = """im sure you've seen the creepy shack across
the road, it tends to scare away customers. unfortunally
its locked and there seems to be no other way inside"""
james = """i raise my glass to you fellow, you're here
to save use right....from what you ask why from drink"""
lynn = "............... burp"
crazy_old_man = "HERE TAKE THE KEY, I DONT WANT IT, THE SHACK....THE KEY....THE SHACK"
people = ['bartender',
          'james',
          'lynn']
storei = ['bread',
          'fish',
          'sugar',
          'flour',
          'eggs',
          'butterknife',
          'pan',
          'holy water',
          'clothes']
town_buildings = [
    "general store",
    "black smith",
    "the notsennep's house",
    "mayor's house",
    "glenn's house",
    "oswell's house",
    "drunken inn",
    "creepy shack",
    "main street",
    "town exit"]
town_layout = [
    [0, 2, 9, 8],
    [1, 4, 8, 8],
    [5, 6, 8, 8],
    [3, 7, 8, 9]]
def generalstore():
    print ("do you wish to buy or talk?")
    while True:
        print ("    b) buy")
        print ("    t) talk")
        print ("    l) leave") 
        global storei
        global items
        choice1 = input(">")
        if choice1 == "b" or choice1 == "buy":
            print (storei)
            print ("choose one")
            print ("its all free")
            print ("    l) leave")
            while True:
                if len(storei) == 0:
                    print ("there is nothing left")
                    break
                c = input(">")
                if c in storei:
                    print ("you now have", c)
                    storei.remove(c)
                    items.append(c)
                    print ("there is now", storei)
                elif c == "l" or c == "leave":
                    print ("good bye")
                    break
                else:
                    print ("we do not have that")
                    True
        elif choice1 == "t" or choice1 == "talk":
            print ("there is noone to talk to")
            print ("do you wish to leave?")
            print ("    y) yes")
            print ("    n) no")
            b = input(">")
            if b == "y" or b == "yes":
                print ("good bye")
                break
            elif b == "n" or b == "no":
                print ("alright")
                True
            else:
                print ("that is neither yes nor no")
                True
        elif choice1 == "l" or choice1 == "leave":
            print ("good bye")
            break
        else:
            print ("that is not a action")
            True
def inn():
    global people
    global items
    print ("people are here to talk to")
    print (people)
    print ("    l) leave")
    while True:
        v = input(">")
        if v in people:
            print ("you are talking to", v)                
            if v == people[0]:
                print (bartender)
                if quest1 not in questlog:
                    questlog.clear()
                    questlog.append(quest1)
                    print ("added quest")
                    print (quest1)
            elif v == people[1]:
                print (james)
            elif v == people[2]:
                print (lynn)
        elif v == "l" or v == "leave":
            break
        else:
            print ("there is noone in here by that name")
def houses():
    if e == 2 or e == 3 or e == 4 or e == 5:
        print ("the door is locked and breaking in is rude")
        crazy = random.randrange(2,6)
        if e == crazy:
            print ("there is a creepy old man outside")
            print ("do you wish to talk to him")
            print ("    y) yes")
            print ("    n) no")
            while True:
                f = input(">")
                if f ==  "y" or f == "yes":
                    if quest1 in questlog and 'key1' not in items :
                        print (crazy_old_man)
                        items.append('key1')
                        print ("key added")
                        break
                    else:
                        print (".................")
                        break
                elif f == "n" or f == "no":
                    print ("alright")
                    break
                else:
                    print ("that is neither yes nor no")
                    True                        
    elif e == 0:
        print ("do you wish to enter?")
        print ("    y) yes")
        print ("    n) no")
        while True:
            choice1 = input(">")
            if choice1 == "y" or choice1 == "yes":
                generalstore()
                break
            elif choice1 == "n" or choice1 == "no":
                break
            else:
                True
    elif e == 7:
        if "key1" in items:
            print ("do you wish to use the key to enter?")
            print ("    y) yes")
            print ("    n) no")
            while True:
                choice1 = input(">")
                if choice1 == "y" or choice1 == "yes":
                    print ("you enter the dungeon")
                    print ("quests completed")
                    cquest.append(quest1)
                    questlog.clear()
                    global game_start_run
                    game_start_run = 1
                    break
                elif choice1 == "n" or choice1 == "no":
                    break
                else:
                    True
        else:
            print ("the door is locked and requires a key to enter")
            if subquest1 not in questlog and quest1 in questlog:
                questlog.append(subquest1)
                print ("find the key")
            
    elif e == 1:
        print ("the black smith's shop is closed")
        if len(weapons) > 0:
            print ("but you find a box of assorted items that")
            print ("say 'free please take'")
            print (weapons)
            print ("    l) leave")
            while True:
                if len(weapons) == 0:
                    print ("there are none left")
                    break
                choice1 = input(">")
                if choice1 in weapons:
                    print ("you now have", choice1) 
                    weapons.remove(choice1)
                    items.append(choice1)
                elif choice1 == "l" or choice1 == "leave":
                    print ("goodbye")
                    break
                else:
                    print ("thats not there, youre drunk")
                    True
    elif e == 6:
        print ("do you wish to enter")
        print ("    y) yes")
        print ("    n) no")
        while True:
            choice1 = input(">")
            if choice1 == "y" or choice1 == "yes":
                inn()
                break
            elif choice1 == "n" or choice1 == "no":
                break
            else:
                True 
                
    else:
        print ("fuck")
def controls():
    print ("controls")
    print ("    m) move")
    print ("    i) inventory")
    print ("    q) quest log")
def buildings2():
    list2 = []
    list1 = []
    sight = town_layout[pllo]
    for line in range(0, 4):
        next_place = sight[line]
        list2.append(town_buildings[next_place])
        list1.append(next_place)
    global e
    e = list1[1]
    print ("you walk up to the", list2[1])
    houses()
def buildings1():
    list2 = []
    list1 = []
    sight = town_layout[pllo]
    for line in range(0, 4):
        next_place = sight[line]
        list1.append(town_buildings[next_place])
        list2.append(next_place)
    global e
    e = list2[0]
    print ("you walk up to the", list1[0])
    houses() 
def move():
    print ("    r) right")
    print ("    l) left")
    print ("    b) back")
    print ("    f) forward")
    movement = input(">")
    if movement == "r" or movement == "right":
        buildings1()
        return movement
    if movement == "l" or movement == "left":
        buildings2()
        return movement
    elif (movement == "f" or movement == "b" or movement == "back" 
    or movement == "forward"):
        print ("you are walking alittle bit")  
        return movement
    else:
        move()
def inventory():
    print ("you have...")
    print (items)
    print
def location():
    if pllo == 0 or pllo == 1 or pllo == 2 or pllo == 3:
        list1 = []
        print ("you are on a street")
        sight = town_layout[pllo]
        for line in range(0, 4):
            next_place = sight[line]
            list1.append(town_buildings[next_place])
        print ("to your right is the", list1[0])
        print ("to your left is the", list1[1])
        print ("behind you is the", list1[2])
        print ("and infront of you is the", list1[3])
        return pllo
    elif pllo > 3 or pllo < 0:
        print ("you encounter the exit")
        print ("are you sure you want to leave")
        print ("    y) yes")
        print ("    n) no")
        while True:
            desition = input(">")
            if desition == "y" or desition == "yes":
                print ("good bye")
                return "death"
            elif desition == "n" or desition == "no":
                return pllo
            else:
                print ("i didnt hear you")
    else:
        print ("shit")
print ("welcome to crazy town") 
print ("this is a fucked up town")
print ("full of insane people")
print ("welcome again")
print ("...............")
print ("please respond")
print ("please...please, will you help us") 
while game_intro == 1:
    print ("    y) yes")
    print ("    n) no")
    response = input(">")
    if response == "n" or response == "N" or response == "no":
        print ("you walk away bored and die of")
        print ("thirst in the virtual desert")
        game_intro = 0
        intro = 0
    elif response == "y" or response == "Y" or response == "yes":
        print ("yay now you can help us")
        game_start_run = 0
        game_intro = 0
    elif response == "fuck you":
        print ("why are you so mean sir, is that a no or yes")
        game_intro = 1
    else:
        print ("that is neither yes or no, what is your anwser")
        game_intro = 1
while intro == 1:
    print ("quick game control intro")
    print ("    m) move")
    print ("    i) inventory")
    print ("    q) quest log")
    intro = 0
while game_start_run == 0:
    l = location()
    if l == "death":
        
        break
    if pllo < 0:
        pllo = pllo + 1
        location()
    if pllo > 3:
        pllo = pllo - 1
        location()
    print ("what would you like to do")
    desision = input(">")
    if desision == "q" or desision == "quest log":
        print(questlog)
    elif desision == "m" or desision == "move":
        #e = choice(doga)
        if e == 45:
            attack()
        m = move()
        if m == "f" or m == "forward":
            pllo = pllo + 1
        if m == "b" or m == "back":
            pllo = pllo - 1
    elif desision == "i" or desision == "inventory" or desision == "items":
        i = inventory()
    elif desision == "end": #remeber to take this out later
        break
    elif desision == "help":
        controls()
    else:
        print ("thats not a option")
    
    
