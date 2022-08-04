class Person: # использование классов (инскапсуляции, атрибутов, свойств, наслование, переопределение функций базового класса, атрибутов класса)
    default_name = 'Underfield'
    __type = 'Person'
    
    def __init__(self, name): 
        if name:
            self.__name = name
        else:
            self.__name = Person.default_name
        self.__age = 18


    @staticmethod
    def print_type():
        print(Person.__type)

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


    def __str__(self):
        return(f'Name: {self.__name}, age - {self.__age}')


class Employee(Person):

    def __init__(self, name, company):
        super().__init__(name)
        self.company = company


    def work(self):
        print(f'{self.name} works. He is {self.age} years old.')

    
    def diplay_info(self):
        super().diplay_info()
        print(f'Company: {self.company}')

gasan = Person('')
gasan.say_hello()
gasan.age = 27
gasan.age = 123
gasan.diplay_info()
print(gasan.name)

gusen = Employee('Gusen', 'Google')
gusen.say_hello()
gusen.age = 21
gusen.age = 123
gusen.diplay_info()

print(isinstance(gasan, Employee)) # проверка принадлежности объекта к опеределнному классу
print(isinstance(gusen, Employee))

Person.print_type()
print(gusen)