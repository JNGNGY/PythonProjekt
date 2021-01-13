# Python 3.9
# Windows 10
# Creator: Nguyen Jan, Kroll Marco, Kayis Boran
import csv
with open('File_C_Inf2019l_JMB.csv') as FileC:                                                                                        # öffnet csv file
 FileC_reader = csv.DictReader(FileC, delimiter=';')                                                                                  # liest CSV ein
 for row in FileC_reader:                                                                                                             # Für jede Zeile in FileC      
  print(row['Vorname'], row['Name'],',',row['Strasse'], row['Hausnr.'],',',row['PLZ'], row['Ort'],',','+41', row['Telefon 1'][1:])    # Printe Spalte aus