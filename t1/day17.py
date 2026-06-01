import numpy as np
import matplotlib.pyplot as plt
heights = np.genfromtxt("https://raw.githubusercontent.com/gagolews/" +
    "teaching-data/master/marek/nhanes_adult_female_height_2020.txt")
counts, bins, __not_important = plt.hist(heights, bins=11,
    color="lightgray", edgecolor="red")
plt.ylabel("Count")
#plt.show()
print(bins)
print(counts)