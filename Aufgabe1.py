# Python 3.9
# Windows 10
# Creator: Nguyen Jan, Kroll Marco, Kayis Boran
import csv
import os
import pathlib
path = pathlib.Path().absolute()                                                                                                       # Holt der aktuellen Verzeichnis
for FileB in os.listdir(path):                                                                                                         # For Schleife durchs Verzeichnis
    if os.path.isfile(os.path.join(path,FileB)) and 'File_B_' in FileB:                                                                # Wenn im Verzeichnis ein File gibt mit dem namen "File_B_"
        for FileA in os.listdir(path):                                                                                                 # For Schleife durchs Verzeichnis 
            if os.path.isfile(os.path.join(path,FileA)) and 'File_A_' in FileA:                                                        # Wenn im Verzeichnis ein File gibt mit dem namen "File_A_"
                with open(FileB, encoding='mac_roman') as FileB, open(FileA, encoding='mac_roman') as FileA:                           # öffnet csv file
                    FileB_reader = csv.DictReader(FileB, delimiter=';')                                                                # liest CSV ein
                    FileA_reader = csv.DictReader(FileA, delimiter=';')                                                                # liest CSV ein
                    FileCWrite = open('DatenSchreiben.csv', 'w', encoding='mac_roman', newline='')                                     # erstellt neue CSV File                
                    myFields = ['ID', 'Vorname', 'Name', 'Strasse', 'Hausnr.', 'PLZ', 'Ort', 'Telefon 1']                              # Variable für Header
                    writer = csv.DictWriter(FileCWrite, delimiter=';', fieldnames=myFields)                                            # Funktion schreiben       
                    writer.writeheader()                                                                                               # Schreibt den Header    
                    for row in FileB_reader:                                                                                           # Für jede Zeile in FileB
                        del row ['ID']                                                                                                 # Löscht den Inhalt von Spalte ID
                        writer.writerow(row)                                                                                           # Schreibt ins neue CSV Datei
                    for row in FileA_reader:                                                                                           # Für jede Zeile in FileA
                        del row ['ID']                                                                                                 # Löscht den Inhalt von Spalte I
                        writer.writerow(row)                                                                                           # Schreibt ins neue CSV Datei                                                                                        # Schreibt ins neue CSV Datei
                    FileCWrite.close()                                                                                                 # Schliesst das CSV Datei
                    FileB.close()                                                                                                      # Schliesst das CSV Datei
                    FileA.close()                                                                                                      # Schliesst das CSV Datei

with open('DatenSchreiben.csv', encoding='mac_roman') as FileWrite, open('DoppelteDatenLöschen.csv','w') as FileDeleteDuplicate:       # öffnet csv file und erstellt ein neues CSV
    duplicate = set()                                                                                                                  # set for fast O(1) amortized lookup
    for line in FileWrite:                                                                                                             # Für jede Zeile im File
        if line not in duplicate:                                                                                                      # Wenn Zeile nicht in duplicate existiert    
            duplicate.add(line)                                                                                                        # In Line hinzüfugen
            FileDeleteDuplicate.write(line)                                                                                            # Daten ins neue CSV reinschreiben         
    FileWrite.close()                                                                                                                  # Schliesst das CSV Datei
    FileDeleteDuplicate.close()                                                                                                        # Schliesst das CSV Datei

with open('DoppelteDatenLöschen.csv', encoding='mac_roman') as FileNoDuplicate:                                                        # öffnet csv file
    FileC_reader = csv.DictReader(FileNoDuplicate, delimiter=';')                                                                      # liest CSV ein
    FileC = open('File_C_Inf2019l_JMB.csv', 'w', encoding='mac_roman',  newline='')                                                    # erstellt neue CSV File
    myFields = ['ID', 'Vorname', 'Name', 'Strasse', 'Hausnr.', 'PLZ', 'Ort', 'Telefon 1']                                              # Variable für Header
    writer = csv.DictWriter(FileC, delimiter=';', fieldnames=myFields)                                                                 # Funktion schreiben        
    writer.writeheader()                                                                                                               # Schreibt den Header
    for count, row in enumerate(FileC_reader,1):                                                                                       # Für jede Zeile mit inhalt wird es von 1 hinaufgezählt
        row['ID'] = count                                                                                                              # Zählt von Spalte ID 1 aufwärts
        writer.writerow(row)                                                                                                           # Schreibt die Daten ins neue CSV File               
    FileNoDuplicate.close()                                                                                                            # Schliesst das CSV Datei           
    FileC.close()                                                                                                                      # Schliesst das CSV Datei

import os                
os.remove('DatenSchreiben.csv')                                                                                                        # Löscht die Datei
os.remove('DoppelteDatenLöschen.csv')                                                                                                  # Löscht die Datei