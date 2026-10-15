# opening and reading files
# 1. reading files with file[f].read(0).splitlines() which returns each line in the file as an element of a list
with open ('devices.txt') as f:
    content = f.read().splitlines()


print (content)
print(f.closed)
print ('*'*50)

# 2. reading files with file[f].readlines() which returns each line in the file as an element of a list
with open ('devices.txt') as f:
    content = f.readlines()

print (content)
print(f.closed)
print ('*'*50)

# 3. reading files with file[f].readline() which returns one line from the file and moves the cursor to the beginning of the next line
with open ('devices.txt') as f:
    content = f.readline()

print (content)
print(f.closed)
print ('*'*50)

# 4. using the list iterable function wsince a file can be used as an iterable in python
with open ('devices.txt') as f:
    content = list(f)

print (content)
print(f.closed)
print ('*'*50)

# 5. iterating over the file contents
with open ('devices.txt') as f:
    for line in f:
        print(line,end='')
#end='' is iused to stop print function from addding aa extra  new line each time it prints
print(f.closed)
print ('*'*50)