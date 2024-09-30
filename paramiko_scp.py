import paramiko
from scp import SCPClient

ssh_client = paramiko.SSHClient()
ssh_client.load_system_host_keys()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname = '192.168.1.169',port = 22,username = 'kali',password = 'kali',allow_agent=False, look_for_keys = True)

scp = SCPClient(ssh_client.get_transport())
#copy a single  to remote server
scp.put('devices.txt','/tmp/aa.txt')
# copying a directory to remote server
scp.put('data1', recursive=True ,remote_path='/tmp')

#copying a file from remote server
scp.get('/tmp/aa.txt','aa.txt')

#copying a directory from remote server
scp.get('/tmp/data1','data2',recursive=True)

ssh_client.close()
scp.close()