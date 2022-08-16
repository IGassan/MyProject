from tkinter import * # использование графического инрефейса

clicks = 0

def click_button():
    global clicks
    clicks += 1
    btn.config(text=f'Clicks {clicks}')

room = Tk() # изпользование конструктора графического окна
room.title('Графическая программма  на Python') # установка загаловка окна
room.geometry('550x500+500+500') # установка размера окна

btn = Button(text= 'Clicks: 0',  background= '#555', foreground='#ccc',
            padx='20', pady='8', font='16', command=click_button) # создание кнопки
btn.place(relx= .5, rely= .8, anchor= 'nw', height= 30, width= 130, bordermode=OUTSIDE)  # вывод кнопки и позиционирование элемента

for r in range(5):
    for c in range(5):
        btn1 = Button(text=f'{r} - {c}')
        btn1.grid(row=r, column=c, ipadx=10, ipady=6, padx=10, pady=10)

room.mainloop() # вывод графического окна 


from tkinter import *
from tkinter import messagebox

def clear():
    name_entry.delete(0, END)
    surname_entry.delete(0, END)

def display():
    messagebox.showinfo('IGassan', name_entry.get() + ' ' + surname_entry.get())


root = Tk()
root.title('IGasan')
root.geometry('500x400')

name_label = Label(text='Inter your name: ') # текстовая метка 
surname_label = Label(text='Inter your surname: ')

name_label.grid(row=0, column=0, sticky='w')
surname_label.grid(row=1, column=0, sticky='w')

name_entry = Entry() # поле для ввода текста
surname_entry = Entry()

name_entry.grid(row=0, column=1, padx=5, pady=5)
surname_entry.grid(row=1, column=1, padx=5, pady=5)

name_entry.insert(0, 'Gasan')
surname_entry.insert(0, 'Kurbanismailov')


diplay_button = Button(text= 'Display', command=display)
clear_button = Button(text='Clear', command=clear)

diplay_button.grid(row=2, column=0, padx=5, pady=5, sticky='e')
clear_button.grid(row=2, column=1, padx=5, pady=5, sticky='e')

root.mainloop()



from tkinter import * 

root = Tk()
root.title('IGasan')
root.geometry('500x400')

ismarried = IntVar()

ismarried_checkbutton = Checkbutton(text='Женат/Замужем', variable=ismarried) # использование флажка
ismarried_checkbutton.pack()

ismarried_label = Label(textvariable=ismarried)
ismarried_label.place(relx=.5, rely=.5, anchor='c')

python_lang = IntVar()
python_checkbutton = Checkbutton(text="Python", variable=python_lang, onvalue=1, offvalue=0, padx=15, pady=10)
python_checkbutton.pack()

root.mainloop()


from tkinter import * 

root = Tk()
root.title('IGasan')
root.geometry('500x400')

header = Label(text='Выберите курс', padx=15, pady=10)
header.grid(row=0, column=0, sticky=W)

lang = IntVar()

python_checkbutton = Radiobutton(text='Python', value=1, variable=lang, padx=15, pady=10) # использование флажка с одномоментным выбором
python_checkbutton.grid(row=1, column=0, sticky=W)

java_checjbutton = Radiobutton(text='Java', value=2, variable=lang, padx=15, pady=10)
java_checjbutton.grid(row=2, column=0, sticky=W)

selection = Label(textvariable=lang, padx=15, pady=10)
selection.grid(row=3, column=0, sticky=W)

root.mainloop()


from tkinter import *

languages = ["Python", "JavaScript", "C#", "Java", "C/C++", "Swift",
             "PHP", "Visual Basic.NET", "F#", "Ruby", "Rust", "R", "Go",
             "T-SQL", "PL-SQL", "Typescript"]

root = Tk()
root.title('IGassan')

scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

language_listbox = Listbox(yscrollcommand=scrollbar.set, width=40) # использование списка элементов

for language in languages:
    language_listbox.insert(END, language)

language_listbox.pack(side=LEFT, fill=BOTH)
#scrollbar.config(command=language_listbox.yview)

root.mainloop()


from tkinter import *
from tkinter import messagebox

def edit_click():
    messagebox.showinfo('Hi!', 'Edit')

root = Tk()
root.title('IGassan')
root.geometry('500x400')

main_menu = Menu() # создание пункта меню

file_menu = Menu(tearoff=0)
file_menu.add_command(label='New')
file_menu.add_command(label='Save')
file_menu.add_command(label='Open')
file_menu.add_separator()
file_menu.add_command(label='Exit')


main_menu.add_cascade(label='File', menu=file_menu)
main_menu.add_cascade(label='Edit', command=edit_click)
main_menu.add_cascade(label='View')

root.config(menu=main_menu)
root.mainloop()