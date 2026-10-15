# with open ('macs.txt','r')as f:
#     content=f.read().splitlines()
#     new_content=set()
#     for line in content:
#         new_content.update(line.split(' '))
#
#     print(new_content)
# with open('new_macs','w')as f:
#    for item in new_content:
#        f.write(f'\n{item}')

# with open ('myfile.txt')as f:
#     content=f.read()
def tail(lines,filename):
    with open(filename)as f:
        for content in f.readlines()[-1:-(lines+1):-1]:
            print(content)


tail(5, 'macs.txt')