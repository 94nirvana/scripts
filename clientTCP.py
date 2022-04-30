import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.settimeout(5)

try:
    client.connect(("ip", 80))

    client.send('GET / HTTP/1.1\nHost: host.com\n\n\n')

    print client.recv(1024)

except:
    print "Conexao Falhou"
