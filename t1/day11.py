x = [1, "two", ["three", 3j, 3], False]  # some iterable object
for i in range(len(x)):  # for i = 0, 1, ..., len(x)-1
    print(i, x[i], sep=": ")  # sep (label separator) defaults to " "

x = [1,  2,   3,    4,     5]  # for testing
y = [1, 10, 100, 1000, 10000]  # just a test
z = []  # result list – start with an empty one
for i in range(len(x)):
    tmp = x[i] * y[i]
    print(f"The product of {x[i]:6} and {y[i]:6} is {tmp:6}")
    z.append(tmp)
print(z)

map = dict(  # from=to
    apple="red",
    pear="yellow",
    kiwi="green",
)
x = ["apple", "pear", "apple", "kiwi", "apple", "kiwi"]
recoded_x = []
for fruit in x:
    recoded_x.append(map[fruit])  # or, e.g., map.get(fruit, "unknown")
print(recoded_x)

import math
def mymin(x):
    """
    Fetches the smallest element in an iterable object x.
    We assume that x consists of numbers only.
    """
    curmin = math.inf  # infinity is greater than any other number
    for e in x:
        if e < curmin:
            curmin = e  # a better candidate for the minimum
    return curmin

print(mymin([0, 5, -1, 100]))
print(mymin(range(5, 0, -1)))
print(mymin((1,)))
print("bc"<"c")

def myminstr(x):
    """
    Fetches the smallest element in an iterable object x.
    We assume that x consists of strings only.
    """
    curmin = x[0]  # infinity is greater than any other number
    for e in x:
        if e < curmin:
            curmin = e  # a better candidate for the minimum
    return curmin

print(myminstr(["mamas", "mamasita","mama"]))
print(myminstr([0, 5, -1, 100]))
print(myminstr(range(5, 0, -1)))
print(myminstr((1,)))

#max, sum, any, and all
def mymax(x):
    """
    """
    curmin = x[0]  
    for e in x:
        if e > curmin:
            curmin = e  
    return curmin
print(mymax(["mamas", "mamasita","mama"]))
print(mymax([0, 5, -1, 100]))
print(mymax(range(5, 0, -1)))
print(mymax((1,)))

def mysum(x):
    """
    """
    y=x[0]
    for e in range(1, len(x)):
        y=y+x[e]
    return y

def denis_sum(x):
    """
    """
    y=None
    for e in x:
        if y is None:
            y = e
        else:
            y=y+e
    return y
print(denis_sum([1,3,5]))
print(denis_sum(range(1, 7, 2)))
print(denis_sum(["mamas", "mamasita","mama"]))
print(bool("") == False)
def myall(x):
    """
    """
    for e in x:
        if bool(e) == False:
            return False
    return True
print(myall([1,2,0,3]), "should be false")
print(myall([1,2,4,3]), "should be true")
print(myall(range(1, -4, -1)), "should be false")
print(myall(range(1, 4, 1)), "should be true")
print(myall(["mama", "papa", "", "homyak"]), "should be false")
print(myall(["mama", "papa", "homyak"]), "should be true")
print(myall([["mama"], ["papa"], [], ["homyak"]]), "should be false")
print(myall([["mama"], ["papa"], ["homyak"]]), "should be true")
def myany(x):
    """
    """
    for e in x:
        if bool(e):
            return True
    return False