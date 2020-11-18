import json
import datetime

def getMsgData():
	with open("msg_data.json", "r") as data:
		return json.load(data)

the_data = getMsgData()


def newMsg(conv_str, user_id_str):
	dt = datetime.datetime.today()
	date = dt.strftime("%m/%d/%y")

	try:
		beforeValue = the_data[conv_str][date][user_id_str]
		the_data[conv_str][date][user_id_str] = beforeValue + 1
	except KeyError:
		try:
			the_data[conv_str][date][user_id_str] = 1
		except KeyError:
			the_data[conv_str][date] = {user_id_str: 1}

	with open("msg_data.json", "w") as file:
		json.dump(the_data, file, indent=4)

'''
{
	"UgySatjjT_zwYMjvfcl4AaABAQ": {
		"10/15/20": {
			"107091478556168807541": 10
		}
	}
}

'''