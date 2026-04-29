x = ["one", "two", "three", "four", "five"]
print(x[1:4])  # from the second to the fifth (exclusive)
print(x[-1:0:-2])  # from the last to first (exclusive) by every second backwards
print(x[3:])  # from the third element to the end
print(x[:2])  # the first two
print(x[:0])  # none (the first zero)
print(x[::2])  # every second element from the start
print(x[::-1])  # the elements in reverse order
"spam, bacon, spam, and eggs"[13:17]  # fetch a substring
print(x[0])  # extraction (indexing with a single integer)
print(x[0:1])  # subsetting (indexing with a slice)

l=[1,2,3,4,5]
l=l[::-1]
print(l)
print("0123456789"[5:9])
