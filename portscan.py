import socket

ports = [21,22,25,80,443,445,3306]

for port in ports:
	cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	cliente.settimeout(0.1)
	code = cliente.connect_ex(("bancocn.com", int(port)))
	if code == 0:
		print(port,"Porta Aberta!")
	else:
		print(port,"Porta Fechada!")
