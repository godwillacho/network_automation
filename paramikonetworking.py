import paramiko
#this to connect to the device using ssh
ssh_client = paramiko.SSHClient()
print('connecting to 10.1.1.10 ')
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname='10.1.1.10',port='22',username='u1',password='cisco',look_for_keys=False,allow_agent=False)

print(ssh_client.get_transport().is_active())
print('closing connection to 10.1.1.10')
ssh_client.close()