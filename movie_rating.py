## need to write a page to display the info now
from tkinter import *
import os
import sys
import tkinter as tk
import tkinter.messagebox as MessageBox
import mysql.connector as mysql

from PIL import ImageTk, Image   # pip3 install pillow



def fetch():
    moviename= e_moviename.get()
    os.execl(sys.executable, "python3", "movie.py", moviename)




root = Tk()
root.geometry("1800x1200")
root.title("Registration Form")

bg = ImageTk.PhotoImage(file="images/back.jpg")
bgL = Label(root, image=bg).place(x=0, y=0, relwidth=1, relheight=1)



moviename = Label(root, text ="Movie Name",font= ('comic sans ms',15, 'bold'))
moviename.place(x=500, y=130)

e_moviename = Entry()
e_moviename.place(x=650, y=130)
Fetch = Button(root, text = "Fetch", font=('comic sans ms' , 14, 'italic'), bg = "white", command = fetch)
Fetch.place(x=650, y=200)




pic= Image.open("graphs.png")
##resized.show()
new_pic = ImageTk.PhotoImage(pic)
pict1=Label(root, image=new_pic).place(x=200, y= 300)

#pic= Image.open("g2.png")
#resized.show()
#new_pic = ImageTk.PhotoImage(pic)
#pict2=Label(root, image=new_pic).place(x=700, y= 300)





root.mainloop()
