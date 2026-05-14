x=dict(a=[1, 2, 3], b=7, z="spam!", c=None)
## {'a': [1, 2, 3], 'b': 7, 'z': 'spam!'}
print(x)
print(f"x[a]={x["a"]}")
## [1, 2, 3]

print("a" in x, 0 not in x, "z" in x, "w" in x ) # a tuple of four tests' results
## (True, True, True, False)

print(x.get("a"))
## [1, 2, 3]
print(x.get("c"))  # if missing, returns None by default
print(x.get("c") is None)  # indeed
## True
print(x.get("c1", "unknown"))
## 'unknown'

x["f"] = "more spam!"
print(x)
## {'a': [1, 2, 3], 'b': 7, 'z': 'spam!', 'f': 'more spam!'}