from tkinter import *
from tkinter import ttk, font
from PIL import Image, ImageTk
import requests
import json
import feedparser
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



app = Tk()
app.title('Welcome')

# app.attributes('-fullscreen', True)

app.geometry('1600x900')
app.configure(background='#1c2431')



clock_font = font.Font(family='Helvetica', size=20, weight='bold')
headline_font = font.Font(family='Helvetia', size=12, weight='bold')
headline_font_title = font.Font(family='Helvetia', size=14, weight='bold', underline=True)

img_1 = ImageTk.PhotoImage(Image.open("comfy.png"))
img_label = Label(image=img_1, borderwidth=0)
img_label.place(x=150, y=125)


def headlines():
    thirty_min = 1800000
    f = feedparser.parse('https://api.axios.com/feed/top/')
    headline_title_label = Label(app, text=f'Top Headlines', anchor='w', justify='left', wraplength=400, font=headline_font_title, background='#1c2431', fg='white').place(x=650, y=145)
    headline_1_label = Label(app, text=f'• {f.entries[0].title}', anchor='w', justify='left', wraplength=400, font=headline_font, background='#1c2431', fg='white').place(x=650, y=180)
    headline_2_label = Label(app, text=f'• {f.entries[1].title}', anchor='w', justify='left', wraplength=400, font=headline_font, background='#1c2431', fg='white').place(x=650, y=240)
    headline_3_label = Label(app, text=f'• {f.entries[2].title}', anchor='w', justify='left', wraplength=400, font=headline_font, background='#1c2431', fg='white').place(x=650, y=300)
    headline_4_label = Label(app, text=f'• {f.entries[3].title}', anchor='w', justify='left', wraplength=400, font=headline_font, background='#1c2431', fg='white').place(x=650, y=360)
    headline_5_label = Label(app, text=f'• {f.entries[4].title}', anchor='w', justify='left', wraplength=400, font=headline_font, background='#1c2431', fg='white').place(x=650, y=420)
    app.after(thirty_min, headlines)


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

    date_label = Label(app,text=date, anchor='w', justify='left', font=clock_font, background='#1c2431', fg='white').place(x=1075, y=185)

    clock_label = Label(app, text=time, anchor='w', justify='left', font=clock_font, background='#1c2431', fg='white').place(x=1075, y=145)

if __name__ == "__main__":
    clock()
    headlines()
app.mainloop()

    
# .grid(row=1, column=0)
# .grid(row=0, column=0)

# picture = ImageTk.PhotoImage(Image.open('jungle.png'))
# label3 = Label(image=picture)




