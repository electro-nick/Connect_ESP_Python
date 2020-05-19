import sys
import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket.settimeout(1.0)
addr = ("192.168.0.187", 4210)

if len(sys.argv) <= 1:
    print('Недостаточно параметров')
else:
	i = 0
	print(sys.argv)
	for val in sys.argv:
		if val == '-h':
			print("\n-m [int] // mode \n-b [byte] // brightness \n-c [byte byte byte] // color\n")
		if val == '-m':
			client_socket.sendto(str.encode("{key: 'mode', value: " + sys.argv[i+1] + "}"), addr)
		if val == '-b':
			client_socket.sendto(str.encode("{key: 'brightness', value: " + sys.argv[i+1] + "}"), addr)
		if val == '-p':
			client_socket.sendto(str.encode("{key: 'power', value: '" + sys.argv[i+1] + "'}"), addr)
		if val == '-c':
			client_socket.sendto(str.encode("{key: 'color', value: '" + sys.argv[i+1] + " " + sys.argv[i+2] + " " + sys.argv[i+3] + "'}"), addr)
		i+=1
		

client_socket.close()