import phonenumbers
from phonenumbers import carrier
import requests
import json
import time

#a function that pulls from telnyx and scrapes the resulting json file 
#for the cariers name
#i cant take credit for this one 
def	getCarrier(number):
	url = 'https://api.telnyx.com/v1/phone_number/1' +	number
	try:
		html = requests.get(url).text
		data =	json.loads(html)
		carrier = data["carrier"]["name"]
	except:
		return False
	time.sleep(1)
	return	carrier

"""def Get_Network(number):
	full_num = "+1" + number
	service_provider = phonenumbers.parse(number,"US")
	print(service_provider)
	print(carrier.name_for_number(service_provider,'en'))"""