def print_hello(language): # конструкция match
    match language:
        case 'russian':
            print('Привет')
        case 'english' | 'british english':
            print('Hello')
        case 'german':
            print('Hallo')
        case _:
            print('Underfined')


print_hello('spanish')
print_hello('british english')
print_hello('russian')
print_hello('english')



def print_data(user): # использование кортежей в качестве параметов
    match user:
        case ('Gasan' | 'Gusen', 27):
            print('Default user')
        case ('Gasan', age):
            print(f'Age: {age}')
        case (name, 22):
            print(f'Name: {name}')
        case (name, age):
            print(f'Name: {name}, Age: {age}')
        case (name, age, *rest):
            print(f'Name: {name}, Age: {age}, {rest}')


print_data(('Gasa', 2, 'Google', 27, 12.5))


def print_people(people): # использование массивов в качестве параметов
    match people:
        case ['Gasan', 'Gusen', 'Magomed'] | ['Gasa', 'Guse', 'Mago']:
            print('Default')
        case ['Gasan', *other]:
            print(f'{other}')
        case ['Gasan' | 'Gasa', 'Gusen', 'Magomed']:
            print('Default people')


print_people(['Gasa', 'Gusen', 'Magomed'])


class Person: # ипользование классов в качестве параметров
    __match_args__ = ('name', 'age')
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student:
    def __init__(self, name):
        self.name = name


def print_person(person):
    match person:
        case Person('Gasan' | 'Gasa', 27) | Student(name = 'IGassan'):
            print('Default person')
        case Person(name, 27):
            print(f'Name = {name}')
        case Person('Gasan', age):
            print(f'Age: {age}')
        case Person(name, age) if age < 18:
            print(f'Name: {name}, Age: {age}')
        case _:
            print(f'Not a Person')


print_person(Person('Gaa', 2))
print_person(Student('IGassan'))