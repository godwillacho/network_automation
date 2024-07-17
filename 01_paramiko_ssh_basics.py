import time
from paramiko import client
from getpass import getpass

hostname ="192.168.137.120"
username =input('Enter the username ') or "admin"
password= getpass(f'\U0001F511 enter password for the user {username}:') or 'admin'

ssh_client=client.SSHClient()
ssh_client.set_missing_host_key_policy(client.AutoAddPolicy())

ssh_client.connect(hostname=hostname
                   ,username=username
                   ,password=password
                   ,look_for_keys=False
                   ,allow_agent=False
                   ,port=22 
                   )
print('CONNECTED SUCCESSFULLY \n')
device_access =ssh_client.invoke_shell()

device_access.send("show run \n")
time.sleep(5)

output = device_access.recv(65535)
print(output.decode())

ssh_client.close()
