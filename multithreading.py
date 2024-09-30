import pythonparamikomodule
import threading

def backup(router):
    client = pythonparamikomodule.connect_to_sever(**router)
    shell = pythonparamikomodule.invoke_shell(client)

    pythonparamikomodule.send_command(shell, 'terminal length 0')
    pythonparamikomodule.send_command(shell, 'enable')
    pythonparamikomodule.send_command(shell, 'cisco')
    pythonparamikomodule.send_command(shell, 'show run')

    output = pythonparamikomodule.show_output(shell)
    print(output)

    # we use python list slicing to remove the part of the configuration thats not needed
    output_list = output.splitlines()
    output_list = output_list[11:-1]
    print(output_list)

    # to write this config to a file it nedds to be changed to string using join function
    output = '\n'.join(output_list)
    print(output)

    from datetime import datetime
    now = datetime.now()
    year = now.year
    month = now.month
    day = now.day
    hour = now.hour
    minute = now.minute

    filename = f'{router['sever_ip']}_{year}_{month}_{day}.txt'
    print(filename)
    print('*'*100 +"\n")

    with open(filename, 'w') as f:
        f.write(output)
    pythonparamikomodule.close_connection(client)

threads = list()
r1={"sever_ip":"10.1.1.10","sever_port":"22","username": 'u1', "password": 'cisco'}
r2={"sever_ip":"10.1.1.20","sever_port":"22","username": 'u1', "password": 'cisco'}
r3={"sever_ip":"10.1.1.30","sever_port":"22","username": 'u1', "password": 'cisco'}
routers = [r1, r2, r3]
for router in routers:
    th = threading.Thread(target=backup, args=(router,))
    threads.append(th)

for th in threads:
    th.start()
for th in threads:
    th.join()