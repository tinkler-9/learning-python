# Welcome to your Python project!
print("Hello word")
alphabet=['a','b','c']
print(alphabet)
letters = ['a', 'b', 'c']
print(letters[2])
top_imdb_movies = ['The Shawshank Redemption', 'The Godfather', 'The Dark Knight']
i=1
for x in top_imdb_movies:
  print(str(i)+". "+x)
  i=i+1
[(1, "a"), (2, 'b')]
[print(f"{i+1}. {x}") for (i, x) in enumerate(top_imdb_movies)]
def concatenate_strings(string_one, string_two):
  cs=string_one+" "+ string_two
  return cs

print(concatenate_strings("Hello", "world"))
print(concatenate_strings("Bonjour", "le monde"))
le_wagon_team = [
    {'name': 'Ben', 'age': 31, 'country': 'France', 'hobbies': ['coding', 'biking']},
    {'name': 'Quinn', 'age': 26, 'country': 'Ireland', 'hobbies': ['skiing']},
    {'name': 'Sasha', 'age': 24, 'country': 'Lebanon', 'hobbies': ['sports']},
    {'name': 'Alex', 'age': 28, 'country': 'Austria', 'hobbies': []}
]
for x in le_wagon_team:
    if x['name']=='Sasha':
        print(len(x['hobbies']))

for x in le_wagon_team:
    if x['name']=='Alex':
        x['hobbies']='video games'
print(le_wagon_team)

ages = [17, 18, 20, 21, 48]
for age in ages:
    if age >= 18 and age < 21:
        print(f'You are {age}, you can vote')
    elif age >= 21:
        print(f'You are {age}, congrats, you can be President!')
    else:
        print(f'You are {age}, you cannot vote yet')
