from socket import *

server = socket(AF_INET, SOCK_STREAM)
server.bind(('localhost', 12000))
server.listen()
print('Listening To Requests')
while True:
    connection, address = server.accept()
    text = input("Type: ")
    if text == 'exit':
        connection.close()
        quit()
    else:
        connection.send(bytes(text, 'utf-8'))
        data = connection.recv(1024).decode()
        print(f'Client: {data}')
        