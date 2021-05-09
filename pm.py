from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import csv
import math
def borderv():
    MB = checksize()
    border = [["b1",MB,MB,MB,0,'w','o'],
              ["b2",MB,-MB,MB,0,'w','o'],
              ["b3",MB,MB,-MB,0,'w','o'],
              ["b4",MB,-MB,-MB,0,'w','o'],
              ["b5",-MB,MB,MB,0,'w','o'],
              ["b6",-MB,-MB,MB,0,'w','o'],
              ["b7",-MB,MB,-MB,0,'w','o'],
              ["b8",-MB,-MB,-MB,0,'w','o']]
    return border

class star:
    def __init__(self,name,x,y,z,s,c,t):
        self.name = name
        self.x = x
        self.y = y
        self.z = z
        self.size = s
        self.color = c
        self.type = t
        
def checksize():
    s = readall()
    m = max([max(abs(i)for i in s[1]),max(abs(i)for i in s[2]), max(abs(i)for i in s[3])])
    return m

def writestar(star):
    with open('space.csv', mode='a', newline='\n') as file:
        writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow([star.name,star.x,star.y,star.z,star.size,star.color,star.type])
        n = max([abs(star.x),abs(star.y),abs(star.z)])

def outputall():
    with open('space.csv', mode='r') as file:
        data = csv.reader(file)
        for row in data:
            print(row)

def readall():
    stars = [[],[],[],[],[],[],[]]
    with open('space.csv', mode='r') as file:
        data = csv.reader(file)
        for row in data:
            stars[0].append(row[0])
            stars[1].append(int(row[1]))
            stars[2].append(int(row[2]))
            stars[3].append(int(row[3]))
            stars[4].append(int(row[4]))
            stars[5].append(row[5])
            stars[6].append(row[6])
    return stars

def graph():
    mpl.style.use('dark_background')
    border = borderv()
    s = readall()
    fig = plt.figure()
    ax = plt.axes(projection="3d")
    for i,txt in enumerate(border[0]):
        ax.scatter3D(border[i][1],border[i][2],border[i][3],s=border[i][4],c=border[i][5],marker=border[i][6])
    for i,txt in enumerate(s[0]):
        ax.scatter3D(s[1][i],s[2][i],s[3][i],s=s[4][i],c=s[5][i],marker=s[6][i])
        ax.text(s[1][i],s[2][i],s[3][i],txt)
    plt.show()

def distance(name1, name2):
    s = readall()
    xyz = [[],[],[]]
    found = 0
    for i,txt in enumerate(s[0]):
        if (txt == name1 or txt == name2):
            xyz[0].append(s[1][i])
            xyz[1].append(s[2][i])
            xyz[2].append(s[3][i])
            found = found + 1
    if (found < 2):
        print ("stars not found")
        return 0
    elif (found == 2):
        dis = math.sqrt(pow((xyz[0][0]-xyz[0][1]),2)+pow((xyz[1][0]-xyz[1][1]),2)+pow((xyz[2][0]-xyz[2][1]),2))
        return dis
    else:
        print ("how")
        return 1
    

