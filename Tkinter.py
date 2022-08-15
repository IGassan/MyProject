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

