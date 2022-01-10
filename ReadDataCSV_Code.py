import csv
file = open("/Users/CSV_File.csv")
csvreader = csv.reader(file)
header = next(csvreader)
print(header)
rows = []
total = 0
for row in csvreader:
    total +=int(row[0])
    rows.append(row)
print(rows)
file.close()