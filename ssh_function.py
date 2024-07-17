import time
from paramiko import client
from getpass import getpass

# server credentials
hostname="192.168.137.120"
username=input('enter the username: ') or 'admin'
password=getpass(f'enter the password for {username}:') or 'admin' 

# cli interface commands 
commands =['config t','int lo1001','ip address 1.1.1.1 255.255.255.0','end']

def cicos_cmd_executor(hostname,commands):
     # connecting to server 
    
    print(f'connecting to device{hostname} ')
    ssh_client=client.SSHClient()
    ssh_client.set_missing_host_key_policy(client.AutoAddPolicy())
    ssh_client.connect (hostname=hostname
                    ,username=username
                    ,password=password
                    ,look_for_keys=False
                    ,allow_agent=False
                    ,port=22 
                    )
    print(f"connected successfully to {hostname}")
    device_acccess=ssh_client.invoke_shell()
    device_acccess.send('terminal len 0\n')

    for cmd in commands:
        device_acccess.send(f"{cmd}\n")
        time.sleep(1)
        output = device_acccess.recv(65535)
        print(output.decode(),end='')

    device_acccess.send('show run int lo1001\n')
    time.sleep(1)
    output = device_acccess.recv(65535)
    print(output.decode())

    ssh_client.close()


cicos_cmd_executor(hostname=hostname,commands=commands)
