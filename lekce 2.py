def secti(a, b):
    globalni_promnena = 20
    vysledek = a+b+globalni_promnena
    return [vysledek, globalni_promnena]

# [] list
#list[0]
#list[1]
#tuple = list ale nahovno basically, nemuzes menit hodnoty


globalni_promnena = 10
y = secti(5, 3)
print(y)
print(globalni_promnena)


def secti_tuple(a, b):
    globalni_promnena = 20
    vysledek = a + b + globalni_promnena
    return vysledek, globalni_promnena

globalni_promnena = 10
y = secti(5, 3)
print(y)
print(type(y))
print(secti_tuple(5, 3))
print(type(secti_tuple(5, 3)))

y[1] = 20
print(y)

z = secti_tuple(3, 3)
print(z)
