import csv
from datetime import date

# with open('weight-tracking.csv', 'w', newline=' ') as file:
#   writer = csv.writer(file)
#    writer.writerow(["Date", "Weight"])

# Ask the user for their current weight. 
weight = input("Enter Your Weight! \n")
today = date.today()
formattedDate = today.strftime("%d/%m/%Y")
print(formattedDate, " ", weight)

# Open CSV and add entered weight
f = open('weight-tracking.csv', 'a', newline='')
writer = csv.writer(f)
writer.writerow([formattedDate, weight])
print("Weight recorded")
f.close()
