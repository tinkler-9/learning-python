x=[2,5,8,0]
z=[]
for y in x:
    z.append(y**2)
print(z)

print([1,2]+[3,4])
print("str"*3)
print([1,2]*3)
import numpy as np
heights = np.genfromtxt("https://raw.githubusercontent.com/gagolews/" +
    "teaching-data/master/marek/nhanes_adult_female_height_2020.txt")
heights[:6]
print(heights[:6])