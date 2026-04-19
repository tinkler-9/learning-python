print('-----------------')
i=0
list5=[6,2,3,4,5]

y=[]
for i in range(0,len(list5)//2):
    var=list5[len(list5)-1-i]
    var1=list5[i]
    list5[i]=var
    list5[len(list5)-1-i]=var1
print(list5)
print('-----------------')

#Exercise 2.1 o the power of …”. Additionally, 1_000_000
print('-----------------')
print(1.23e-4)
print(9.8e5)
print(1_000_000)
print('-----------------')
#Exercise 2.2. Define two named variables height (in centimetres) and weight (in kilograms). Determine the corresponding body mass index (BMI).
height=1.68
weight=53
BMI=weight/height**2
print(BMI)
print('-----------------')
#Exercise 2.3 Call the print function on the above objects to reveal the meaning of the included escape sequences.
a="""
spam\\spam
tasty\t"spam"
lovely\t'spam'
"""
print(a)
print('-----------------')
π = 3.14159265358979323846
e = 2.71828182845904523536
print(f"""
π   = {π:10.10f}
e   = {e:10.8f}
πe² = {(π*e**2+100):10.2f}
""")
print(f"a=12345678901234567890")
print(f"a={12345.678901:10.6f}")
print('-----------------')

#help("round")
print(round(e,10))
import math   # the math module must be imported before we can use it
print(math.log(2.718281828459045))  # the natural logarithm (base e)
## 1.0
print(math.floor(-7.5))  # the floor function
## -8
print(math.sin(math.pi))  # sin(pi) equals 0 (with small numeric error)
## 1.2246467991473532e-16
print(math.pi)
import numpy as np
print(np.random.rand())