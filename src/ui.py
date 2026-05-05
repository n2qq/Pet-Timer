from tkinter import *


def button_pressed(text):
    print(text)



window = Tk(screenName="time")
ent = Entry(window, width=20)
but = Button(window, text='Преобразовать')
lab = Label(window, width=20, bg='black', fg='white')
ent.pack()
but.pack()
lab.pack()
but.bind('<Button-1>', button_pressed)
window.mainloop()
