import csv
import pandas
import sys

header_dict = {}
index = 0
row_list = []

# Inladen eerste 500 rows van dataset
ifile  = open('stage3.csv', "r")
read = csv.reader(ifile)
headers = next(read)
row_list.append(headers)
for i in range(500):
    row_list.append(next(read))

# Veranderd missende data in NA
for row in row_list:
    for i in range(len(row)):
        if row[i] == '':
            row[i] = 'NA'

# Exporteer aangepaste data naar output.csv
writer = csv.writer(open('output.csv', 'w'))
writer.writerows(row_list)

# Maak dicitonary met als keys de headers
for header in headers:
    header_dict[header] = []
    for i in range(1, len(row_list)):
        header_dict[header].append(row_list[i][index])
    index += 1

# Bepaal hoeveel totaal aantal wapens
number_of_guns = 0
for value in header_dict['n_guns_involved']:
    if value != 'NA':
        number_of_guns += int(value)

#bepaal totaal aantal gestolen wapens
number_of_guns_stolen = 0
for value in header_dict['gun_stolen']:
    if 'Unknown' in value:
        print("hello")
    if len(list(value)) < 2:
        number_of_guns_stolen += int(value)



