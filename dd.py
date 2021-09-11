def Order(n):
	import random
	order = []
	for i in range(n):
		order.append(i+1)
	for x in range(n):
		ran = len(order)
		num = random.choice(range(ran))
		print(order[num])
		del order[num]
def planes(n):
    from random import choice
    plane=["|Mount Celestia|", "|Bytopia       |", "|Elysium       |",
           "|The Beastlands|", "|Arborea       |", "|Ysgard        |",
           "|Limbo         |", "|Pandemonium   |", "|The Abyss     |",
           "|Carceri       |", "|Hades         |", "|Gehenna       |",
           "|The Nine Hells|", "|Archeron      |", "|Mechanus      |",
           "|Arcadia       |", "|Plane of Fire |", "|Plane of Air  |",
           "|Plane of Earth|", "|Plane of Water|", "|Shadowfell    |",
           "|Feywild       |", "|Etherial      |", "|Astral        |",
           "|Outlands      |", "|Sigil         |", "|Seruatis      |",
           "|Deorum        |", "|Mortuorum     |", "|Periculosus   |",
           "|Fluctus       |", "|Sensus        |", "|Aeternum      |",
           "|Expertes      |"]
    ran=range(0,34)
    picks=[]
    pre=27
    for i in range(n):
        num=choice(ran)
        while True:
            if num != pre:
                pre=num
                break
            else:
                num=choice(ran)                
        picks.append(num)
    print("----------------")
    for y in range(n):
        print(plane[picks[y]])
    print("----------------")
def cg():
    from random import choice
    plane=["|Mount Celestia|", "|Bytopia       |", "|Elysium       |",
           "|The Beastlands|", "|Arborea       |", "|Ysgard        |",
           "|Limbo         |", "|Pandemonium   |", "|The Abyss     |",
           "|Carceri       |", "|Hades         |", "|Gehenna       |",
           "|The Nine Hells|", "|Archeron      |", "|Mechanus      |",
           "|Arcadia       |", "|Plane of Fire |", "|Plane of Air  |",
           "|Plane of Earth|", "|Plane of Water|", "|Shadowfell    |",
           "|Feywild       |", "|Etherial      |", "|Astral        |",
           "|Outlands      |", "|Sigil         |"]
    picks=[]
    ran=range(0,26)
    for i in range(5):
        num=choice(ran)
        #print("num ",num)
        while True:
            flag=0
            if i >= 1:
                for x in range(i):
                    if num == picks[x]:
                        flag=1
                        #print("flag")
            if flag==0:
                picks.append(num)
                #print("pick ", num)
                break
            else:
                num=choice(ran)
                #print("retry ",num)
    print("|Material Plane|")
    for y in range(5):
        print(plane[picks[y]])
def cgs(n):
    for i in range(n):
        print("Box: ",i+1)
        print("----------------")
        cg()
        print("----------------")
def roll(s):
    from random import choice
    ran=range(1,(s+1))
    num=choice(ran)
    return num
def rolls(s,t):
    total = 0
    for i in range(t):
        total = total + roll(s)
    return total
def vfr(a):
    a8 =0
    a9=0
    a10=0
    a11=0
    a12=0
    a13=0
    a14=0
    a15=0
    a16=0
    a17=0
    a18=0
    for i in range(a):
        y = roll(6)
        x = roll(6)
        t = x+y+6
        if t == 8:
            a8+=1
        elif t == 9:
            a9+=1
        elif t == 10:
            a10+=1
        elif t == 11:
            a11+=1
        elif t == 12:
            a12+=1
        elif t == 13:
            a13+=1
        elif t == 14:
            a14+=1
        elif t == 15:
            a15+=1
        elif t == 16:
            a16+=1
        elif t == 17:
            a17+=1
        elif t == 18:
            a18+=1
        else:
            print ("what the fuck\n")
    print(a8/a*100," ",a9/a*100," ",a10/a*100," ",a11/a*100," ",a12/a*100," ",a13/a*100," ",a14/a*100," ",a15/a*100," ",a16/a*100," ",a17/a*100," ",a18/a*100," ")
def dice():
    rol=0
    while True:
        r=input("dice sides >")
        r = int(r)
        if r==0:
            break
        times=int(input("how many times >"))
        total=0
        num=0
        ave=[]
        for i in range(0,times):
            rol=roll(r)
            total=total+rol
            num=num+1
            ave.append(rol)
            print (rol)
        average=sum(ave)
        print("your total from",num,"d",r,"'s is",total)
        print("average of",(average/times))
def vstat():
    vstats(1)
def vstats(y):
    print("2d6+6 stats")
    for x in range(y):
        print("player",x+1)
        for i in range(6):
            s = 6
            for n in range(2):
                num = roll(6)
                s = s + num
            print(i+1,": ",s)
def vsa(x):
    print("average of vstat")
    total = 0
    for y in range(x):
        s = 6
        for n in range(2):
            num = roll(6)
            s = s + num
        total = total + s
    print(total/x)
def sa(x):
    print("average of stat")
    total = 0
    for y in range(x):
        s = 0
        m = 6
        for n in range(4):
            num = roll(6)
            if num <= m:
                m = num
            s = s + num
        s = s - m
        total = total + s
    print(total/x)
def stat():
    stats(1)
def stats(y):
    print("4d6-the lowest stats")
    for x in range(y):
        print("player",x+1)
        for i in range(6):
            s = 0
            m = 6
            for n in range(4):
                num = roll(6)
                if num <= m:
                    m = num
                s = s + num
            s = s - m
            print(i+1,": ",s)
def d():
    while True:
        r=input("roll >")
        if (r=="end" or r=="exit"):
            break
        loc = r.find('d')
        rolls = int(r[0:loc])
        sides = int(r[loc+1:])
        total = 0
        ave=[]
        for i in range(0,rolls):
            rol=roll(sides)
            total=total+rol
            ave.append(rol)
            print (rol)
        average=sum(ave)
        print("your total from",rolls,"d",sides,"'s is",total)
        print("average of",(average/rolls))
def brightwing():
    import spells
    can_lvl = 3
    hit = 10
    spells.firebolt(hit,can_lvl)
        
            

