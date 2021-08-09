import telethon.sync
from telethon import TelegramClient
from telethon.errors import SessionPasswordNeededError
from telethon.tl.functions.messages import (GetHistoryRequest)
import time
from telethon.tl.types import (
PeerChannel
)
import pyautogui

api_id = *******
api_hash = '***************'
username = '*****'
phone= '+91**********'
user_input_channel = 'https://t.me/*************'



#input("enter entity(telegram URL or entity id):")

client = TelegramClient(username, api_id, api_hash)
client.start()
print("Client Created")
# Ensure you're authorized
if not client.is_user_authorized():
	client.send_code_request(phone)
	try:
		client.sign_in(phone, input('Enter the code: '))
	except SessionPasswordNeededError:
		client.sign_in(password=input('Password: '))





if user_input_channel.isdigit():
	entity = PeerChannel(int(user_input_channel))
else:
	entity = user_input_channel

my_channel = client.get_entity(entity)





resetTime = float(input('Enter the reset time in seconds : '))
checkIterations = float(input('Enter the time period (in minutes) : '))
checkIterations = (checkIterations*60)/resetTime
print('Program will run ' + str(checkIterations) +' times')


def read(fileName):
	file = open("files\\" + fileName + ".txt","r")
	lines = ''.join(file.readlines()[1:]).strip()
	client.send_message(entity=entity,message=lines)


def addToFile(fileName, typeOfQuery):
	#Adding queries or tasks to files with name fileName and typeOfQuery
	file = 'files\\' + fileName + '.txt'
	client.send_message(entity = entity, message = typeOfQuery + ' < ' + message[1] + ' > addedd boss')
	with open(file) as file_object:
		lines = file_object.readlines()
	
	count = int(lines[0].split(" ")[0])

	with open(file, 'w') as filo:
		filo.write( str(count+1) + ' \n')
		for i in range(1,len(lines)):
			filo.write( lines[i])
		filo.write( str(count+1) + ' ' + message[1].strip()+'\n')
	

def deleteFromFile(fileName, typeOfQuery):
	#Deleting queries or tasks to files with name fileName and typeOfQuery
	file = "files\\" + fileName + ".txt"
	delNum = message[1].strip()
	with open(file, "r") as f:
		lines = f.readlines()
	
	count = int(lines[0].split(" ")[0])
	if count < int(delNum):
		client.send_message(entity=entity,message="No such element exist. Try again")
	else:
		delNum = int(delNum)
		with open(file, 'w') as filo:
			filo.write( str(count-1) + ' \n')
			for i in range(1,delNum):
				filo.write( lines[i])
			for i in range(delNum+1,len(lines)):
				filo.write( str(i-1) + ' ' +  ' '.join(lines[i].split(' ')[1:]))
		
		client.send_message(entity=entity,message= typeOfQuery +  "<  "+ lines[delNum][:-1] + " >  deleted boss")
	





while(checkIterations>0 ):

	
	all_messages = [] # contains all messages with details in range 100 
	while True:   
		history = client(GetHistoryRequest(
			peer=my_channel,
			offset_id=0,
			offset_date=None,
			add_offset=0,
			limit=50,
			max_id=0,
			min_id=0,
			hash=0
		))


		if not history.messages:
			break
		messages = history.messages

		for message in messages:
			all_messages.append(message.to_dict())
		break

	
	
	messages =[]
	

	for i in all_messages:
		if 'message' not in i.keys() :
			break
		if i['message'] == 'Anything else boss':
			break
		messages.append(i['message'].lower())
	messages.reverse()






	for i in range(len(messages)):
		message = messages[i].split(':')
		print('.'+message[0].strip()+'.')
		if(message[0].strip() =='screen'):
			upd = pyautogui.screenshot()
			upd.save('files\\updates.png')
			client.send_file(my_channel, 'files\\updates.png', caption="Your Screen Update is ready Sir")
			

		elif(message[0].strip() == 'curi add'):
			addToFile('curi','Query')
			

		elif(message[0].strip() == 'curi'):
			read('curi')
			
			

		elif(message[0].strip() == 'curi delete'):
			deleteFromFile('curi','Curi')
			


		elif(message[0].strip() == 'task add'):
			addToFile('todo','Task')
			

		elif(message[0].strip() == 'task'):
			read('todo')
			
			

		elif(message[0].strip() == 'task delete'):
			deleteFromFile('todo','Task')


		else:
			client.send_message(entity=entity,message="Boss I am unable to find < " + message[0].strip() + ' >')


	time.sleep(resetTime)
	checkIterations-=1

	if messages != []:
		print(".Anything else boss.")

		client.send_message(entity=entity,message="Anything else boss")



