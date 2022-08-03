class Person: # использование классов (инскапсуляции, атрибутов, свойств)
    def __init__(self, name):
        self.__name = name
        self.__age = 18

    @property
    def age(self):
        return self.__age


    @age.setter
    def age(self, age):
        if 1 < age <110:
            self.__age = age
        else:
            print('Неправильно введен возраст')
    
    @property
    def name(self):
        return self.__name
    

    def message(self, message):
        print(message)


    def say_hello(self):
        self.message('Hi!')


    def diplay_info(self):
        print(f'Name: {self.__name} Age: {self.__age}')


class Employee(Person):
    def work(self):
        print(f'{self.name} works. He is {self.age} years old.')

gasan = Person('Gasan')
gasan.say_hello()
gasan.age = 27
gasan.age = 123
gasan.diplay_info()
print(gasan.name)

gusen = Employee('Gusen')
gusen.say_hello()
gusen.age = 21
gusen.age = 123
gusen.work()
