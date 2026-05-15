print(list([1,2,3,4]))
print(list((1,2,3,4)))
print(list('hamster'))
print(list(range(0,8)))

#help(enumerate)

print(enumerate([1,2,3,4,5]))
print(tuple(enumerate([11,2,3,4,5])))
i = enumerate([11,2,3,4,5])
print(i.__next__())
print(i.__next__())
print(i.__next__())
print(enumerate([1,2,3,4,5]))

i = "хомяк".__iter__()
print(i)
print(i.__next__())
print(i.__next__())

i = iter('hamster')
try:
    while True:
        print(next(i))
except StopIteration:
    print("that's all")


for p in range(1, 25, 2):
    print(p)



