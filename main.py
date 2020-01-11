from tkinter import *
from tkinter import ttk, font
from PIL import Image, ImageTk
import requests
import json
import time
import datetime
import sys
import os

if os.environ.get('DISPLAY','') == '':
    print('no display found. Using :0.0')
    os.environ.__setitem__('DISPLAY', ':0.0')
#things to add:
# Weather
# Air Quality
# News Headlines
# 



app = Tk()
app.title('Welcome')

# app.attributes('-fullscreen', True)

app.geometry('1600x900')
app.configure(background='black')


app.iconbitmap('rocket.ico')
clock_font = font.Font(family='Helvetica', size=20, weight='bold')
headline_font = font.Font(family='Helvetia', size=12, weight='bold')


img_1 = ImageTk.PhotoImage(Image.open(""))


# def reddit_all():
#     thirty_min = 1800000
#     headers = {'Authorization': 'itK-P8RvowdxI1KHUjUYF-fpAq0', "User-Agent": "Desktop Start Page by bbellini"}
#     r = requests.get('https://www.reddit.com/r/all/.json', headers=headers)
#     rall = r.json()

#     rall_headline_1_title = rall['data']['children'][0]['data']['title']
#     rall_headline_1_sub = rall['data']['children'][0]['data']['subreddit']

#     rall_headline_1 = rall_headline_1_title + ' via r/' + rall_headline_1_sub
#     rall_headline_1_label = Label(app, text = rall_headline_1, wraplength=500, font=headline_font, background = 'black', fg = 'white').grid(row=0, column=1)
#     outline_label = LabelFrame(rall_headline_1_label, text='Reddit All')
#     app.after(thirty_min, reddit_all)

def clock():
    time = datetime.datetime.now().strftime("%I:%M:%S %p")
    date = datetime.datetime.now().strftime('%A %d %B %Y')
    app.after(1000, clock)

    date_label = Label(app,text=date, font=clock_font).grid(row=1, column=0)
    clock_label = Label(app, text=time, font=clock_font).grid(row=0, column=0)

if __name__ == "__main__":
    clock()
    reddit_all()
app.mainloop()

    


# picture = ImageTk.PhotoImage(Image.open('jungle.png'))
# label3 = Label(image=picture)




