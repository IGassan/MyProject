with open("hello.txt", "w") as file: # запись в текствовый файл
    file.write("hello world")


with open("hello.txt", "a") as file: # дозапись в текстовый файл
    file.write("\ngood bye, world")


with open('hello.txt', 'r') as file: # вывод из файла на консоль строки
    for line in file:
        print(line, end='')


with open('hello.txt', 'r') as file: # вывод из файла на консоль всего содержимого
    content = file.readlines()
    for i in content:
        print(i, end='')


filename = 'message.txt' # программа для записи в файл введенных пользователем строк и вывод ее в терминал
messages = list()

for i in range(4):
    message = input('Write a line ' + str(i + 1) + ': ')
    messages.append(message + '\n')

with open(filename, 'a') as file:
    for message in messages:
        file.write(message)

print('Answer')
with open(filename, 'r') as file:
    for message in file:
        print(message, end='')

import pickle  # работы с бинарными файлами

filename = 'users.dat'

users = [
    ['Gasan', 27],
    ['Gusen', 22]
]

with open(filename, 'wb') as file:
    pickle.dump(users, file)

with open(filename, 'rb') as file:
    use = pickle.load(file)
    for user in use:
        print(user)