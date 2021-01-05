#Aufgabe3
with open('File_B_In2019_L.csv', encoding='mac_roman') as csvdatei, open('2.csv','w') as out_file:
    seen = set() # set for fast O(1) amortized lookup
    for line in csvdatei:
        if line in seen: continue # skip duplicate

        seen.add(line)
        out_file.write(line)