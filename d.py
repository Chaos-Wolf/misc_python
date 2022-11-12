import random
class d(object):
	def __init__(self,value):
		self.value = value
	def __str__(self):
		return("D"+str(self.value))
	def r(self):
		return(random.choice(range(1,self.value+1)))
	def rs(self,times):
		total = 0
		for i in range(times):
			total = total + random.choice(range(1,self.value+1))
		return(total)
class stat(object):
	d6 = d(6)
	def rolled_drop_lowest(self):
		min_value = 6
		total = 0
		for i in range(4):
			num = d6.r()
			if num <= min_value:
				min_value = num
			total = total + num
		total = total - min_value
		return(total)
	def rolled_var(self):
		num1 = d6.r()
		num2 = d6.r()
		return(num1 + num2 + 6)
class spell(object):
	des = ""
	def add_des(self,des):
		self.des = des
	def __str__(self):
		return(self.des)
class attack_spell(spell):
	def __init__(self,times,value,att,dam_type):
		self.times = times
		self.value = value
		self.att = att
		self.dam_type = dam_type
	def attack(self):
		spell_attack = d20.r() + self.att
		dattack = d(self.value)
		spell_damage = dattack.rs(self.times)
		return(spell_attack,spell_damage)
class save_spell(spell):
	def __init__(self,times,value,save):
		self.times = times
		self.value = value
		self.save = save
	def cast(self):
		die = d(self.value)
		spell_damage = die.rs(self.times)
		return(self.save,spell_damage)
class pc(object):
	def __init__(self):
		stat_temp = stat()
		self.strength = stat_temp.rolled_drop_lowest()
		self.dexterity = stat_temp.rolled_drop_lowest()
		self.constitution = stat_temp.rolled_drop_lowest()
		self.intelligence = stat_temp.rolled_drop_lowest()
		self.wisdom = stat_temp.rolled_drop_lowest()
		self.charisma = stat_temp.rolled_drop_lowest()
	def __str__(self):
		return("str: "+str(self.strength)+"\ndex: "+str(self.dexterity)+"\ncon: "+str(self.constitution)+"\nint: "+str(self.intelligence)+"\nwis: "+str(self.wisdom)+"\ncha: "+str(self.charisma))
class pcv(pc):
	def __init__(self):
		stat_temp = stat()
		self.strength = stat_temp.rolled_var()
		self.dexterity = stat_temp.rolled_var()
		self.constitution = stat_temp.rolled_var()
		self.intelligence = stat_temp.rolled_var()
		self.wisdom = stat_temp.rolled_var()
		self.charisma = stat_temp.rolled_var()
		
d100 = d(100)
d20 = d(20)
d12 = d(12)
d10 = d(10)
d8 = d(8)
d6 = d(6)
d4 = d(4)
coin = d(2)
	