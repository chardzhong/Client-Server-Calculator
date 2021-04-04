import socket
import sys

FILEDIR = sys.argv[1]
HOST = '127.0.0.1'  
PORT = 54321     

file = open(FILEDIR, "r")
send = file.readline()
while send != "":
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
		s.connect((HOST, PORT))
		print(send)
		s.sendall(send.encode('utf-8'))
		data = s.recv(1024).decode('utf-8')
		stuff = data.split()
		if stuff[0] == "200":
			ops = send.split()
			print(ops[1]+ops[0]+ops[2] + " is " + stuff[1])
		elif stuff[0] == "520":
			print("Error: " + stuff[0] + " Invalid OC")
		else:
			print("Error: " + stuff[0] + " Invalid operands")
		s.close()
	send = file.readline()
file.close()