from tkinter import *
from tkinter import ttk, font
from PIL import Image, ImageTk
import requests
import json
import time
import datetime

#things to add:
# Weather
# Air Quality
# News Headlines
# 




app = Tk()
app.title('Welcome')
# mainframe = ttk.Frame(app, padding="100 100 100 100")
# mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
# app.columnconfigure(0, weight=1)
# app.rowconfigure(0, weight=1)
# app.geometry('700x350')
app.iconbitmap('rocket.ico')
clock_font = font.Font(family='Helvetica', size=20, weight='bold')

def clock():
    time = datetime.datetime.now().strftime("%I:%M:%S %p")
    date = datetime.datetime.now().strftime('%A %d %B %Y')
    app.after(1000, clock)

    date_label = Label(app,text=date, font=clock_font).grid(row=1, column=1)
    clock_label = Label(app, text=time, font=clock_font).grid(row=0, column=1)


clock()
app.mainloop()

    


# picture = ImageTk.PhotoImage(Image.open('jungle.png'))
# label3 = Label(image=picture)




