import numpy as np
import matplotlib.pyplot as plt


weight = np.genfromtxt("https://raw.githubusercontent.com/gagolews/teaching-data/master/marek/nhanes_adult_female_weight_2020.txt")
counts, bins, __not_important = plt.hist(weight, bins=11,
    color="lightgray", edgecolor="red")
plt.ylabel("Count")
plt.show()

#plt.hist
#numpy.histogram 