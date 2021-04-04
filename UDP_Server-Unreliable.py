import socket
import re
import sys
import random

DROP = float(sys.argv[1])
HOST = '127.0.0.1' 
PORT = 54321

def drop(prob):
	return random.random() < prob

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((HOST, PORT))
s.settimeout(1)

while True:
	try:
		data, addr = s.recvfrom(1024)
		data = data.decode('utf-8')
		print('Connected by', addr)
	except socket.timeout:
		continue
	except KeyboardInterrupt:
		s.close()
		sys.exit()
	if drop(DROP):
		continue	
	ops = data.split()
	matchop = re.fullmatch('^(\+|-|\*|/)$', ops[0])
	matchnum1, mathnum2 = re.fullmatch('^[-+]?[0-9]+$', ops[1]), re.fullmatch('^[-+]?[0-9]+$', ops[2])
	tosend = ""
	if matchop and matchnum1 and mathnum2:
		if ops[0] == "/" and ops[2] == "0":
			tosend = "530 -1"
			break
		exp = ops[1] + ops[0] + ops[2]
		result = int(eval(exp)) 
		tosend = "200 "+ str(result)
	elif matchop:
		tosend = "530 -1"
	else:
		tosend = "520 -1"
	s.sendto(tosend.encode('utf-8'), addr)
