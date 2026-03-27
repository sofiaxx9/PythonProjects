import matplotlib.pyplot as plt

labels=["prvaci", "druhaci", "tretaci", "ctvrtaci"]
values=[100,80,60,40]
y=[80,75,6,45]
plt.bar(labels,values, label="sloupce")
plt.plot(labels,y,linestyle="--", label="cara", color="red")
plt.title("pocet vyhozenych studentu")
plt.legend()
plt.show()