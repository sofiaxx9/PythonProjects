pole =[5,2,9,1,7,3,10,6,4]

#najdi pozici a hodnotu nejvetsiho prvku v poli
maximalni_prvek= pole[0] #nastavim maximalni prvek-pomocna promenna
pozice_max_prvku=0 #nastavim pozici max prvku 0
for i in range(1, len(pole)): #0 prvek je uz nastaveni takze ignoruju proto napisu 1- zacnu od 1
    if maximalni_prvek<pole[i]: #pokud je i-ty prvek vetsi nez dosavadni
        maximalni_prvek=pole[i] #nastavim max na i-ty prvek
        pozice_max_prvku=i #nastavim tu max pozici na i

print("{} je maximalni prvek a je na pozici {}".format(maximalni_prvek,pozice_max_prvku))

#najdi pozici a hodnotu nejmensiho prvku v poli
minimalni_prvek= pole[0] #nastavim min prvek-pomocna promenna
pozice_min_prvku=0 #nastavim pozici min prvku 0
for i in range(1, len(pole)): #0 prvek je uz nastaveni takze ignoruju proto napisu 1- zacnu od 1
    if minimalni_prvek>pole[i]: #pokud je i-ty prvek mensi nez dosavadni
        minimalni_prvek=pole[i] #nastavim min na i-ty prvek
        pozice_min_prvku=i #nastavim tu min pozici na i

print("{} je minimalni prvek a je na pozici {}".format(minimalni_prvek,pozice_min_prvku))

pole =[5,2,9,1,7,3,1,6,4]
minimalni_prvek= pole[0]
pozice_min_prvku=0
for i in range(1, len(pole)):
    if minimalni_prvek>=pole[i]: #zmena ze kdyz tam napisu mensi rovno a je tam vickrat to samy maly cislo tak to vezme tu posledni pozici kde toje
        minimalni_prvek=pole[i]
        pozice_min_prvku=i

print("{} je minimalni prvek a je na pozici {}".format(minimalni_prvek,pozice_min_prvku))


pole =[5,2,9,1,7,3,10,6,4]

#vypocitejte prumernou hodnotu vsech prvku v poli
soucet= pole[0]

for i in range(1,len(pole)):
    soucet=soucet+pole[i]

print(soucet/len(pole))

#neebo
soucet=0
for i in range(len(pole)):
    soucet=soucet+pole[i]

print(soucet/len(pole))

#zjistete kolik prvku je v poli vetsi nez 5
pocitadlo=0
limit=5
for i in range(len(pole)):
    if pole[i]>limit:
        pocitadlo +=1

print("pocet prvku vetsich nez "+str(limit)+" je: "+str(pocitadlo))

#soucet vsech prvku
soucet=0
for i in range(len(pole)):
    soucet=soucet+pole[i]

print(soucet)

#vytvor nove pole ktere bude obsahovat prvky v obracenem poradi
nove_pole=[]
for i in range(len(pole)-1,-1,-1):
    nove_pole.append(pole[i])  # append-nove pole

print(nove_pole)

#neboo
nove_pole=[]
for i in range(len(pole)):
    nove_pole.append(pole[-i-1])

print(nove_pole)
