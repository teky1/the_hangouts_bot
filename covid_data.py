import requests
from lxml import html

def md_covid():
	data = requests.get("https://services.arcgis.com/njFNhDsUCentVYJW/arcgis/rest/services/MDCOVID19_TotalCasesStatewide/FeatureServer/0/query?where=1%3D1&outFields=*&outSR=4326&f=json").json()
	return data['features'][-1]['attributes']['Count_']

def us_covid():
	site = requests.get("https://www.worldometers.info/coronavirus/country/us/")
	site_code = html.fromstring(site.content)

	return site_code.xpath('//*[@id="maincounter-wrap"]/div/span/text()')[0].strip()