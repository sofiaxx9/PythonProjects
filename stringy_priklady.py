#vypiste jednotlive znaky pod sebe (pomoci for-cyklu)
promenna = "ahoj karle, jak se mas?"
for i in range(len(promenna)):
    print(promenna[i])

#totez, ale pozpatku
for i in range(len(promenna)):
    print(promenna[-i-1])

#pyramida znaku
for i in range(len(promenna)):
    print(promenna[:i+1])

#po dvou pismenkach
for i in range(len(promenna)-1):
    print(promenna[i:i+2])

#po trech
for i in range(len(promenna)-2):
    print(promenna[i:i+3])

#vypiste vedle sebe vzdy prvni a posledni pismenko, pak druhy a predposledni, skoncime v pulce textu
for i in range(int(len(promenna)/2)+1): #musi tam byt ten int(integer- dela cely cislo tim ze tu desetinnou cast proste odhodi a NEZAOKROUHLUJE) a ne flow
    print(promenna[-i-1])
print(int(5.9))

#promenna = promenna.replace("a","x")

a = "    yoloyolo "
print(a)
print(a.strip())

a="5"
print(a.zfill(5))