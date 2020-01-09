from tkinter import *
import requests
import json




app = Tk()
app.title('test')
app.geometry('700x350')
label1 = Label(app, text='Hello')
label2 = Label(app, text='Hello00')

label1.grid(row=0, column=0)
label2.grid(row=1, column=0)

app.mainloop()
