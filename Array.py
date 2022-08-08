""" numbers1 = [1, 2, 3, 4, 5] # разные способы создания списков
numbers2 = []
numbers3 = list()
people1 = ['Gasan'] * 3
people2 = ['Gasan', 'Muhtar', 'Kurban']
people2[2] = 'Dolbaeb'

print(people1)
print(people2[0]) # обращение к элементам списка
print(people2[2])

gasan , muhtar, kurban = people2 # разложение списка
print(gasan)
print(muhtar)
print(kurban)

for person in people2: # перебор элментов списка
    print(person)

people2.append('Magomed') # методы и функции работы со списками
people2.insert(1, 'gusen')
if 'Gasa' in people2: 
    people2.remove('Gasa')
people2.sort()
people2.reverse()

print(people2)

people3 = sorted(people2, key=str.lower) # сортировка без без учета индекса
print(people3)

people4 = people2.copy() # глубокое копирование 
people4.append('Murat')
print(people4)


gas1 = ('Gasan', 27, 'Google', 'Darginez') # разные способы создания кортежа, обращение к элементам кортежа такое же как у списков
gas2 = 'Gasan', 27
gas3 = ('Gasan', )

print(gas1[1:2]) #получения подкортежа

def get_user(): # кортеж как результат функции
    name = 'Gasan'
    age = 27
    gender = 'Man'
    return name, age, gender

user = get_user()
print(user)

def print_person(name, age, gender):
    print(f'Name: {name}, Age: {age}, Gender: {gender}')

gusen = ('Gusen', 21)
print_person(*gusen, 'Man') # кортеж как параметр функции

for i in range(1,10): # пример использоывания диапазонов
    for j in range(1, 10):
        print(i * j, end='\t')
    print('\n') """


users1 = {1: 'Gasan', 2: 'Muhtar', 'Dolbaeb': 'Kurb'}
users2 = {}
users3 = dict()
user_list = [
    [1, 'Gasan'],
    [2, 'Muhtar'],
    [3, 'Kurban']
]

user_list = dict(user_list)
print(user_list)
users1['Dolbaeb'] = 'Ne Kurban'
print(users1['Dolbaeb'])

userss = users1.get('Dolbae', 'Error')
print(userss)
del users1['Dolbaeb']
print(users1)

students = users1.copy()
students.update()
print(students)

users = {
    'Men':{
        '1': 'Gasan',
        '2': 'Muhtar'
    },
    'kids':{
        '1': 'Israfil',
        '2': 'Dzhabrail'
    }
}

print(users)
print(users['kids']['1'])