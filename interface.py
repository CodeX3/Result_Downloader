import tkinter as tk

from tkcalendar import *
from urllib import *


root = tk.Tk()
root.title("Interface Window")
'''root.geometry("500x500+300+120")'''
regno_var = tk.StringVar()
dob_var = tk.StringVar()


from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
req = Request('https://www.google.co.in/')
try:
    response = urlopen(req)
except HTTPError as e:
    print('The server couldn\'t fulfill the request.')
    print('Error code: ', e.code)
except URLError as e:
    print('We failed to reach a server.')
    print('Reason: ', e.reason)
else: print('ok done ')

def submit():
    regno = regno_entry.get()
    dob = dob_var.get()
cal=Calendar(root,selectmode="day",year=2020,month=7,day=30)
cal.pack(pady=20)

regno_var.set("")
dob_var.set("")


regno_label = tk.Label(root, text='register number', font=('calibre', 10, 'bold'))

regno_entry = tk.Entry(root, textvariable=regno_var, font=('calibre', 10, 'normal'))

dob_label = tk.Label(root, text='Dato of birth', font=('calibre', 10, 'bold'))
dob_entry = tk.Entry(root, textvariable=dob_var, font=('calibre', 10, 'normal'))
sub_btn = tk.Button(root, text='Submit', command=submit)
regno_label.pack()
regno_entry.pack()
dob_label.pack()
dob_entry.pack()
sub_btn.pack()

def grab_date():
    mylabel.config(text=cal.get_date())

mybutton=tk.Button(root,text="Select date",command=grab_date)
mybutton.pack(pady=20)

mylabel=tk.Label(root,text="")
mylabel.pack(pady=20)


root.mainloop()
