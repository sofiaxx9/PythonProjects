#funkce ktera vrati 2. nejvetsi cislo v seznamu

def druhy_nej(x):
    if x[0]>x[1]:
        cislo1 = x[0]
        cislo2 = x[1]
    else:
        cislo1 = x[1]
        cislo2 = x[0]

    for i in range(2, len(x)):
        if x[i]>cislo1:
            cislo2=cislo1
            cislo1=x[i]
        elif x[i]>cislo2:
            cislo2=x[i]
    return cislo2
seznam = [9,3,4,8,5, 6, 7]

print(druhy_nej(seznam))

#je cislo prvocislo?

def cislo(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

print (cislo(3))
