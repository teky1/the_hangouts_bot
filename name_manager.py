import json

def getName(user_id):
	try:
		with open('names.json') as file:
			return json.load(file)[user_id]
	except KeyError:
		return False

def setName(user_id, name):
	with open('names.json') as file:
		names = json.load(file)
		names[user_id] = name

		with open('names.json', 'w') as json_file:
			json.dump(names, json_file, indent=4)

	return getName(user_id)
