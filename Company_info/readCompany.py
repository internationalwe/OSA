import csv

f = open('company_info.csv', 'r', encoding='utf-8')
rdr = csv.reader(f)

for line in rdr:
    print(line[1])

f.close()