from tkinter import *
import tkinter.messagebox as MessageBox
import mysql.connector as mysql
import sys
import os
from PIL import ImageTk, Image   # pip3 install pillow

global Username
Username =  sys.argv[1]


def bm():
    os.execl(sys.executable, "python3", "movie_rating.py")


root = Tk()
root.geometry("1800x1200")
root.title("User Ratings")
title=Label(root, text ="USER PROFILE", font= ('Comic sans ms',50, 'bold', 'underline'))
title.pack(side = "left")
title.place(x=250, y=160)

bg = ImageTk.PhotoImage(Image.open("images/user-bg.jpg").resize((1366,768)))
#bg = (file="images/user-bg.jpg")
bgL = Label(root, image=bg).place(x=-1, y=-1)



connection =mysql.connect(host="localhost", user="ashna03", password="password", database ="movie_project")
cursor = connection.cursor()
query= "select username, FName, LName, gender, email, AGE, contact from users where username = '" + str(Username) +"';"

cursor.execute(query)
result = cursor.fetchall()[0]
#print(Username)
#query1= "select avg(ratings) from user_ratings Inner join users on user_ratings.contact= users.contcat where users.fname = 'uname' "
connection.commit()
connection.close()

uname = Label(root, text = "Username            " + str(result[0]), font= ('Arial',20, 'bold'))
uname.place(x=170, y=270)
name = Label(root, text =  "Name                    " + result[1] + " " + result[2], font= ('Arial',20, 'bold'))
name.place(x=170, y=320)

gender = Label(root, text= "Gender                 " + str(result[3]), font= ('Arial',20, 'bold'))
gender.place(x=170, y=370)

email = Label(root, text = "Email                   "+ str(result[4]),font= ('Arial',20, 'bold'))
email.place(x=170, y=420)

age = Label(root, text =   "Age                      "+ str(result[5]),font= ('Arial',20, 'bold'))
age.place(x=170, y=470)

#avg_rating = Label(root, text ="Average Rating"+ str(result[3]),font= ('Arial',20, 'bold'))
#avg_rating.place(x=320, y=520)

title0=Label(root, text ="A.R. Movies Homepage", font= ('Comic sans ms',35, 'bold'))
title0.pack(side = "left")
title0.place(x=150, y=50)



title1=Label(root, text ="Previously rated movies", font= ('Comic sans ms',25, 'bold', 'italic'))
title1.pack(side = "right")
title1.place(x=750, y=300)
title2=Label(root, text ="Movie Name             Ratings", font= ('Comic sans ms',20, 'bold', 'underline' ))
title2.pack(side = "right")
title2.place(x=750, y=350)

connection =mysql.connect(host="localhost", user="ashna03", password="password", database ="movie_project")
cursor = connection.cursor()
contact = result[6]
query = "SELECT COUNT(*) FROM user_rating where contact = " + str(contact) + ";"
cursor.execute(query)
count = cursor.fetchall()[0][0]

if count > 5:
    query = "SELECT * FROM user_rating where contact = " + str(contact) + " limit 5;"
    cursor.execute(query)
    result = cursor.fetchall()
    #print(result)
    ct = 0
    mv = [None] * 5
    mmv = [None] * 5
    for i in result:
        mv[ct]=Label(root, text = str(i[1]) , font= ('Comic sans ms',15, 'bold' ))
        mv[ct].pack(side = "right")
        mv[ct].place(x=750, y=(420 + 50*ct))
        #print(movie[ct])
        mmv[ct]=Label(root, text = str(i[2]) , font= ('Comic sans ms',15, 'bold'))
        mmv[ct].pack(side = "right")
        mmv[ct].place(x=1100, y=(420 + 50*ct))
        ct+=1



else:
    query = "SELECT * FROM user_rating where contact = " + str(contact) + " limit " +  str(count) + ";"
    cursor.execute(query)
    result = cursor.fetchall()
    #print(result)
    ct = 0
    mv = [None] * count
    mmv = [None] * count
    for i in result:
        mv[ct]=Label(root, text = str(i[1]) , font= ('Comic sans ms',15, 'bold' ))
        mv[ct].pack(side = "right")
        mv[ct].place(x=750, y=(420 + 50*ct))
        #print(movie[ct])
        mmv[ct]=Label(root, text = str(i[2]) , font= ('Comic sans ms',15, 'bold' ))
        mmv[ct].pack(side = "right")
        mmv[ct].place(x=1100, y=(420 + 50*ct))


        ct+=1



title3=Label(root, text ="Watchlisted movies", font= ('Comic sans ms',25, 'bold', 'italic'))
title3.pack(side = "right")
title3.place(x=750, y=50)
title4=Label(root, text ="Movie Name", font= ('Comic sans ms',20, 'bold', 'underline' ))
title4.pack(side = "right")
title4.place(x=750, y=100)


query = "SELECT COUNT(*) FROM watchlist where contact = " + str(contact) + ";"
cursor.execute(query)
count = cursor.fetchall()[0][0]

if count > 3:
    query = "SELECT * FROM watchlist where contact = " + str(contact) + " limit 5;"
    cursor.execute(query)
    result = cursor.fetchall()
    #print(result)
    ct = 0
    movie = [None] * 5
    for i in result:
        movie[ct]=Label(root, text = str(i[1]), font= ('Comic sans ms',15, 'bold' ))
        movie[ct].pack(side = "right")
        movie[ct].place(x=750, y=(150 + 50*ct))
        #print(movie[ct])
        ct+=1



else:
    query = "SELECT * FROM watchlist where contact = " + str(contact) + " limit 5;"
    cursor.execute(query)
    result = cursor.fetchall()
    #print(result)
    ct = 0
    movie = [None] * count
    for i in result:
        movie[ct]=Label(root, text = str(i[1]), font= ('Comic sans ms',15, 'bold' ))
        movie[ct].pack(side = "right")
        movie[ct].place(x=750, y=(150 + 50*ct))
        #print(movie[ct])
        ct+=1

connection.close()




#bg = ImageTk.PhotoImage(file="Untitled.png")
#bgL = Label(root, image=bg).place(x=0, y=0, relwidth=1, relheight=1)









BM = Button(root, text = "Browse Movies", font=('Arial' , 30, 'italic'), bg = "white", command = bm)
BM.place(x=250, y=600)

root.mainloop()
