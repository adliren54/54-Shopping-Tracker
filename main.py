import csv # Imports the csv library

total = 0

with open("Day54Totals.csv") as file: 
  reader = csv.DictReader(file) 
  
  for row in reader: 
    print(row["Net Total"])
    total += float(row["Net Total"]) 

print(f"Total: {total}")