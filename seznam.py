#list,pole prvku
promenna = [1,2,3,4,5]
print(promenna)

p2 = [1,"abc",5.5,True,[1,2,"a"]]
print(p2)
print(type(p2))
print(p2[2])
print(type(p2[2])) #float

print((p2[0]))
print(type(p2[0])) #integer

print((p2[1]))
print(type(p2[1]))#string

x=[1,2,8,4,6,11,7,4]

for i in range(len(x)):
    print(x[i])

for i in range(len(x)):
    if i%2 == 0:
     print(x[i])