import paramiko
import time

def connect_to_sever(sever_ip,sever_port,username,password):
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    print(f'Connecting to {sever_ip}')
    ssh_client.connect(hostname = sever_ip,port = sever_port,username = username,password = password,allow_agent = False,look_for_keys=False)
    return ssh_client

def invoke_shell(ssh_client):
    shell=ssh_client.invoke_shell()
    return shell

def send_command(shell,command,timeout=1 ):
    shell.send(command + '\n')
    time.sleep(timeout)


def show_output(shell,n=10000):
    output=shell.recv(n)
    return output.decode()

def close_connection(ssh_client):
    if ssh_client.get_transport().is_active():
        print('Closing connection')
        ssh_client.close()

if __name__ == '__main__':
    client = connect_to_sever('10.1.1.10','22','u1','cisco')
    shell = invoke_shell(client)
    send_command(shell,'enable')
    send_command(shell,'cisco')
    send_command(shell,'terminal length 0')
    send_command(shell,'sh version')
    send_command(shell,'sh ip int br')
    output = show_output(shell)
    print(output)
    close_connection(client)
