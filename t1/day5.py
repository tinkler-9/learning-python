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