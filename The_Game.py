from random import choice
a = 4
b = 0
c = 0
d = 0
e = 0
f = 0
g = 0
h = 0
i = 0
j = 0
k = 0
score = 0

def reset():
    print ("    r) reset easter eggs")
    print ("    b) restart")
    pli = input(">")
    if pli == "r" or pli == "b":
        return pli
    else:
        reset()
def print_location(player_location):
    print ("you are in ")
    print (cave_names[player_location])
    print ("from here you can see")
    neighbors = cave_structure[player_location]
    for tunnel in range(0,3):
        next_cave = neighbors[tunnel]
        print ("   ", tunnel+1, "_", cave_names[next_cave])
    if young_dragon_location in neighbors and c == 0:
       print ("i hear a young dragon")
    if troll_location in neighbors and e == 0:
       print ("i smell a troll")
    if dragon_location in neighbors:
       print ("i smell a dragon")
    if ogre_location in neighbors and d == 0:
        print ("i smell a ogre")
def get_next_location():
    print ("which cave")
    player_input = input(">")
    if player_input in ['1', '2', '3']:
        index = int(player_input) - 1
        neighbors = cave_structure[player_location]
        cave_number = neighbors[index]
        return cave_number
    else:
        print (player_input + "?")
        print ("thats not a direction i know")
        return False
def get_action():
    print ("what do you want to do next")
    print ("    m) move")
    print ("    a) fire an arrow")
    action = input(">")
    if (action == "m" or action == "a" or action == "win" or
        action == "raven" or action == "locations" or
        action == "cheats" or action == "amanda" or action == "hamish"
        or action == "rose"):
        return action
    else:
        print (action + "?")
        print ("thats not a action ive heard of")
        return None
def do_movement():
    print ("moving...")
    new_location = get_next_location()
    if new_location is False:
        return player_location
    else:
        return new_location
def score_print():
    if score == 0:
        print ("well done but the caves are still dangerous")
    if score == 1:
        print ("you have killed the dragon and one more,")
        print ("but others still lie there")
    if score == 2:
        print ("the dragon is dead and most of the other beasts too")
    if score == 3:
        print ("well done mighty dragon hunter")
        print ("because of you it is now safe for")
        print ("everyone to enter the caves")
def do_shooting():
    print ("firing...")
    shoot_at = get_next_location()
    if shoot_at is False:
        return False
    if shoot_at == dragon_location:
        print ("twang, you shot the dragon")
        score_print()        
        return True
    if shoot_at == troll_location and e == 0:
        print ("you shot the troll")
        shots = arrow_count()
        if shots == True:
            return True
        else:
            return troll_location
    if shoot_at == young_dragon_location and c == 0:
        print ("you shot the baby dragon!")
        shots = arrow_count()
        if shots == True:
            return True
        else:
            return young_dragon_location 
    if shoot_at == ogre_location and d == 0:
        print ("you shot the ogre")
        shots = arrow_count()
        if shots == True:
            return True
        else:
            return ogre_location
    else:
        print ("twang, clatter clatter")
        print ("you wasted an arrow")
        shots = arrow_count()
        if shots == True:
            return True
        else:
            return False
def arrow_count():
    arrows = a 
    print ("you have", arrows, "arrows left")
    if arrows == 0:
        print ("you ran out of arrows")
        print ("and return emptyhanded")
        return True
    else:
        return False
def young_dragon():
    if j == 0:
        print ("the baby dragon flies up to you")
        if (c == 0 or d == 0 or e == 0):
            print ("it is giving you a choice")
        print ("     t) have youself transported to the dragon's nieghbors")
        if (c == 0 or d == 0 or e == 0):
            print ("     kc) have one of the lesser beasts killed and the")
            print ("         baby dragon as a companian")
        the_choice3 = input(">")
        return the_choice3
    else:
        return "epic"
def butterfly():
    if f == 0:
        print ("a magical butterfly flew up to you")
        if (c == 0 or d == 0 or e == 0):
            print ("it is giving you a choice")
        print ("     aa) get additional arrows")
        if (c == 0 or d == 0 or e == 0):
            print ("     k) kill one of the lesser beasts")
        the_choice = input(">")
        return the_choice
    else:
        return "try"
def unicorn():
    if g == 0:
        print ("a majestic unicorn runs up to you")
        print ("it is giving you a choice")
        print ("     b) get the locations of the monsters")
        print ("     c) have the unicorn as a companion")
        the_choice2 = input(">")
        return the_choice2
    else:
        return "try2"
def beast_locations():
    print ("dragon:", (cave_names[dragon_location]))
    if c == 0:
        print ("young dragon:", (cave_names[young_dragon_location]))
    if d == 0:
        print ("ogre:", (cave_names[ogre_location]))
    if e == 0:
        print ("troll:", (cave_names[troll_location]))
lesser_beast_numbers2 = range(0,2)
lesser_beast_numbers = range(0,3)
cave_numbers = range(0,20)
unvisited_caves = range(0,20)
visited_caves = []
cave_structure = [
    [18, 1, 5],
    [0, 10, 8],
    [10, 7, 4],
    [5, 4, 6],
    [2, 14, 3],
    [0, 3, 17],
    [11, 3, 12],
    [2, 10, 16],
    [1, 13, 9],
    [11, 8, 13],
    [7, 2, 1],
    [9, 6, 13],
    [6, 15, 19],
    [8, 9, 11],
    [4, 18, 17],
    [12, 16, 17],
    [7, 15, 19],
    [5, 15, 14],
    [14, 19, 0],
    [16, 18, 12]]
cave_names = [
    "golgari layer",
    "death wind caverns",
    "kraken layer",
    "elf ruins",
    "wolfir den",
    "cave of sorrows",
    "drake perches",
    "cave of exile",
    "jarad's tomb",
    "guild pass",
    "demons ravine",
    "rainbow caverns",
    "avenger stronghold",
    "oblivion temple",
    "angels sanctuary",
    "murderous ruin",
    "vampire roost",
    "zombie grave cave",
    "bloody caverns",
    "deadly ruins" ] 
troll_location = choice(cave_numbers)
young_dragon_location = choice(cave_numbers) 
dragon_location = choice(cave_numbers)
player_location = choice(cave_numbers) 
ogre_location = choice(cave_numbers) 
while dragon_location == (troll_location or young_dragon_location or
        ogre_location):
    dragon_location = choice(cave_numbers)
while young_dragon_location == (ogre_location or troll_location or
    dragon_location):
    young_dragon_location = choice(cave_numbers)
while ogre_location == (young_dragon_location or dragon_location or
     troll_location):
    ogre_location = choice(cave_numbers)
while troll_location == (young_dragon_location or troll_location or
    dragon_location):
    troll_location = choice(cave_numbers)
while player_location == (troll_location or dragon_location or
    young_dragon_location or ogre_location):
    player_location == choice(cave_numbers)
print ("welcome to the dragon hunt")
print ("kill the dragon to win")
print ("but beware of the lesser beasts")
print ("you have 5 arrows in your quiver")
print ("""choose the number of the
cave you want to go to next""")
while 1:
    print_location(player_location)
    action = get_action()
    if action is None:
        continue
    if action == "win":
        print ("you got ripped apart, pummeled, disemboweled and")
        print ("eaten by the ogre, young dragon, troll and")
        print ("dragon at the same time you cheater")
        break
    if action == "hamish" and j == 0 and c == 0:
        easter_egg3 = young_dragon()
        if easter_egg3 == "kc":
            c = 1
            k = 1
            score = score + 1
            while j == 0:
                creature_death = choice(lesser_beast_numbers2)
                if creature_death == 0 and d == 0:
                    print ("the young dragon threw a fireball down the caves")
                    print ("and became your companian")
                    print ("later you hear the dieing howl of the ogre")
                    d = 1
                    score = score + 1
                    j = 1
                    break
                if creature_death == 1 and e == 0:
                    print ("the young dragon threw a fireball down the caves")
                    print ("and became your companian")
                    print ("later you hear the dieing wail of the troll")
                    e = 1
                    score = score + 1
                    j = 1
                    break
                else:
                    j = 0
                    f = 1
        if easter_egg3 == "t":
            j = 1
            player_location = choice(cave_structure[dragon_location])
            while player_location == (troll_location or young_dragon_location or
                                      ogre_location):
                choice(cave_structure[dragon_location])
        if easter_egg3 == "james":
            print ("the young dragon smiled and you were transported")
            c = 0
            d = 0
            e = 0
            young_dragon_location = dragon_location
            troll_location = dragon_location
            ogre_location = dragon_location
            player_location = dragon_location
            if player_location == (dragon_location and young_dragon_location
                               and ogre_location and troll_location):
                if i == 0:
                    print ("all the beasts looked down you and smiled,")
                    print ("that was the last thing you ever saw")
                    break
                if i == 1:
                    print ("having the unicorn as a companian proved to")
                    print ("be of no use, the unicorn was ripped apart and")
                    print ("you shortly followed")
                    break
                                                    
    if action == "amanda" and h == 0:
        easter_egg2 = unicorn()
        if easter_egg2 == "b":
            print ("the unicorn burst into flames and")
            print ("spells out the beast's locations")
            h = 1
            beast_locations()
        if easter_egg2 == "c":
            print ("the unicorn bows it's head and")
            print ("promises to help kill one beast")
            h = 1
            i = 1
        if easter_egg2 == "kullen":
            print ("""
fire and rainbows start to dance around the unicorn, growing bigger
and brighter. once they hit you you are instanly transported to the
outside of the caves were you watch all the caves, with the beasts
inside, burn and get destoryed.""")
            break
    if action == "raven" and b == 0:
        easter_egg = butterfly()
        if easter_egg == "aa":
            print ("the butterfly began to glow brightly and")
            print ("became 5 more arrows in you quiver")
            a = a + 5
            b = 1
        while easter_egg == "k" and (c == 0 or d == 0 or e == 0):
            creature_death = choice(lesser_beast_numbers)           
            if creature_death == 0 and c == 0:
                print ("the butterfly burst into a fireball and flew off")
                print ("down the caves")
                print ("later you hear the dieing scream of the young dragon")
                c = 1
                score = score + 1
                b = 1
                break
            if creature_death == 1 and d == 0:
                print ("the butterfly burst into a fireball and flew off")
                print ("down the caves")
                print ("later you hear the dieing howl of the ogre")
                d = 1
                score = score + 1
                b = 1
                break
            if creature_death == 2 and e == 0:
                print ("the butterfly burst into a fireball and flew off")
                print ("down the caves")
                print ("later you hear the dieing wail of the troll")
                e = 1
                score = score + 1
                b = 1
                break
            else:
                b = 0
                f = 1
        if easter_egg == "fire":
            print ("all the beasts are dead but the dragon")
            print ("you gain 5 arrows to your quiver")
            a = a + 5
            b = 1
            if c == 0:
                c = 1
                score = score + 1
            if d == 0:
                d = 1
                score = score + 1
            if e == 0:
                e = 1
                score = score + 1                
    if action == "locations":
        beast_locations()
    if action == "rose":
        epic = reset()
        if epic == "r":
            print ("the easter eggs can be used again")
            b = 0
            h = 0
            j = 0
        elif epic == "b":
            pass
    if action == "cheats":
        print ("""
            locations
            raven
            amanda
            hamish
            win""")
    if action == "m":
        player_location = do_movement()
       
        if player_location == dragon_location and i == 0 and j == 0:
            print ("you got eaten by the dragon")
            break
        if player_location == young_dragon_location and c == 0 and i == 0 and j == 0:
            print ("you got ripped apart by a young dragon")
            break
        if player_location == ogre_location and d == 0 and i == 0 and j == 0:
            print ("you got pummeled by the ogre")
            break
        if player_location == troll_location and e == 0 and i == 0 and j == 0:
            print ("you got disemboweled by the troll")
            break
        if player_location == dragon_location and (i == 1 or j == 1):
            if i == 1 and j == 1:
                print ("the young dragon tries to betray you but the unicorn stops")
                print ("it, sacrificing its life for you. during this confusion you")
                print ("let louse an arrow killing the dragon.")
                score_print()
                break
            elif i == 1:
                print ("the unicorn rushes and kills the dragon before it kills you")
                print ("its work being done it runs off")
                score_print()
                break
            elif j == 1:
                print ("the young dragon joins up with its father and together they")
                print ("burn and rip you apart")
                break
            
        if player_location == young_dragon_location and c == 0 and i == 1 and j == 0:
            print ("the unicorn saves you from the young dragon and kills it")
            print ("its work being done it runs off")
            c = 1
            i = 0
            score = score + 1
        if player_location == ogre_location and d == 0 and (i == 1 or j == 1):
            if i == 1:
                print ("the unicorn kills the ogre as it trys to pumel you")
            if j == 1:
                print ("the dragon burns the ogre to a crisp")
            print ("its work being done it runs off")
            d = 1
            i = 0
            score = score + 1
        if player_location == troll_location and e == 0 and (i == 1 or j == 1):
            if i == 1:
                print ("the unicorn disembowels the troll before it can do the same to you")
            if j == 1:
                print ("the dragon burns the troll to a crisp")
            print ("its work being done it runs off")
            e = 1
            i = 0
            score  = score + 1
    if action == "a":
        end_game = do_shooting()
        if end_game == True:
            break
        elif end_game == ogre_location:
            d = 1
            a = a - 1
            score = score + 1
        elif end_game == young_dragon_location:
            c = 1
            a = a - 1
            score = score + 1
        elif end_game == troll_location:
            e = 1
            a = a - 1
            score = score + 1
        else:
            a = a - 1
