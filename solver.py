import csv

rows = []
path = input()

with open(path, mode='r', encoding='utf-8-sig') as csv_f:
    reader = csv.reader(csv_f)
    header = next(reader)

    for row in reader:
        for el in row:
            if el != '': rows.append(row)

print(header)
print(rows)