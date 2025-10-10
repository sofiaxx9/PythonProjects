print("ahojks")

odpoved = input("do radky:")
print(odpoved)
print(type(odpoved))
try:
    odpoved_jako_cislo = int(odpoved)
except:
    print("ajajajajjj umis pekny nic zas, pisu 0")
    odpoved_jako_cislo = 0
odpoved_jako_cislo = int(odpoved)
#odpoved_jako_cislo = float(odpoved)
print("ahojks" + "lubrikone")
print(67 + odpoved_jako_cislo)
