import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

client.sendto("AAAAAAA",("192.168.15.9", 666))

print client.recvfrom(1024)

client.close()
