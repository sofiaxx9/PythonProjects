text= "ahoj"
text2 = 'sybau'
text3 = "O'Connery"
text4 = 'ty mas urcite "tism" ze'
text5 = '\'tism '
text6 = "musis naklikat: \\autism.cz\\"
text7 = "fine \n shyt"
print (text)
print (text2)

a= "shut"
b= "ur"
c= "ba"
d= "up"

print(a+d)

e= "a"
for i in range(5):
    c=c+"a"
print(c)

promenna = "shush ty autisto"
print(promenna[4]) #indexovani od 0!!!!!!!!!!!!!!!!!!!(0 1 2 0 3 4.....)
for i in range (len(promenna)):
    print(promenna[i])
print(len(promenna))

print(promenna[len(promenna)-1])
print(promenna[-1])

print(promenna[5:10]) #slicing= promenna [a:b]-znaky z intervalu <a;b)
print(promenna[5:10:2])
print(promenna[10:5:-2])
print(promenna[5:]) #kdyz tam neni ta druha promenna tak to znamena az do konce nebo od zacatku(viz dole)
print(promenna[:5])
print(promenna[:5:-1]) #na to prazdny doplni to nejvetsi cislo
print(promenna[::-1]) #na to prvni prazdny doplni to nejvetsi na to druhy prazdny nejmensi

print(promenna.index("au"))