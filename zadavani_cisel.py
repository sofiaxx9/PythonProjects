cislo_jako_text=input("zadej cislo: ")

try:
    cislo=int(cislo_jako_text)
except:
    cislo=0

print("zadane cislo + 10 = "+str(cislo+10))

#zadavani hesla do ty doby nez to bude dobre
while True:
    cislo_jako_text = input("zadej cislo: ")
    try:
        cislo=int(cislo_jako_text)
        break
    except:
        print("neni cislo")
print("zadane cislo + 10 = "+str(cislo+10))