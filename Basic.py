""" import message # подключение модулей
import locale
import random
from message import print_message as diplay
from decimal import Decimal


print(message.hello) # использование модулей

message.print_message('Gasan')

diplay('Hello')

number1 = random.random() * 100 # испоьзование модуля random
print(number1)

number1 = random.randint(10, 50)
print(number1)

number1 = [1, 2, 3, 4, 5, 6, 7, 8] # работа со списком
random.shuffle(number1)
print(number1)
print(random.choice(number1))


print(locale.getlocale()) # использование модуля locale 

print(0.1 + 0.1 + 0.1)

numb = Decimal('0.1')  # использование модуля decimal
print(numb + 0.1 + numb) """


from unicodedata import name


text = ('Myn name is Gasan.' # работа со строками
        'I am 27 years old.')

print(text)

text = '''My name is Gasan. многострочный вывод
I am 27 years old'''

print(text)

text = r'D:\python\name.txt' # вывод текста со слешем

print(text)
print(ord('A')) # числовое значение символа
print('python' in text) # поиск в строке 
print(len(text)) # получение длины строки
print(text[0]) # обращене к символам в строке
print(text[2:9]) # получение подстроки 
print(text.find('python')) # поиск в строке с нахождением индекса начала подстроки
print(text.replace('python', '-')) # замена в строке
print(text.split('n')) # разделение строк
print('|'.join(text)) # соединение строк
print('My name is {name}. I am {age} years old.'.format(name = 'Gasan', age = 27))