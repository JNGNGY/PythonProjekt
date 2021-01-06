# Python 3.8. 3.9
# Mac OSx, Windows 10
#Creator: Nguyen Jan, Kroll Marco, Kayis Boran
import csv
from os import write
with open('File_B_In2019_L.csv', encoding='mac_roman') as csvdatei, open('File_A_Inf2019_L.csv', encoding='mac_roman') as csvdatei1 :           # öffnet csv file
    csv_reader = csv.DictReader(csvdatei, delimiter=';')
    csv_reader1 = csv.DictReader(csvdatei1, delimiter=';')                                                                                      # liest Datein ein mit Header
    csvfile = open('File_C_Inf2019l_Baba.csv', 'w', encoding='mac_roman',  newline='')                                                          # erstellt neue CSV File                
    myFields = ['ID', 'Vorname', 'Name', 'Strasse', 'Hausnr.', 'PLZ', 'Ort', 'Telefon 1']                                                       # Variable für Header
    writer = csv.DictWriter(csvfile, delimiter=';', fieldnames=myFields)                                                                        # Schreibt die Datein ein mit Header        
    writer.writeheader()                                                                                                                        # Schreibt den Header    
    for row in csv_reader:                                                                                                                      # Für jede Zeile in der Variable csv_reader
        writer.writerow(row)
    for row in csv_reader1:                                                                                                                     # Für jede Zeile in der Variable csv_reader
        writer.writerow(row)                                                                                                                    # Schreibt die Datein ein            
    csvfile.close()


 #-----------------------------------------------History--------------------------------------------------------------------------------   
    
#import csv
#from os import write
# show data value
#with open('File_B_In2019_L.csv', encoding='mac_roman') as csvdatei:     # öffnet csv file
 #   csv_reader = csv.reader(csvdatei, delimiter=';')                    # legt trennzeichen fest
  #  Name_freq = {}
   # for row in csv_reader:
        #print(row)                                                      # gibt reihe aus
    #    ID, Vorname, Name, Strasse, Hausnr, PLZ, Ort, Telefon = row
     #   Name_freq[Name] = Name_freq.get(Name, 0) + 1

    #print('-'*70)

# search for rendundant
#with open('File_B_In2019_L.csv', encoding='mac_roman') as csvdatei:
#    csv_reader = csv.reader(csvdatei, delimiter=';')
#    duplicate_Names = []                                                #sucht nach doppelten Daten
#    for row in csv_reader:
 #       ID, Vorname, Name, Strasse, Hausnr, PLZ, Ort, Telefon = row
  #      if Name_freq[Name] > 1:
   #         duplicate_Names.append(row)

# show results
#import pprint
#pprint.pprint(Name_freq)
#print('-'*70)
#pprint.pprint(sorted(duplicate_Names))                                                                                         # Schliesst das CSV Datei        