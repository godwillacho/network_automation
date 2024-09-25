# writing to file

with open('myfile.txt','w') as f:
    f.write('just another mumu line ')
    f.write('\nsecond line of mumu words ')
# when using the write function to write multiple lines it is advisable to add /n becaouse the write function doest add new line by default
#Also it is important to note that the write function does not append to the file but overwrites the existing file


# appending to file

with open('myfile.txt','a') as f:
    f.write('\nThis is the third line of mumu words ')
    f.write('\nAnd this is the fourth line ')

# to be able to write and read a file at the same time r+ which is access mode is used .
with open ('myfile.txt','r+') as f:
    f.write('\nthis line was added with r+ ')
#when using r+ the file must already exist and the content is written to the biggining of the file
#r+ basically works like random access files in java use the seek() funtion to place the pointer at particular position
    f.seek(0)
    print(f.read())
#r+ mode can be used to modify file contents