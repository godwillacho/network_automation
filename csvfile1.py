import csv
with open('data1/airtravel.csv')as f:
    reader=csv.reader(f)
    next(reader)
    for row in reader:
        print(row)
#csv file library next() function which can be used to skip the first line of the file
#to display a particular row in the file the index of the elementr in that row can be inserted into the row object to be printed

# creating script to calculate the busiest month of the year 1958
with open('data1/airtravel.csv')as f:
    reader=csv.reader(f)
    next(reader)
    busiest_month = dict()
    for row in reader:
      busiest_month[row[0]]=row[1]

    print (busiest_month)
    max=max(busiest_month.values())
    print (max)
    for k,v in busiest_month.items():
        if v==max:
            print(f"Busiest month in 1958 was {k} and it had {v.strip()} flights")
