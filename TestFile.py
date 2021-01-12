import sys
import csv

#variablen definieren

File_A_Inf2019l = open('File_A_Inf2019_L.csv', encoding='mac_roman')       #argumente entgegen nehmen
File_B_Inf2019l = open('File_B_In2019_L.csv', encoding='mac_roman')

#with open('File_B_In2019_L.csv', encoding='mac_roman') as File_B_Inf2019l, open('File_A_Inf2019_L.csv', encoding='mac_roman') as File_A_Inf2019l:

inhaltA = File_A_Inf2019l.read()  # inhalt csv auslesen und speichern
inhaltB = File_B_Inf2019l.read()
  
inhaltC = inhaltA + inhaltB     #inhalt zusammenführen

zeilenC = inhaltC.split('\n')
anzahlZeilenC, anzahlSpaltenC = len(zeilenC), 8  #grösse definieren

arrC = [[0 for x in range(anzahlSpaltenC)] for y in range(anzahlZeilenC)]  # array definieren



def füllenArray():
    for i in range(anzahlZeilenC):  #array füllen
        spalten = zeilenC[i].split(';')
        if len(spalten) == 8:
            for x in range(anzahlSpaltenC):
                arrC[i][x] = spalten[x]
                




def erkennenDoppelteDatensätze():       #erkennt doppelte Datensätze
    for y in range(anzahlZeilenC): #nimmt erste row

            for z in range(anzahlZeilenC): #nimmt zweite row

                if y != z:  #stellt sicher, dass index unterschiedlich ist

                    for s in range(anzahlSpaltenC - 1):  # vergleicht Inhalt von beiden rows, -1 damit id nicht geprüft wird
                        if s != 7 and y < anzahlZeilenC and z < anzahlZeilenC:  #verhindert index fehler
                            if arrC[y][s + 1] == arrC[z][s + 1]:  #+1 damit id nicht geprüft wird
                                if s == 6:  #wenn letzter wert positiv geprüft wird, doppelter Datensatz löschen
                                    löschenDatensatz(z)
                            else:
                                break


def löschenDatensatz(ds):
    global anzahlZeilenC
    anzahlZeilenC -= 1
    arrC.pop(ds)     #datensatz löschen



def schreibenDatei():
    indexZähler = 0
    print(arrC)
    csv.register_dialect("semik.", delimiter=";")       #trenner definieren
    datei = open('File_C_Inf2019l_VAN.csv', 'w', encoding='mac_roman')

    with datei:
        schreiber = csv.writer(datei, dialect="semik.", lineterminator='\n', delimiter=";")    #schreiber erstellen

        for zeile in arrC:       #jede Zeile aus array in for schleife schreiben
            if zeile != [0, 0, 0, 0, 0, 0, 0, 0] and zeile != ['', '', '', '', '', '', '', '']:  # verhindert schreiben von leeren zeilen

                if indexZähler != 0:            #damit Header 'ID' gleich bleibt
                    zeile[0] = indexZähler      #anpassung ID-Wert
                schreiber.writerow(zeile)
                indexZähler += 1

#Funktionen ausführen

füllenArray()

erkennenDoppelteDatensätze()

schreibenDatei()
