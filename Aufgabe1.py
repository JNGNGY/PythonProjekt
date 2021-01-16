# Python 3.9.1
# Windows 10
# Creator: Nguyen Jan, Kroll Marco, Kayis Boran
import os
def csveinleisen_fileb():
    import csv
    import os
    import pathlib
    path = pathlib.Path().absolute()                                                              # Holt der aktuellen Verzeichnis
    for fileb in os.listdir(path):                                                                # For Schleife durchs Verzeichnis
        if os.path.isfile(os.path.join(path,fileb)) and 'File_B_' in fileb:                       # Wenn im Verzeichnis ein File gibt mit dem namen "File_B_"
          with open(fileb, encoding='mac_roman') as fileb:                                        # öffnet csv file
            fileb_reader = csv.DictReader(fileb, delimiter=';')                                   # liest CSV ein
            filewrite = open('FileB.csv', 'w', newline='')                                        # erstellt neue CSV File
            header = ['ID', 'Vorname', 'Name', 'Strasse', 'Hausnr.', 'PLZ', 'Ort', 'Telefon 1']   # Array für Header
            writer = csv.DictWriter(filewrite, delimiter=';', fieldnames=header)                  # Funktion schreiben
            writer.writeheader()                                                                  # Schreibt den Header
            for row in fileb_reader:                                                              # Für jede Zeile in der Variable
                del row ['ID']                                                                    # Löscht den Inhalt von Spalte ID
                writer.writerow(row)                                                              # Zeile wird ins neue CSV gschrieben
            filewrite.close()                                                                     # Schliesst das CSV Datei
            fileb.close()                                                                         # Schliesst das CSV Datei
 
def csveinleisen_filea():
    import csv
    import os
    import pathlib           
    path = pathlib.Path().absolute()                                                              # Holt der aktuellen Verzeichnis
    for filea in os.listdir(path):                                                                # For Schleife durchs Verzeichnis
        if os.path.isfile(os.path.join(path,filea)) and 'File_A_' in filea:                       # Wenn im Verzeichnis ein File gibt mit dem namen "File_B_"
          with open(filea, encoding='mac_roman') as filea:                                        # öffnet csv file
            filea_reader = csv.DictReader(filea, delimiter=';')                                   # liest CSV ein
            filewrite = open('FileA.csv', 'w', newline='')                                        # erstellt neue CSV File
            header = ['ID', 'Vorname', 'Name', 'Strasse', 'Hausnr.', 'PLZ', 'Ort', 'Telefon 1']   # Array für Header
            writer = csv.DictWriter(filewrite, delimiter=';', fieldnames=header)                  # Funktion schreiben
            writer.writeheader()                                                                  # Schreibt den Header
            for row in filea_reader:                                                              # Für jede Zeile in der Variable
                del row ['ID']                                                                    # Löscht den Inhalt von Spalte ID
                writer.writerow(row)                                                              # Zeile wird ins neue CSV gschrieben
            filewrite.close()                                                                     # Schliesst das CSV Datei
            filea.close()                                                                         # Schliesst das CSV Datei

def duplicatefind():
    import csv
    datensatzb = []                                                                               # Array erstellen
    with open('FileB.csv', encoding='mac_roman') as fileb:                                        # öffnet csv file
        fileb_reader = csv.DictReader(fileb, delimiter=';')                                       # liest CSV ein
        for line in fileb_reader:                                                                 # Für jede Zeile in der Variable
            datensatzb.append(line)                                                               # Speicher die Zeile im Array
        fileb.close                                                                               # Schliesst das CSV Datei

    with open('FileA.csv', encoding='mac_roman') as filea:                                        # öffnet csv file
        filea_reader = csv.DictReader(filea, delimiter=';')                                       # liest CSV ein
        filecwrite = open('FileC.csv', 'w', encoding='mac_roman', newline='')                     # erstellt neue CSV File
        header = ['ID', 'Vorname', 'Name', 'Strasse', 'Hausnr.', 'PLZ', 'Ort', 'Telefon 1']       # Array für Header
        writer = csv.DictWriter(filecwrite, delimiter=';', fieldnames=header)                     # Funktion schreiben
        writer.writeheader()                                                                      # Schreibt den Header
        for line in filea_reader:                                                                 # Für jede Zeile in der Variable
            count = datensatzb.count(line)                                                        # Zählt wie oft die Zeile in der Variable vor kommt
            if count >= 2:                                                                        # Wenn gleich oder mehr als 2 mal vorkommt
                writer.writerow(line)                                                             # Zeile wird ins neue CSV gschrieben
        filecwrite.close                                                                          # Schliesst das CSV Datei
        filea.close                                                                               # Schliesst das CSV Datei

def deletedoppelte():
    with open('FileC.csv', 'r', encoding='mac_roman') as fileRedundant:                           # öffnet csv file
        filenoredudant = open('NoRedudant.csv', 'w', encoding='mac_roman')                        # erstellt neue CSV File
        duplicate = set()                                                                         # Wert kann nicht mehrmals in der Variable vorkommen
        for row in fileRedundant:                                                                 # Für jede Zeile in der Variable
            if row not in  duplicate:                                                             # Wenn Zeile nicht in der Variable ist
                duplicate.add(row)                                                                # Zeile wird in Duplicate hinzugefügt
                filenoredudant.write(row)                                                         # Zeile wird ins neue CSV gschrieben
        fileRedundant.close                                                                       # Schliesst das CSV Datei

def createid():
    import csv
    with open('NoRedudant.csv', encoding='mac_roman') as FileNoDuplicate:                         # öffnet csv file
        noduplicate_reader = csv.DictReader(FileNoDuplicate, delimiter=';')                       # liest CSV ein
        endfile = open('File_C_Inf2019l_JMB.csv', 'w', encoding='mac_roman',  newline='')         # erstellt neue CSV File
        header = ['ID', 'Vorname', 'Name', 'Strasse', 'Hausnr.', 'PLZ', 'Ort', 'Telefon 1']       # Array für Header
        writer = csv.DictWriter(endfile, delimiter=';', fieldnames=header)                        # Funktion schreiben
        writer.writeheader()                                                                      # Schreibt den Header
        for count, row in enumerate(noduplicate_reader,1):                                        # Für jede Zeile mit inhalt wird es von 1 hinaufgezählt
            row['ID'] = count                                                                     # Zählt von Spalte ID von 1 aufwärts
            writer.writerow(row)                                                                  # Zeile wird ins neue CSV gschrieben
        FileNoDuplicate.close()                                                                   # Schliesst das CSV Datei
        endfile.close()                                                                           # Schliesst das CSV Datei


print('Start Script')

#Methode ausführen
csveinleisen_filea()
csveinleisen_fileb()
duplicatefind()
deletedoppelte()
createid()

# Files löschen die nicht gebraucht werden
os.remove('FileC.csv')
os.remove('NoRedudant.csv')
os.remove('FileA.csv')
os.remove('FileB.csv')

print('Script done')