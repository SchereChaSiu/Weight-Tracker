import csv
import os
from datetime import date

def generateFile():
    f = open('weight.csv', 'w', newline='')
    writer = csv.writer(f)
    writer.writerow(['Date', 'Weight'])
    print('Weight.csv generated')
    f.close()

# Generate file if it doesn't exist
if os.path.isfile('./weight.csv') == False:
    generateFile()

# Ask the user for their current weight. 
weight = input("Enter Your Weight! \n")
today = date.today()
formattedDate = today.strftime("%d/%m/%Y")
print(formattedDate, " ", weight)

# Open CSV and add entered weight
f = open('weight.csv', 'a', newline='')
writer = csv.writer(f)
writer.writerow([formattedDate, weight])
print("Weight recorded")
f.close()
