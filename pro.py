import dd
from datetime import datetime,timedelta
def pdate(x):
	time = dd.roll(x)
	print(datetime.today() + timedelta(183 + time))
