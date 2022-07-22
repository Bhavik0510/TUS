import csv
#Read CSV file
with open('Student.csv') as file:
    #read_file = csv.reader(file)
    read_file = csv.DictReader(file)

    for i in read_file:
        print(i)

#write CSV file

# importing the csv module
# import csv

# my data rows as dictionary objects
mydict = [{'No':'5', 'name': 'Nikhil', 'Marks': '52'}]

# field names
fields = ['No','name', 'Marks']

# name of csv file
filename = "Student.csv"

# writing to csv file
# with open('Student.csv', 'w') as csvfile:
#     writer = csv.DictWriter(csvfile, fieldnames=fields)
#
#     writer.writeheader()
#
#     # writing data rows
#     writer.writerows(mydict)



