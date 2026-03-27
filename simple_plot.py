import numpy as np
import matplotlib.pyplot as plt

y=[1,7,3,-5,7,6]
y2=[2,5,6.5,8.9,6,5]
x=[1,3,5,7,9,11]
plt.plot(x,y,label="U [V]")
plt.plot(x,y2, label="I [mA]")
plt.xlabel("t [s]")
plt.ylabel("hodnota")
plt.title("graf elektriky v case")
plt.legend()
plt.show()