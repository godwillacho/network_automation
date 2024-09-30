import paramiko
import time
ssh_client = paramiko.SSHClient()

ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

R1 = {'hostname':'10.1.1.10','password':'cisco','username':'u1','port':'22'}
R2 = {'hostname':'10.1.1.20','password':'cisco','username':'u1','port':'22'}
R3 = {'hostname':'10.1.1.30','password':'cisco','username':'u1','port':'22'}
Routers = [R1,R2,R3]
for router in Routers:
    ssh_client.connect(**router,look_for_keys=False,allow_agent=False)
    print(f'Connecting to {router["hostname"]}')
    shell = ssh_client.invoke_shell()
    shell.send('terminal length 0 \n')
    shell.send('enable \n')
    shell.send(f'{router['password']}\n')
    shell.send('conf t \n')
    shell.send('router ospf 1 \n')
    shell.send('network 0.0.0.0 0.0.0.0 area 0 \n')
    shell.send('end \n')
    shell.send('sh ip protocol \n')
    time.sleep(2)

    output = shell.recv(10000)
    output = output.decode('utf-8')
    print(output)


    if ssh_client.get_transport().is_active():
        print(f'closing connection to {router['hostname']}')
        print('*'*100)
        ssh_client.close()