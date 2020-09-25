import os

def send_message(conv_id, message):
	os.system(f'python3 send_msg.py --conversation-id {conv_id} --message-text "{message}"')