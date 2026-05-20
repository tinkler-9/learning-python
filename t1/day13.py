x = { "a": 1, "b": ["spam", "bacon", "spam"] }
print(list(x.items()))  # just a demo
## [('a', 1), ('b', ['spam', 'bacon', 'spam'])]


for k, v in x.items():   # or: for (k, v) in x.items()...
    print(k, v, sep=": ")
## a: 1
## b: ['spam', 'bacon', 'spam']
for a, b, *c, d in [range(4), range(10), range(3)]:
    print(a, b, c, d, sep="; ")

x=[3,4,5,6,7]
print("------")
print(x[0], x[1], x[:0], x[1:3])