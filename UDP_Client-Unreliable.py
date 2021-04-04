import socket
import sys

FILEDIR = sys.argv[1]
HOST = '127.0.0.1'  
PORT = 54321     

file = open(FILEDIR, "r")
send = file.readline()
while send != "":
	d = 0.1
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.sendto(send.encode('utf-8'), (HOST, PORT))
	data, addr = None, None
	try:
		while True:
			if d>2:
				raise Exception("Server Dead")
				break
			try:
				s.settimeout(d)
				data, addr = s.recvfrom(1024)
				data = data.decode('utf-8')
				break
			except socket.timeout:
				d*=2
				continue
			except KeyboardInterrupt:
				s.close()
				sys.exit()
			print("No data recieved, sending again ...")
			s.sendto(send.encode('utf-8'), (HOST, PORT))
		stuff = data.split()
		if stuff[0] == "200":
			ops = send.split()
			print(ops[1]+ops[0]+ops[2] + " is " + stuff[1])
		elif stuff[0] == "520":
			print("Error: " + stuff[0] + " Invalid OC")
		else:
			print("Error: " + stuff[0] + " Invalid operands")
	except Exception:
		print("Server dead")
		pass
	s.close()
	send = file.readline()
file.close()