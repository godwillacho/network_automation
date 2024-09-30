import pythonparamikomodule
import getpass


username = input('Enter  your username: ')
password = getpass.getpass('enter your password :')

ssh_client = pythonparamikomodule.connect_to_sever('192.168.1.169',22, username, password)
remote_connection=pythonparamikomodule.invoke_shell(ssh_client)

new_user = input('enter the user you want to create : ')
command = f'sudo useradd -m -d /home/' + new_user + ' -s /bin/bash user' + new_user
pythonparamikomodule.send_command(remote_connection,command)
pythonparamikomodule.send_command(remote_connection,password)
print('A new user has been created.')
answer = input('Display the users ? <y/n>')
if answer == 'y' or answer == 'yes' :
     users = pythonparamikomodule.send_command(remote_connection,'cat /etc/passwd')
     print(users.decode('utf-8'))
pythonparamikomodule.close_connection(ssh_client)





