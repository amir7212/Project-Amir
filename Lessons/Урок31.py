import csv

"""def filters_csv(csv_file):
    with open (csv_file,'r',newline='') as file:
        csv_reader = csv.DictReader(file) 
        for row in csv_reader:
            if row["Name"].startswith("A"):
                print(row)

csv_file = "data.csv"

filters_csv(csv_file)
"""
def filters_csv(csv_file):
    with open (csv_file,'r') as file:
        csv_reader = csv.DictReader(file) 
        for row in csv_reader:
            print(row["Name"],row["Author"],row["Year"])

def add_csv(csv_file, data):
    with open(csv_file, 'a') as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(data)

csv_file = "books.csv"

new_data = ["The Godfather", "Puzo", "1969"]

add_csv(csv_file, new_data)
filters_csv(csv_file)