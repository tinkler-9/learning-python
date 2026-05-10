a = [2,3,4]
b = a 
print(hex(id(a)))
print(hex(id(b)))
a.append(6)
print(hex(id(a)))
a = a + [4]
print(hex(id(a)))
print(a)
print(b)



print('-----------')

p = [2000,3000,4000]
print(hex(id(p)))
q = p.copy()
print(q)
print(hex(id(q)))

print('--------')
z = {"a":3, "b":4}
x = [z, {"c":5, "d": 6}]
y = x.copy()
print(y)

z['a'] = 7
x[0] = [{"t": 89}]
print(y)

from copy import deepcopy
w = deepcopy(x)
z['a'] = 9
print(w)

print('-----------')

aa = [[2,3], [4,5]]
ab = aa.copy()

ab = [aa[0], aa[1]]
aa[0][1] = 4
aa[0] = [5,6]
print(ab)

ptr1 = [ptr2, ptr3]
ptr2 = [2,3]
ptr3 = [4,5]
aa -> ptr1

ptr4 = [ptr2, ptr3]
ab -> ptr4

aa[0][1] = 4
ptr2 = [2,4]

aa[0] = [5,6]
ptr5 = [5,6]
ptr1 = [ptr5, ptr3]

