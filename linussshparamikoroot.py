import paramiko
import time

ssh_client=paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
print('connecting to 192.168.1.169')
ssh_client.connect(hostname='192.168.1.169',port='22',username='kali',password='kali',look_for_keys=False,allow_agent=False)


stdin,stdout,stderr = ssh_client.exec_command('sudo useradd u2\n',get_pty=True)
stdin.write('kali\n')
time.sleep(2)


stdin,stdout,stderr = ssh_client.exec_command('cat /etc/passwd\n')
print(stdout.read().decode('utf-8'))
time.sleep(1)

if ssh_client.get_transport().is_active():
    print('closing connection to linux computer')
    ssh_client.close()