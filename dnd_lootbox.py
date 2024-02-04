import d
import csv
class master_ledger(object):
	def __init__(self):
		self.common = load_from_csv('common_items.csv')
		self.uncommon = load_from_csv('uncommon_items.csv')
		self.rare = load_from_csv('rare_items.csv')
		self.very_rare = load_from_csv('very_rare_items.csv')
		self.legendary = load_from_csv('legendary_items.csv')
		
class lootbox(object):
	def __init__(self,name,rarity,contents):
		self.name = name
		self.rarity = rarity
		self.contents = contents
		
	def __str__(self):
		list_of_contents = ""
		for item in self.contents:
			list_of_contents += str(item)+"\n"
		return(self.name+"\n"+self.rarity+" lootbox\n"+list_of_contents)
	
class item(object):
	def __init__(self, name, rarity, des, magic):
		self.name = name
		self.rarity = rarity
		self.des = des
		self.magic = magic
	def __str__(self):
		buffer = "--------------------"
		if int(self.magic) == 1:
			return(buffer+"\n"+self.rarity+" magical item\n"+self.name+"\n"+self.des+"\n"+buffer)
		else:
			return(buffer+"\n"+self.rarity+" item\n"+self.name+"\n"+self.des+"\n"+buffer)
		
def load_from_csv(filename):
	contents = []
	with open(filename, 'r') as fd:
		reader = csv.reader(fd)
		for row in reader:
			temp = item(row[0],row[1],row[2],row[3])
			contents.append(temp)
	return(contents)

def make_box(box_rarity):
	temp_contents = []
	num_of_items = d.d6.r()+3
	all_items = master_ledger() 
	dc = d.d(len(all_items.common))
	duc = d.d(len(all_items.uncommon))
	dr = d.d(len(all_items.rare))
	dvr = d.d(len(all_items.very_rare))
	dl = d.d(len(all_items.legendary))
	bounds = []
	d1000 = d.d(1000)
	match box_rarity:
		case 'common':
			bounds = [910,960,985,995,1000]
		case 'uncommon':
			bounds = [815,915,965,990,1000]
		case 'rare':
			bounds = [625,825,925,975,1000]
		case 'very rare':
			bounds = [250,650,850,950,1000]
		case 'legendary':
			bounds = [0,300,700,900,1000]
	for i in range(num_of_items):
		rarity = d1000.r()
		if rarity <= bounds[0]:
			temp_contents.append(all_items.common[dc.r()-1])
		elif rarity <= bounds[1]:
			temp_contents.append(all_items.uncommon[duc.r()-1])
		elif rarity <= bounds[2]:
			temp_contents.append(all_items.rare[dr.r()-1])
		elif rarity <= bounds[3]:
			temp_contents.append(all_items.very_rare[dvr.r()-1])
		elif rarity <= bounds[4]:
			temp_contents.append(all_items.legendary[dl.r()-1])
		else:
			print("how the fuck did you get here")
	return(lootbox('lootbox',box_rarity,temp_contents))
			