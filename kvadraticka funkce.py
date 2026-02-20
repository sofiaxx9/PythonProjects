def kvadr(a, b, c):
    diskriminant = (b**2)-4*a*c



    if diskriminant < 0:
        return("neni")
    elif diskriminant > 0:
        rovnice1 = (-b + (diskriminant ** (1 / 2))) / 2 * a
        rovnice2 = (-b - (diskriminant ** (1 / 2))) / 2 * a
        return [rovnice1, rovnice2]
    else:
        nula = -b / (2 * a)
        return nula


#print(kvadr(1,2,1))
#print(kvadr(1,3,1))
#print(kvadr(1,1,1))

def kvadratick_test():
    results=[]
    for i in range(5):
        results.append(kvadr(1,i,1))
    return results

vysledky=kvadratick_test()
for vysledek in vysledky:
    print(vysledek)