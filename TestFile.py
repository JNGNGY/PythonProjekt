import csv
with open('File_B_In2019_L.csv', newline='') as csvfile:
 data = csv.DictReader(csvfile, delimiter=';')
 print("ID Department Name")
 print("---------------------------------")
 for row in data:
   print(row['Vorname'], row['Name'])