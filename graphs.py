import msg_data_manipulator as mdm
import matplotlib.pyplot as plt 
import datetime
import receive_messages
import numpy as np
import random

def today(conv_str, pplList, ul):
	data = mdm.getMsgData()[conv_str][datetime.datetime.today().strftime("%m/%d/%y")]
	data = sorted(data.items(), key=lambda x: x[1], reverse=True)
	file_name = f"images/{round(random.random()*1000)}.png"

	user_ids = []
	msg_counts = []

	for item in data:
		msg_counts.append(item[1])
		for ppl in pplList:
			if ppl.id_.chat_id == item[0]:
				person = ppl
				user_ids.append(receive_messages.getName(person.id_, ul))
				break
            
	print(user_ids, msg_counts)

	plt.rcdefaults()
	fig, ax = plt.subplots()
	
	y_pos = np.arange(len(user_ids))
	'''
	plt.xticks(ypos, user_ids)
	plt.bar(ypos, msg_counts)
	plt.show()
	'''

	ax.barh(y_pos, msg_counts, align='center')
	ax.set_yticks(y_pos)
	ax.set_yticklabels(user_ids)
	ax.invert_yaxis()  # labels read top-to-bottom
	ax.set_xlabel('Messages')
	ax.set_title('Today\'s Message Counts')
	plt.tight_layout()
	plt.savefig(file_name)
	return file_name

def yesterday(conv_str, pplList, ul):
	data = mdm.getMsgData()[conv_str][(datetime.datetime.today()-datetime.timedelta(days=1)).strftime("%m/%d/%y")]
	data = sorted(data.items(), key=lambda x: x[1], reverse=True)
	file_name = f"images/{round(random.random()*1000)}.png"

	user_ids = []
	msg_counts = []

	for item in data:
		msg_counts.append(item[1])
		for ppl in pplList:
			if ppl.id_.chat_id == item[0]:
				person = ppl
				user_ids.append(receive_messages.getName(person.id_, ul))
				break
            
	print(user_ids, msg_counts)

	plt.rcdefaults()
	fig, ax = plt.subplots()
	
	y_pos = np.arange(len(user_ids))
	'''
	plt.xticks(ypos, user_ids)
	plt.bar(ypos, msg_counts)
	plt.show()
	'''

	ax.barh(y_pos, msg_counts, align='center')
	ax.set_yticks(y_pos)
	ax.set_yticklabels(user_ids)
	ax.invert_yaxis()  # labels read top-to-bottom
	ax.set_xlabel('Messages')
	ax.set_title('Yesterday\'s Message Counts')
	plt.tight_layout()
	plt.savefig(file_name)
	return file_name