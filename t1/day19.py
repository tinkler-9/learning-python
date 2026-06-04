import numpy as np
import matplotlib.pyplot as plt
income = np.genfromtxt("https://raw.githubusercontent.com/gagolews/" +
    "teaching-data/master/marek/uk_income_simulated_2020.txt")
a=[]
for x in range(0, 7):
    a.append(x*20000)
a.append(140000)
a.append(200000)
print(a)
b = [x * 20000 for x in range(0, 8)] + [200000]
print(b)
plt.hist(income, a, color="lightgray", edgecolor="red")
plt.ylabel("Count")
plt.show()

plt.subplot(1, 2, 1)  # one row, two columns; the first plot
plt.hist(income, bins=5, color="lightgray", edgecolor="black")
plt.ylabel("Count")
plt.subplot(1, 2, 2)  # one row, two columns; the second plot
plt.hist(income, bins=200, color="lightgray", edgecolor="black")
plt.ylabel(None)
#plt.show()