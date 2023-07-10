from tkinter import *
import tkinter.messagebox as MessageBox
import mysql.connector as mysql
import sys
from PIL import ImageTk, Image   # pip3 install pillow    connection =mysql.connect(host="localhost", user="ashna03",password="password", database ="movie_project")

moviename = sys.argv[1]


def wl():
    connection =mysql.connect(host="localhost", user="ashna03",password="password", database ="movie_project")
    cursor = connection.cursor()
    moviename= sys.argv[1]
    print(moviename)
    query = "Select * from movie_ratings where primary_title='"+ str(moviename) + "'"
    cursor.execute(query)
    result = cursor.fetchone()
    print(result)
    tid = result[0]
    moviename = result[3]

    query = "INSERT INTO watchlist VALUES('" + str(tid) + "','" + str(moviename) + "',1111111111);"
    cursor.execute(query)
    connection.commit()
    connection.close()
    MessageBox.showinfo("Insert Status", moviename+ " entered into watchlist")



def rt():
    nnW = Toplevel(root)
    #nnW.geometry("1800x1200")
    nnW.title("Rating")



def enter_rating():
    connection =mysql.connect(host="localhost", user="ashna03",password="password", database ="movie_project")
    cursor = connection.cursor()
    moviename= sys.argv[1]
    rating = e_rate.get()
    print(moviename)
    print(rating)
    query = "Select * from movie_ratings where primary_title='"+ str(moviename) + "'"
    cursor.execute(query)
    result = cursor.fetchone()
    print(result)
    tid = result[0]
    moviename = result[3]

    query = "INSERT INTO user_rating VALUES('" + str(tid) + "','" + str(moviename) + "', " + rating + " ,1111111111);"
    #print(query)
    cursor.execute(query)
    connection.commit()
    connection.close()
    MessageBox.showinfo("Insert Status", "You have given " + moviename+ "a rating of " + str(rating))













connection =mysql.connect(host="localhost", user="ashna03",password="password", database ="movie_project")
cursor = connection.cursor()
query = "Select * from movie_ratings where primary_title='"+ str(moviename) + "'"
cursor.execute(query)
result = cursor.fetchone()

tid = result[0]
print(tid)
type = result[1]
year = result[2]
moviename = result[3]
print(moviename)
runtime = result[4]
genres = result[5]
rating = result[6]
votes = result[7]
connection.close()


root = Tk()
root.geometry("1800x1200")
root.title(moviename)

bg = ImageTk.PhotoImage(file="images/back.jpg")
bgL = Label(root, image=bg).place(x=0, y=0, relwidth=1, relheight=1)


title0=Label(root, text ="Movies Browser", font= ('Comic sans ms',35, 'bold'))
title0.pack(side = "left")
title0.place(x=300, y=150)

mname = Label(root, text =  "Movie             " + str(moviename), font= ('Arial',25, 'bold'))
mname.place(x=300, y=300)

genre = Label(root, text =  "Genre            " + genres.split(',')[0], font= ('Arial',25, 'bold'))
genre.place(x=300, y=370)

ratings = Label(root, text ="Rating            " + str(rating), font= ('Arial',25, 'bold'))
ratings.place(x=300, y=440)

year1 = Label(root, text =   "Year              "+ str(year),font= ('Arial',25, 'bold'))
year1.place(x=300, y=510)

addtoWatchlist = Button(root, text = "Add to Watchlist", font=('comic sans ms' , 14, 'italic'), bg = "white", command = wl)
addtoWatchlist.place(x=300, y=570)

e_rate = Entry(root)
e_rate.place(x=300, y=650)

rate = Button(root, text = "Rate this Movie", font=('comic sans ms' , 14, 'italic'), bg = "white", command = enter_rating)
rate.place(x=500, y=650)

pic= Image.open("posters/" + str(tid) + ".jpg")
resized =pic.resize((400,550), Image.ANTIALIAS)
#resized.show()
new_pic = ImageTk.PhotoImage(resized)
pict=Label(root, image=new_pic).place(x=800, y= 130)#.pack(pady=20)


root.mainloop()
