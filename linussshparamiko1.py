import paramiko
import time

ssh_client=paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
print('connecting to 192.168.1.169')
ssh_client.connect(hostname='192.168.1.169',port='22',username='kali',password='kali',look_for_keys=False,allow_agent=False)
stdin,stdout,stderr = ssh_client.exec_command('ifconfig \n')
output = stdout.read()
output = output.decode('utf-8')
print(output)


stdin,stdout,stderr = ssh_client.exec_command('who\n')
time.sleep(0.5)
output = stdout.read()
output = output.decode('utf-8')
print(output)

if ssh_client.get_transport().is_active():
    print('closing connection to linux computer')
    ssh_client.close()