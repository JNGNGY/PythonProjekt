# Python3.8
# Mac OSx
import csv
with open('File_B_In2019_L.csv', encoding='mac_roman') as csvdatei:
    csv_reader = csv.reader(csvdatei, delimiter=';')
    Name_freq = {}
    for row in csv_reader:
        print(row)
        ID, Vorname, Name, Strasse, Hausnr, PLZ, Ort, Telefon = row
        Name_freq[Name] = Name_freq.get(Name, 0) + 1

    print('-'*70)

with open('File_B_In2019_L.csv', encoding='mac_roman') as csvdatei:
    csv_reader = csv.reader(csvdatei, delimiter=';')
    duplicate_Names = []
    for row in csv_reader:
        ID, Vorname, Name, Strasse, Hausnr, PLZ, Ort, Telefon = row
        if Name_freq[Name] > 1:
            duplicate_Names.append(row)

# show results
import pprint
pprint.pprint(Name_freq)
print('-'*70)
pprint.pprint(sorted(duplicate_Names))