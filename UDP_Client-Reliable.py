import socket
import sys

FILEDIR = sys.argv[1]
HOST = '127.0.0.1'  
PORT = 54321     


file = open(FILEDIR, "r")
send = file.readline()
while send != "":
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.sendto(send.encode('utf-8'), (HOST, PORT))
	s.settimeout(1)
	data, addr = None, None	
	try:
		data, addr = s.recvfrom(1024)
		data = data.decode('utf-8')
	except socket.timeout:
		continue
	except KeyboardInterrupt:
		s.close()
		sys.exit()
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