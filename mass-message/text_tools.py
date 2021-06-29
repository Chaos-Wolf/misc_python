import phonenumbers
from phonenumbers import carrier
import requests
import json
import time
def	getCarrier(number):
	url = 'https://api.telnyx.com/v1/phone_number/1' +	number
	try:
		html = requests.get(url).text
		data =	json.loads(html)
		carrier = data["carrier"]["mobile_network_code"]
	except:
		return False
	time.sleep(1)
	return	carrier
def Get_Network(number):
	full_num = "+1" + number
	service_provider = phonenumbers.parse(number,"US")
	print(service_provider)
	print(carrier.name_for_number(service_provider,'en'))