import paramiko
import time

def connect_to_sever(sever_ip,sever_port,username,password):
    ssh_client=paramiko.SSHClient
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    print(f'Connecting to {sever_ip}')
    ssh_client.connect(hostname = sever_ip,port = sever_port,username = username,password = password,
                       allow_agent = False,look_for_keys=False)
    return ssh_client

def send_command(ssh_client,command,timeout=1 ):
    shell=ssh_client.invoke(command+'\n')
    time.sleep(timeout)
    return shell

def receive_output(shell,n=10000):
    output=shell.recv(n)
    return output

def close_connection(ssh_client):
    if ssh_client.get_transport().is_active():
        print('Closing connection')
        ssh_client.close()