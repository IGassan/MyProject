""" try: #использование конструкции try..exception..finally, обработка разных типов исключений
    number1 = int(input('Write a first number: '))
    number2 = int(input('Write a second number: '))
    if number2 == 0:
        raise Exception('Division by zero')
    print('Answer: ', number1 / number2)
except ValueError as e:
    print('Transormation', e)
except Exception as e:
    print('Igas')
except BaseException as e:
    print('Error!', e)
print('The end') """


class PersonAgeException(Exception): # генерация исключений и создание своих типов иисключений
    def __init__(self, age, minage, maxage):
        self.age = age
        self.minage = minage
        self.maxage = maxage

    def __str__(self):
        return f'Недопустимое значение: {self.age}. ' \
            f'Возраст между {self.minage} до {self.maxage}'


class Person:
    def __init__(self, name, age):
        self.__name = name
        minage, maxage = 1, 110
        if minage < age < maxage:
            self.__age = age
        else:
            raise PersonAgeException (age, minage, maxage)

        
    def display_info(self):
        print(f'Name: {self.__name} Age: {self.__age}')

    
try:
    gasan = Person('Gasan', 27)
    gasan.display_info()

    gusen = Person('Gusen', -21)
    gusen.display_info
except PersonAgeException as e:
    print(e)
