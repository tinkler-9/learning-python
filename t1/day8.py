import requests
x = requests.get("https://api.github.com/users/gagolews/starred").json()
print(type(x))
print(len(x))
print(x[0]['id'])
print(len(x[0]))
"""id
name
owner login"""
print("#\tid\t\tname\t\towner")
for y in range(0,len(x)):
    #print(y)
    print(f"{y}\t{x[y]['id']}\t\t{x[y]['name']}\t\t{x[y]['owner']['login']}")
    

print('---------------------------------111')
for y in x:
    #print(y)
    print(f"{y['id']:20} {y['name']:20} {y['owner']['login']:20}")


print('---------------------------------')    
z = [{"id":y['id'], 'name':y['name'], 'owner': y['owner']['login']} 
     for y in x]
print(z)

print('---------------------------------')   
w = [u + 1 for u in [1, 2, 3]]
print(w)

w = []
for u in [1, 2, 3]:
    w.append(u+1)
