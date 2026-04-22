import numpy as np

x = np.random.rand() 
if x < 0.5:
    print("spam!")
    print("ham!")    # :(

count = 0
sum=0
while  count<100:
    sum=np.random.rand()+sum
    count = count + 1
print(sum/count)
print(sum)
print(count)