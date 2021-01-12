# Python 3.8. 3.9
# Mac OSx, Windows 10
#Creator: Nguyen Jan, Kroll Marco, Kayis Boran
import csv
with open('File_C_Inf2019l_Baba.csv') as csvfile:
 data = csv.DictReader(csvfile, delimiter=';')
 for row in data:  
  print(row['Vorname'], row['Name'],',',row['Strasse'], row['Hausnr.'],',',row['PLZ'], row['Ort'],',','+41', row['Telefon 1'][1:])