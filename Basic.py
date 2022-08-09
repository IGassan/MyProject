import message # подключение модулей
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
print(numb + 0.1 + numb)