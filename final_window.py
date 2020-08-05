import tkinter as tk
from tkcalendar import *
from urllib import *
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
from urllib.parse import urlparse
from tkinter import filedialog

root = tk.Tk()
root.title("Result Downloader")
width, height = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry('%dx%d+0+0' % (width, height))
heading=tk.Label(root,text='Result Downloader',font=('Times Roman New',40,'bold'))
heading.grid(row=0,column=1)
link_url = tk.Label(root, text='URL', font=('Calibre', 10, 'bold'))
link_url.grid(row=3, column=0)
link_url.place(x=0,y=70)
link_entry = tk.Entry(root, font=('calibre', 10, 'normal'),width=45)
link_entry.grid(row=3, column=1)
link_entry.place(x=145,y=70)


def submit():
    url = link_entry.get()
    if not urlparse(url).scheme:
        url = 'http://' + url
    req = Request(url)
    text = ''
    try:
        response = urlopen(req)

    except HTTPError as e:
        text = '❌ not Valid'
    except URLError as e:
        text = '❌ not Valid'
    else:
        text = '✅ Valid'
    valid = tk.Label(root, text=text)
    valid.grid(row=3, column=3)


check_valid = tk.Button(root, text='validate', command=submit)
check_valid.grid(row=3, column=2)
check_valid.place(x=515,y=65)


def select_path():
    path = filedialog.askdirectory()
    pathvar.set(path)


pathvar = tk.StringVar()
pathvar.set('')
path_label = tk.Label(root, text='Download location', font=('calibre', 10, 'bold'))
path_label.grid(row=4, column=0)
path_label.place(x=0,y=100)
pathentry = tk.Entry(root, textvariable=pathvar, font=('calibre', 10, 'normal'), width=45)
pathentry.grid(row=4, column=1)
pathentry.place(x=145,y=100)
pathbtn = tk.Button(root, text='select folder', command=select_path)
pathbtn.grid(row=4, column=2)
pathbtn.place(x=515,y=100)

Opt = tk.Label(root, text='Choose Method:',font=('calibre',10,'bold'))
Opt.grid(row=5, column=0)
Opt.place(x=0,y=129)
personal = tk.Checkbutton(root, text='Personal')
multiple = tk.Checkbutton(root, text='By DataBase')
personal.grid(row=5,column=1)
multiple.grid(row=5,column=2)
personal.place(x=135,y=128)
multiple.place(x=220,y=128)
root.mainloop()
