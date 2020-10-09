# a simple program to notify you when you're back online

import os #for system commands
from datetime import datetime  #for noting the time


def check():
	site = "google.com" #your website of choice
	while True:
		if os.system("ping "+site) == 0:
			print(" pass \n device came online at "+str(datetime.now()))
			play()
			break
		else:
			print(" fail \n as of "+str(datetime.now()))
			os.system("cls")



def play():
	os.system('F: && cd \\Music\\Soft Jazz\\ && "02. Fallin\'.mp3"') #your music file of choice

if __name__ == '__main__':
	check()




