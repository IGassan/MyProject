""" print(2 + 3) # сложение 
print(7 / 2) # деление 
print(7 // 2) # целочисленное деление
text = '''My name  
is Gasan.''' # многострочный вывод
print(text)

message = 'My name is Gasan'
gasan = 'Gasan'
print(gasan in message) # нахождение определенного значения в наборе значений

age = int(input('Enter your age: '))
name = input('Enter your name: ')
if age < 18: # использование условного оператора if
    print(f'Your name is {name} and you are {age} years old. You are underage')
else:
    if age < 65: # использование вложенного оператора if
        print(f'Your name is {name} and you are {age} years old. You are of legal age')
    else:
        print(f'Your name is {name} and you are {age} years old. You are a pensioner') """

""" number = 1 # использование цикла while
while number < 5:
    print(f'number: {number}')
    number += 1
else:
    print(f'number: {number}. Конец цикла.')
print('Конец программы') """

""" for i in range(1, 10): # использование цикла for
    for j in range(1, 10):
        print(i * j, end='\t')
        j += 1
    print('')
    i += 1 """

def person(name, age): # использование функций с параметрами
    if age < 1 or age > 120:
        print('Неправильный возраст')
    else:
        print(f'Your name : {name}. Your age: {age}')


person(age = 125, name = 'Gasan')
