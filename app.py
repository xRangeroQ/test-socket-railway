import socket

sock=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("0.0.0.0", 8080))

while True:
  try:
    data=sock.recvfrom(4096)

    if not data:
      continue

    sock.sendto(b'SERVER:1', data[1])
  except Exception as e:
    print(e)
    pass
