# a simple program to notify you whhen you're back online

import os #for system commands
import datetime	#for noting the time
from time import time

start = time()

def check():
	site = "google.com" #your website of choice
	
	while True:
		if os.system("ping "+site) == 0:
			print("\n\n pass \n device came online at "+str(datetime.datetime.now()))
			time_passed()
			play()
			break
		else:
			print("\n\n fail \n as of "+str(datetime.datetime.now()))
			time_passed()
			os.system("cls")


def time_passed():
	end = time()
	print("\n	time passed: ",datetime.timedelta(seconds=int(end-start)))

def play():
	os.system('F: && cd \\Music\\Soft Jazz\\ && "02. Fallin\'.mp3"') #your music file of choice


if __name__ == '__main__':
	check()




