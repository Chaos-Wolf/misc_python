import datetime
class Maya_Date(object):
	def __init__(self,baktun,katun,tun,uinal,kin):
		self.baktun = baktun
		self.katun = katun
		self.tun = tun
		self.uinal = uinal
		self.kin = kin
	def __init__(self,total_days):
		self.baktun = total_days//144000
		self.katun = (total_days%144000)//7200
		self.tun = ((total_days%144000)%7200)//360
		self.uinal = (((total_days%144000)%7200)%360)//20
		self.kin = (((total_days%144000)%7200)%360)%20
	def __str__(self):
		return(str(self.baktun)+"."+str(self.katun)+"."+str(self.tun)+"."+str(self.uinal)+"."+str(self.kin))
	
def today_maya():
	today = datetime.date.today()
	bce = datetime.date.fromisoformat('2012-12-21')
	total_days = 1872000+abs(today-bce).days
	final_date = Maya_Date(total_days)
	return(final_date)
	
def mayan_conversion(year,month,day):
	today = datetime.date(year,month,day)
	end = datetime.date.fromisoformat('2012-12-21')
	total_days = 1872000+(today-end).days
	final_date = Maya_Date(total_days)
	return(final_date)

