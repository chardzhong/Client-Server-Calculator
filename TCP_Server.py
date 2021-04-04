import socket
import re
import sys

HOST = '127.0.0.1' 
PORT = 54321

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	s.bind((HOST, PORT))
	s.listen()
	s.settimeout(1)
	while True:
		try:
			conn, addr = s.accept()
		except socket.timeout:
			continue
		except KeyboardInterrupt:
			if conn:
				conn.close()
			s.close()
			sys.exit()
		with conn:
			print('Connected by', addr)
			data = conn.recv(1024).decode("utf-8")
			ops = data.split()
			matchop = re.fullmatch('^(\+|-|\*|/)$', ops[0])
			matchnum1, matchnum2 = re.fullmatch('^[-+]?[0-9]+$', ops[1]), re.fullmatch('^[-+]?[0-9]+$', ops[2])
			tosend = ""
			if matchop and matchnum1 and matchnum2:
				if ops[0] == "/" and ops[2] == "0":
					tosend = "530 -1"
					break
				exp = ops[1] + ops[0] + ops[2]
				result = eval(exp)
				tosend = "200 "+ str(result)
			elif matchop:
				tosend = "530 -1"
			else:
				tosend = "520 -1"
			conn.sendall(tosend.encode('utf-8'))
