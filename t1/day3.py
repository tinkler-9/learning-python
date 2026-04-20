import math


x = 1+2j
print(type(x))
#help("complex")
print(abs(x))
#print(x.abs)
print(complex(real=1, imag=2))
print(x.conjugate())
print(5**0.5)
print(abs(-5))
#print(abs((3,4)))
print(x.real)  # access slot `real` of object `x` of the class `complex`
print(x.imag)
print("egga" < "eggaf")
print(math.sin(math.pi))
print(abs(math.sin(math.pi)))
# Assuming that p, q, r are logical and a, b, c, d are variables of the type float, simplify the following expressions:
# Here are the simplified forms of each logical expression, using the rules of Boolean algebra (like De Morgan's laws) and relational operators:
# 1. not not p
# Simplified: p
# Explanation: This is the rule of Double Negation. Two "nots" cancel each other out.
# 2. not p and not q
# Simplified: not (p or q)
# Explanation: Applying De Morgan's laws, factoring out the not changes the and to an or. This reduces the number of logical operators from three to two.
# 3. not (not p or not q or not r)
# Simplified: p and q and r
# Explanation: Applying De Morgan's laws, we distribute the outer not into the parentheses. This negates all the variables (turning not p into p, etc.) and flips the or operators to and operators.
# 4. not a == b
# Simplified: a != b
# Explanation: The negation of "equal to" is simply "not equal to".
# 5. not (b > a and b < c)
# Simplified: b <= a or b >= c
# Explanation: Applying De Morgan's laws. We negate the individual conditions (the opposite of > is <=, and the opposite of < is >=) and flip the and to an or.
# 6. not (a >= b and b >= c and a >= c)
# Simplified: a < b or b < c
# Explanation: First, notice that by the transitive property, if a >= b and b >= c, then a >= c is mathematically guaranteed to be true. Therefore, the inner expression is logically equivalent to just a >= b and b >= c.
# Applying De Morgan's laws to negate this simplified inner expression gives us a < b or b < c.
# 7. (a > b and a < c) or (a < c and a > d)
# Simplified: a < c and (a > b or a > d)
# Explanation: Both sides of the or contain the exact same condition (a < c). By using the distributive property of Boolean algebra, we can factor out the common term a < c, requiring fewer comparisons.