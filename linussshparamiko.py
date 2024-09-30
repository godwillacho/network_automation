import paramiko
import time

ssh_client=paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
print('connecting to 192.168.1.169')
ssh_client.connect(hostname='192.168.1.169',port='22',username='kali',password='kali',look_for_keys=False,allow_agent=False)
shell=ssh_client.invoke_shell()
shell.send('cat /etc/passwd\n')
time.sleep(1)


shell.send('sudo cat /etc/shadow\n')
shell.send('kali\n')
time.sleep(1)

output=shell.recv(10000)
output=output.decode('utf-8')
x = print(output)

if ssh_client.get_transport().is_active():
    print('closing connection to linus computer')
    ssh_client.close()