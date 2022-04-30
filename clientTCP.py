import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.settimeout(5)

try:
    client.connect(("191.252.51.2", 80))

    client.send('GET / HTTP/1.1\nHost: ambientec.com\n\n\n')

    print client.recv(1024)

except:
    print "Conexao Falhou"
