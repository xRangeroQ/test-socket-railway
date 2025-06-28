import socket

sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("0.0.0.0", 8080))
sock.listen()

cn, adr=sock.accept()
print(adr)

for i in range(10):
  cn.send(b'SERVER:UP\n')

cn.close()
sock.close()
