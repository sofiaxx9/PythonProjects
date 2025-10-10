vstup = input("zadej cislo: ")
try:
    cislo = int(vstup)
except:
    cislo = 0

print("vstup = " + vstup)

if cislo > 5:
    print("cislo")
    print(cislo)
    print("je")
    print("vetsi nez 5 ty demente")
if cislo > 10:
    print("skrtim se")
else:
    print("fakt neni vetsi nez 5")
if cislo < 67:
        print("cislo je mensi nez 67 logicky")
print("konec")

a = input("zadej A")
b = input("zadej B")
c = input("zadej C")

# AX^2+BX+C=0

d= b**2 - 4*a*c
print("nula reseni v R.")
print("jedno reseni v R.")
print("dve reseni v R.")

if d > 0:
    print("dve reseni v R.")
elif d == 0:
    print("jedno reseni v R.")
else:
    print("nula reseni v R.")