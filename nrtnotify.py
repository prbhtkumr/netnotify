# a simple program to notify you whhen you're back online

import os
import sys
from datetime import datetime


def check():
	site = "google.com" #your website of choice
	while True:
		if os.system("ping "+site) == 0:
			print("pass")
			print("device came online at "+str(datetime.now()))
			play()
			break
		else:
			sys.stdout.write("fail \n as of "+str(datetime.now()))
			sys.stdout.flush()
			os.system("cls")



def play():
	os.system('F: && cd \\Music\\Soft Jazz\\ && "02. Fallin\'.mp3"') #your music of choice

if __name__ == '__main__':
	check()




