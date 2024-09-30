import paramiko
import time
import getpass

username = input('enter username :')
password = getpass.getpass('Enter password :')
ssh_client=paramiko.SSHClient()

ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

Router={"hostname":"10.1.1.10","port":"22","username": username, "password": password}
print(f'Connecting to {Router['hostname']}')
ssh_client.connect(**Router,look_for_keys = False,allow_agent=False)
shell = ssh_client.invoke_shell()
shell.send('terminal length 0 \n')
shell.send('show version\n')
shell.send('sh ip int br\n')
time.sleep(1)

output = shell.recv(10000)
output = output.decode('utf-8')
print(output)

if ssh_client.get_transport().is_active:
    print(f'Closing connection to {Router['hostname']}')
    ssh_client.close()