import csv

with open("data.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerow(["transaction_id", 1])

with open("data.csv") as file:
    reader = csv.reader(file)
    print(list(reader))
    for row in reader:
        print(row)
