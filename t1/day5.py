def min3(a, b, c):
    """
    A function to determine the minimum of three given inputs.

    By the way, this is a docstring (documentation string);
    call help("min3") later to view it.
    """
    if a < b:
        if a < c:
            return a
        else:
            return c
    else:
        if b < c:
            return b
        else:
            return c
print(min3(30, 40, 90))

height=1.68
weight=53
BMI=weight/height**2
def bmi(height,weight):
    """
    A function that returns the Body Mass Index (BMI) based on height in meters and weight in kilograms.
    """
    return round(weight/height**2, 3)
print(bmi(1.68,53))

def max3(a,b,c):
    """
    a function, which determines the maximum of three given values.
    """
    m=a
    if b>m:
        m=b
    if c>m:
        m=c
    return m
print(max3(20, 40, 15))
def med3(a,b,c):
    """
    Write a function med3 which defines the median of three given values (the value that is in-between two other ones).
    """
    if a<b:
        if a<c:
            if b<c:
               m=b
            else:
                m=c
        else:
            m=a
    else:
        if a>c:
           if b>c:
              m=b
           else:
               m=c
        else:
            m=a
               
    return m


print(med3(2, 3, 4) == 3)
print(med3(2, 4, 3) == 3)
print(med3(3, 2, 4) == 3)
print(med3(3, 4, 2) == 3)
print(med3(4, 3, 2) == 3)
print(med3(4, 2, 3) == 3)
    

my_list = [4,5,8,1]
print(my_list * 2)

def min4(a, b, c, d):
    """
    A function to determine the minimum of 4 given inputs
    (alternative version).
    """
    m = a  # a local (temporary/auxiliary) variable
    if b < m:
        m = b
    if c < m:   # be careful! no `else` or `elif` here — it's a separate `if`
        m = c
    if d<m:
        m=d
    return m
print(min4(2, 3, 4,5) == 2)
print(min4(2, 3, 5,4) == 2)
print(min4(2, 4, 3,5) == 2)
print(min4(2, 4, 5,3) == 2)
print(min4(2, 5, 4,3) == 2)
print(min4(2, 5, 3,4) == 2)

print(min4(3, 2, 4,5) == 2)
print(min4(3, 2, 5,4) == 2)
print(min4(3, 4, 5,2) == 2)
print(min4(3, 4, 2,5) == 2)
print(min4(3, 5, 4,2) == 2)
print(min4(3, 5, 2,4) == 2)

from itertools import permutations

perm = permutations([2, 3, 4, 5])
for p in perm:
    print(f"min4({p[0]}, {p[1]}, {p[2]}, {p[3]}): {min4(p[0], p[1], p[2], p[3]) == 2}")

def med3vol2(a,b,c):
    m=[a,b,c]
    m.sort()
    return m[1]
print(med3vol2(2, 3, 4) == 3)
print(med3vol2(2, 4, 3) == 3)
print(med3vol2(3, 2, 4) == 3)
print(med3vol2(3, 4, 2) == 3)
print(med3vol2(4, 3, 2) == 3)
print(med3vol2(4, 2, 3) == 3)

for i1 in range(2,6):
     for i2 in range(2,6):
         for i3 in range(2,6):
             for i4 in range(2,6):
                 # if i1!=i2 and i2!=i3 and i3!=i4 and i1!=i3 and i1!=i4 and i2!=i4:
                 if len({i1, i2, i3, i4}) == 4:
                     print(f"i1={i1},i2={i2},i3={i3},i4={i4}", min4(i1,i2,i3,i4) == 2)

def print_x_and_fx(x, f):
    """
    Arguments: x - some object; f - a function to be called on x
    """
    print(f"x = {x} and f(x) = {f(x)}")
import math
print_x_and_fx(4, lambda x: x**2)
## x = 4 and f(x) = 16
print_x_and_fx(math.pi/4, lambda x: round(math.cos(x), 5))
## x = 0.7853981633974483 and f(x) = 0.70711

sqr = lambda x: x**0.5
a=4
print(f"sqr {a} = {sqr(a)}")

print(range(0))