import matplotlib.pyplot as plt

x = [5,7,8,7,2,17,2,9]
y = [99,86,87,88,111,86,103,87]
plt.scatter(x,y)
plt.show()
x1=[1,2,3]
y1=[2,3,4]

x2=[1,2,3]
y2=[5,1,2]

x3=[1,3,5]
y3=[1,4,5]

plt.scatter(x1,y1, color="red",s=100,  marker="o", label="data1")
plt.scatter(x2,y2, color="green", marker="s", label="data2")
plt.scatter(x3,y3, color="blue", marker="^", label="data3")

plt.grid()
plt.legend()
plt.xlabel("cas [s]")
plt.ylabel("hodnota")
plt.show()