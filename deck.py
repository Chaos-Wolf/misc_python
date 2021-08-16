import random
class Card_Stan(object):
	def __init__(self,suite,num,value):
		self.suite = suite
		self.num = num
		self.value = value
	def __str__(self):
		return(str(self.num)+" of "+str(self.suite))
	
class Deck_52(object):
	def __init__(self):
		self.L_Of_Suites = ["Spades","Clubs","Diamonds","Hearts"]
		self.L_Of_Num = ["Ace","2","3","4","5","6","7","8","9","10","Jack","Queen","King"]
		self.L_Of_Cards = []
		self.L_Of_Cards_Shuf = []
		self.L_Of_Spent = []
		for i in range(4):
			for j in range(13):
				temp_card = Card_Stan(self.L_Of_Suites[i],self.L_Of_Num[j],j+1)
				self.L_Of_Cards.append(temp_card)
		self.Shuffle()
	def Shuffle(self):
		self.L_Of_Cards_Shuf = []
		self.L_Of_Spent = []
		L_Temp = self.L_Of_Cards[:]
		for i in range(len(self.L_Of_Cards)):
			pull = random.choice(L_Temp)
			self.L_Of_Cards_Shuf.append(pull)
			L_Temp.remove(pull)	
	def Pull(self):
		pull = self.L_Of_Cards_Shuf[0]
		self.L_Of_Cards_Shuf.remove(pull)
		self.L_Of_Spent.append(pull)
		return(pull)
	def Next_Card(self):
		return(self.L_Of_Cards_Shuf[0])	
	def Cards_Left(self):
		for x in self.L_Of_Cards_Shuf:
			print(x)

class Hand(object):
	def __init__(self,deck,name,size):
		self.Hand = []
		for i in range(size):
			self.Hand.append(deck.Pull())
		self.name = name
	def __str__(self):
		temp = self.name
		for i in self.Hand:
			temp = temp + "\n" + str(i)
		return(temp)

def Texas_Holdem(players):
	deck = Deck_52()
	hands = []
	for i in range(players):
		hands.append(Hand(deck,str(i),2))
	deck.Pull()
	hands.append(Hand(deck,"Flop",3))
	deck.Pull()
	hands.append(Hand(deck,"Turn",1))
	deck.Pull()
	hands.append(Hand(deck,"River",1))
	for i in hands:
		print(i,"\n")
	print(deck.Next_Card())

deck = Deck_52()
deck.Cards_Left()
