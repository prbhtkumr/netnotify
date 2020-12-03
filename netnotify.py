# a simple program to notify you when you're back online

import os #for system commands
import datetime	#for noting the time
from time import time
from plyer import notification 

start = time()

def check():
	site = "google.com" #your website of choice
	
	while True:
		if os.system("ping "+site) == 0:
			print("\n\n pass \n device came online at "+str(datetime.datetime.now()))
			time_passed()
			notify()
			print(" time passed: {}".format(time_passed))
			play()
			break
		else:
			print("\n\n fail \n as of "+str(datetime.datetime.now()))
			time_passed()
			print(" time passed: {}".format(time_passed))
			notify()
			os.system("cls")

def time_passed():
	end = time()
	global time_passed
	time_passed = datetime.timedelta(seconds=int(end-start))
	return time_passed
def play():
	os.system('F: && cd \\Music\\Soft Jazz\\ && "02. Fallin\'.mp3"') #your music file of choice

def notify():
	notification.notify( 
		title = "Your device is back online", 
		message = ("Time Offline: {}".format(time_passed)),
		timeout = 5)

if __name__ == '__main__':
	check()

