import socket
host = 'localhost'
port = 10000
size = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
answer = s.recv(size)
print(answer.decode())
exp = s.recv(size).decode("utf-8") 
arr = exp.split('+')
print(arr)
a = arr[1]
result = int(arr[0])+int(a[:a.index('=')])
s.send(str(result).encode())
print(s.recv(size).decode())
s.close()

