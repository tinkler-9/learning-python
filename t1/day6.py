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
l1=l[::-1]
print(l1)
print("0123456789"[5:9])

l.reverse()
print(l)
l.clear()
print(l)
l.extend([1,2,3,4,5,6])
print(l)
l2=l.copy()
print(l2)
l[0]=7
print(l2)
print(l)
print(x.count("one"))
print(x.index("five"))
l.insert(3,33)
print(l)
'''
help("list")
append(self, object, /)
 |      Append object to the end of the list.
 |
 |  clear(self, /)
 |      Remove all items from list.
 |
 |  copy(self, /)
 |      Return a shallow copy of the list.
 |
 |  count(self, value, /)
 |      Return number of occurrences of value.
extend(self, iterable, /)
 |      Extend list by appending elements from the iterable.
 |
 |  index(self, value, start=0, stop=9223372036854775807, /)
 |      Return first index of value.
 |
 |      Raises ValueError if the value is not present.
 |
 |  insert(self, index, object, /)
 |      Insert object before index.
 |
 |  pop(self, index=-1, /)
 |      Remove and return item at index (default last).
 |Raises IndexError if list is empty or index is out of range.
 |
 |  remove(self, value, /)
 |      Remove first occurrence of value.
 |
 |      Raises ValueError if the value is not present.
 |
 |  reverse(self, /)
 |      Reverse *IN PLACE*.
 |
 |  sort(self, /, *, key=None, reverse=False)
 |      Sort the list in ascending order and return None.
The sort is in-place (i.e. the list itself is modified) and stable (i.e. the
 |      order of two equal elements is maintained).
 |
 |      If a key function is given, apply it once to each list item and sort them,
 |      ascending or descending, according to their function values.
 |
 |      The reverse flag can be set to sort in descending order.
 '''