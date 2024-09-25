import csv
#Writing to csv files
with open ('people.csv',"a")   as f:
    writer = csv.writer(f)
    csvdata=(5, 'Anne', 'Amsterdam')
    writer.writerow(csvdata)

#creationg a csv file and writing the number from 1-100 in one field,thier square in another and thhier cube  in another field \
# the newline parameter is added to file calling function to  eliminate and extra newline in the csv file
with open('numbers.csv','w',newline='')as f:
    writer=csv.writer(f)
    writer.writerow(['Number','Square','Cube','quartic'])  # header row
    for i in range(1,101):
        writer.writerow([i,i**2,i**3,i**4])


#the delimiter in csv files can vary and the delimiter can be passed as a parameter when calling the file object constructor

with open('passwd.csv')as f:
    reader=csv.reader(f,delimiter=':')
    for row in reader:
        print(row)

#a dialect describes the properties of function or library functions
#creating and using custom csv diualects

csv.register_dialect('hashes',delimiter='#',quoting=csv.QUOTE_NONE,)
with open('items.csv')as f:
    reader=csv.reader(f,dialect='hashes')
    for row in reader:
        print(row)

with open('items.csv','a')as f:
    writer=csv.writer(f,dialect='hashes',lineterminator='')
    writer.writerow(('cup',3,1.5))