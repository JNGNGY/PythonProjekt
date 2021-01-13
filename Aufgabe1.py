# Python 3.9
# Windows 10
# Creator: Nguyen Jan, Kroll Marco, Kayis Boran
import csv
from os import write
with open('File_B_In2019_L.csv', encoding='mac_roman') as FileB, open('File_A_Inf2019_L.csv', encoding='mac_roman') as FileA:          # öffnet csv file
    FileB_reader = csv.DictReader(FileB, delimiter=';')                                                                                # liest CSV ein
    FileA_reader = csv.DictReader(FileA, delimiter=';')                                                                                # liest CSV ein
    FileC = open('DatenSchreiben.csv', 'w', encoding='mac_roman',  newline='')                                                         # erstellt neue CSV File                
    myFields = ['ID', 'Vorname', 'Name', 'Strasse', 'Hausnr.', 'PLZ', 'Ort', 'Telefon 1']                                              # Variable für Header
    writer = csv.DictWriter(FileC, delimiter=';', fieldnames=myFields)                                                                 # Funktion schreiben       
    writer.writeheader()                                                                                                               # Schreibt den Header    
    for row in FileB_reader:                                                                                                           # Für jede Zeile in FileB
        del row ['ID']                                                                                                                 # Löscht den Inhalt von Spalte ID
        writer.writerow(row)                                                                                                           # Schreibt ins neue CSV Datei
    for row in FileA_reader:                                                                                                           # Für jede Zeile in FileA
        del row ['ID']                                                                                                                 # Löscht den Inhalt von Spalte ID
        writer.writerow(row)                                                                                                           # Schreibt ins neue CSV Datei

with open('DatenSchreiben.csv', encoding='mac_roman') as FileWrite, open('DoppelteDatenLöschen.csv','w') as FileDeleteDuplicate:       # öffnet csv file und erstellt ein neues CSV
    duplicate = set()                                                                                                                  # set for fast O(1) amortized lookup
    for line in FileWrite:                                                                                                             # Für jede Zeile im File
        if line not in duplicate:                                                                                                      # Wenn Zeile nicht in duplicate existiert    
            duplicate.add(line)                                                                                                        # In Line hinzüfugen
            FileDeleteDuplicate.write(line)                                                                                            # Daten ins neue CSV reinschreiben         

with open('DoppelteDatenLöschen.csv', encoding='mac_roman') as FileC:                                                                  # öffnet csv file
    FileC_reader = csv.DictReader(FileC, delimiter=';')                                                                                # liest CSV ein
    FileC = open('File_C_Inf2019l_JMB.csv', 'w', encoding='mac_roman',  newline='')                                                   # erstellt neue CSV File
    myFields = ['ID', 'Vorname', 'Name', 'Strasse', 'Hausnr.', 'PLZ', 'Ort', 'Telefon 1']                                              # Variable für Header
    writer = csv.DictWriter(FileC, delimiter=';', fieldnames=myFields)                                                                 # Funktion schreiben        
    writer.writeheader()                                                                                                               # Schreibt den Header
    for count, row in enumerate(FileC_reader,1):                                                                                       # Für jede Zeile mit inhalt wird es von 1 hinaufgezählt
        row['ID'] = count                                                                                                              # Zählt von Spalte ID 1 aufwärts
        writer.writerow(row)                                                                                                           # Schreibt die Daten ins neue CSV File
                 
import os
os.remove('DatenSchreiben.csv')                                                                                                        # Löscht die Datei
os.remove('DoppelteDatenLöschen.csv')                                                                                                  # Löscht die Datei