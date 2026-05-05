from tkinter import Tk, Entry, Button, Label #Changed imports - only things that we use at exatly moment


def button_pressed(text):
    print(text)



window = Tk(screenName="time")
ent = Entry(window, width=20)
but = Button(window, text='Преобразовать')
lab = Label(window, width=20, bg='black', fg='white')
ent.pack()
but.pack()
lab.pack()
but.bind('<Button-1>', button_pressed) #Find out how this method works
window.mainloop()
