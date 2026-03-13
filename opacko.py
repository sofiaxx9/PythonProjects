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
#2. funkce zjisti jestli je cislo prvocislo
#-vstup: cislo
#vystup: logicka promenna True nebo False
def je_prvocislo(n):
    if n < 2:
        return False
#for i in range (2,int(n**(1/2)+1):
    for i in range(2,n):
        if n % i == 0:
            return False
    return True
print(je_prvocislo(12))
print(je_prvocislo(7))
print(je_prvocislo(2))
#print(je_prvocislo(int(input("zadej cislo"))))

#3. funkce ktera spocita prvocisla v seznamu
#vstup: list (seznam celych cisel)
#vystup: cislo (pocet prvocisel)

def pocet_prvocisel(seznam_cisel):
        count=0
        for i in muj_seznam:
            if je_prvocislo(i):
                count+=1
        return count
muj_seznam = [5, 13, 31, 55, 17, 54]
print(pocet_prvocisel(muj_seznam))

def adding(a,b):
    return a + b
def subtracting(c,d):
    return a - b
def calculate(funkce,x,y):
    return funkce(x,y)
print("***************")
print(calculate(adding,2,3))
print(calculate(subtracting,2,3))

pejser= int(input("zadej cislo"))
koci=int(input("zadej dalsi cislo"))
ptacek=input("zadej funkci (+/-)")
 if ptacek == "+":
     print(calculate(adding,pejser, koc))
elif ptacek == "-":
else:
print("neznam")