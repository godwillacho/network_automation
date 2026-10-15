# this my solution is works but the data is not save into a list its just prionted out properly
with open('devices.txt','r+') as f:
    f.readline()
    linelist=list()
    for line in f:
        linelist=line.split(":")
        print(linelist)

print("\n\n\n")
# this is how iut should  be done
with open('devices.txt','r+') as f:
    content=f.readlines()
    devices=list()
    for line in content[1:]:
        devices.append(line.split(":"))
    print(devices)
# to pick one field from the list and work with it for example to ping all the ip addresses
    for device in devices:
        print(f'pinging {device[1]}')
