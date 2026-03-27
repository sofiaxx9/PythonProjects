import matplotlib.pyplot as plt
x=[1,2,3,4]
y=[10,20,30,35]

plt.subplot(1,2,1)
plt.plot(x,y)
plt.title("plot1")

plt.subplot(2,1,2)
plt.bar(x,y)
plt.title("plot2")
plt.show()