import requests

def ellicott_city():
	data = requests.get("http://api.openweathermap.org/data/2.5/weather?q=ellicott%20city&appid=9782ecda8479af4702ed641dcbb65a90").json()
	temp_kelvin = data['main']['temp']
	temp_faren = temp_kelvin*(9/5)-459.67
	return round(temp_faren)